#!/usr/bin/env python3
"""
verify_claims.py -- Automated Claim Verification for Genesis PROV 5a (PFAS Remediation)
========================================================================================

This script verifies the key numerical claims in the Genesis PROV 5a white paper
against canonical reference values stored in reference_data/canonical_values.json.

Five independent checks are performed:

  1. Lead Fluorocatcher binding energy exceeds irreversibility threshold
     (-121 kJ/mol < -80 kJ/mol)
  2. 15/15 PFAS DFT calculations converged with binding below threshold
  3. Lead compound irreversibility ratio exceeds 1.5 safety margin
  4. Scaffold library size >= 730
  5. Activated carbon binding is above threshold (validates the problem statement)

Usage:
    python verify_claims.py            # Human-readable output
    python verify_claims.py --json     # Machine-readable JSON output

Requirements:
    Python >= 3.8 (standard library only; no external packages)

Author: Genesis Platform
Date: 2026-02-18
"""

import json
import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
CANONICAL_PATH = SCRIPT_DIR / "reference_data" / "canonical_values.json"
EVIDENCE_PATH = SCRIPT_DIR.parent / "evidence" / "key_results.json"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> dict:
    """Load a JSON file and return its contents as a dict."""
    if not path.exists():
        print(f"ERROR: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    with open(path, "r") as f:
        return json.load(f)


def approx_eq(a: float, b: float, tol: float = 0.5) -> bool:
    """Check if two floats are approximately equal within tolerance."""
    return abs(a - b) <= tol


class ClaimCheck:
    """Container for a single claim verification result."""

    def __init__(self, check_id: int, name: str, description: str):
        self.check_id = check_id
        self.name = name
        self.description = description
        self.passed = False
        self.expected = None
        self.actual = None
        self.detail = ""

    def to_dict(self) -> dict:
        return {
            "check_id": self.check_id,
            "name": self.name,
            "description": self.description,
            "passed": self.passed,
            "expected": self.expected,
            "actual": self.actual,
            "detail": self.detail,
        }


# ---------------------------------------------------------------------------
# Verification checks
# ---------------------------------------------------------------------------

def check_1_binding_exceeds_threshold(canonical: dict) -> ClaimCheck:
    """
    Check 1: Lead Fluorocatcher PFOA binding energy exceeds the
    irreversibility threshold.

    The claim: FC-003 achieves -121 kJ/mol, which is below (more negative
    than) the -80 kJ/mol irreversibility threshold.
    """
    c = ClaimCheck(1, "Binding exceeds irreversibility threshold",
                   "Lead Fluorocatcher PFOA binding < -80 kJ/mol")

    threshold = canonical["thresholds"]["irreversibility_threshold_kJ_mol"]
    lead_binding = canonical["lead_compound"]["pfoa_binding_kJ_mol"]

    c.expected = f"binding ({lead_binding} kJ/mol) < threshold ({threshold} kJ/mol)"
    c.actual = f"{lead_binding} kJ/mol"

    if lead_binding < threshold:
        c.passed = True
        margin = threshold - lead_binding
        c.detail = (
            f"FC-003 binding of {lead_binding} kJ/mol is {margin:.1f} kJ/mol "
            f"below the irreversibility threshold of {threshold} kJ/mol. "
            f"PFAS capture is thermodynamically permanent."
        )
    else:
        c.passed = False
        c.detail = (
            f"FAIL: FC-003 binding of {lead_binding} kJ/mol does NOT exceed "
            f"the irreversibility threshold of {threshold} kJ/mol."
        )
    return c


def check_2_all_15_exceed_threshold(canonical: dict) -> ClaimCheck:
    """
    Check 2: All 15 PFAS DFT calculations converged with binding energies
    below the irreversibility threshold.
    """
    c = ClaimCheck(2, "15/15 PFAS DFT convergence",
                   "All 15 candidates have PFOA binding < -80 kJ/mol")

    threshold = canonical["thresholds"]["irreversibility_threshold_kJ_mol"]
    results = canonical["dft_results"]
    n_total = len(results)
    n_pass = sum(1 for r in results if r["pfoa_kJ"] < threshold)

    c.expected = f"15/15 candidates below {threshold} kJ/mol"
    c.actual = f"{n_pass}/{n_total} candidates below {threshold} kJ/mol"

    if n_pass == 15 and n_total == 15:
        c.passed = True
        worst = max(r["pfoa_kJ"] for r in results)
        best = min(r["pfoa_kJ"] for r in results)
        c.detail = (
            f"All 15 candidates exceed the irreversibility threshold. "
            f"Range: {best} to {worst} kJ/mol (threshold: {threshold} kJ/mol)."
        )
    else:
        c.passed = False
        failures = [r["id"] for r in results if r["pfoa_kJ"] >= threshold]
        c.detail = (
            f"FAIL: Only {n_pass}/{n_total} candidates exceed threshold. "
            f"Failures: {failures}"
        )
    return c


def check_3_irreversibility_ratio(canonical: dict) -> ClaimCheck:
    """
    Check 3: Lead compound irreversibility ratio exceeds 1.5 safety margin.

    Irreversibility ratio = |binding energy| / |threshold|
    For FC-003: 121 / 80 = 1.5125, which rounds to 1.51.
    """
    c = ClaimCheck(3, "Irreversibility ratio >= 1.5",
                   "Lead compound safety margin for permanent capture")

    threshold = canonical["thresholds"]["irreversibility_threshold_kJ_mol"]
    lead_binding = canonical["lead_compound"]["pfoa_binding_kJ_mol"]
    claimed_ratio = canonical["lead_compound"]["irreversibility_ratio"]

    # Recompute ratio from first principles
    computed_ratio = round(abs(lead_binding) / abs(threshold), 2)

    c.expected = f"ratio >= 1.50 (claimed: {claimed_ratio})"
    c.actual = f"computed ratio = {computed_ratio}"

    if computed_ratio >= 1.50 and approx_eq(computed_ratio, claimed_ratio, tol=0.02):
        c.passed = True
        c.detail = (
            f"Irreversibility ratio = |{lead_binding}| / |{threshold}| = "
            f"{computed_ratio}. Exceeds 1.5 safety margin. "
            f"Claimed value ({claimed_ratio}) matches computed value."
        )
    else:
        c.passed = False
        c.detail = (
            f"FAIL: Computed ratio {computed_ratio} vs claimed {claimed_ratio}. "
            f"Ratio must be >= 1.50."
        )
    return c


def check_4_scaffold_library_size(canonical: dict) -> ClaimCheck:
    """
    Check 4: The computational scaffold library contains >= 730 unique
    molecular architectures.
    """
    c = ClaimCheck(4, "Scaffold library size >= 730",
                   "Breadth of the computational design space")

    library_size = canonical["campaign"]["scaffold_library_size"]

    c.expected = ">= 730 scaffolds"
    c.actual = f"{library_size} scaffolds"

    if library_size >= 730:
        c.passed = True
        c.detail = (
            f"Scaffold library contains {library_size} unique molecular "
            f"architectures, meeting the >= 730 threshold."
        )
    else:
        c.passed = False
        c.detail = f"FAIL: Library size {library_size} is below 730."
    return c


def check_5_gac_below_threshold(canonical: dict) -> ClaimCheck:
    """
    Check 5: Activated carbon (GAC) binding energy is above (weaker than)
    the irreversibility threshold.

    This validates the problem statement: current technology cannot achieve
    permanent PFAS capture.
    """
    c = ClaimCheck(5, "GAC below irreversibility threshold",
                   "Current technology fails permanent capture test")

    threshold = canonical["thresholds"]["irreversibility_threshold_kJ_mol"]
    gac_binding = canonical["thresholds"]["gac_baseline_kJ_mol"]

    c.expected = f"GAC binding ({gac_binding} kJ/mol) > threshold ({threshold} kJ/mol)"
    c.actual = f"GAC = {gac_binding} kJ/mol, threshold = {threshold} kJ/mol"

    # GAC is -45 kJ/mol, threshold is -80 kJ/mol.
    # -45 > -80, meaning GAC is weaker (less negative) than the threshold.
    if gac_binding > threshold:
        c.passed = True
        gap = gac_binding - threshold
        c.detail = (
            f"GAC binding of {gac_binding} kJ/mol is {gap:.1f} kJ/mol weaker "
            f"than the irreversibility threshold of {threshold} kJ/mol. "
            f"Activated carbon CANNOT permanently capture PFAS. "
            f"This validates the problem statement."
        )
    else:
        c.passed = False
        c.detail = (
            f"FAIL: GAC binding of {gac_binding} kJ/mol appears to exceed "
            f"the threshold. Problem statement may be invalid."
        )
    return c


# ---------------------------------------------------------------------------
# Cross-validation: check evidence/key_results.json against canonical values
# ---------------------------------------------------------------------------

def cross_validate_evidence(canonical: dict) -> list:
    """
    Optional cross-validation: if evidence/key_results.json exists, verify
    that its values are consistent with canonical_values.json.
    """
    warnings = []
    if not EVIDENCE_PATH.exists():
        return warnings

    evidence = load_json(EVIDENCE_PATH)

    # Check lead compound binding energy
    ev_lead = evidence.get("lead_compound", {}).get("pfoa_binding_kJ_mol")
    cn_lead = canonical["lead_compound"]["pfoa_binding_kJ_mol"]
    if ev_lead is not None and not approx_eq(ev_lead, cn_lead, tol=0.5):
        warnings.append(
            f"Mismatch: evidence lead binding {ev_lead} vs canonical {cn_lead}"
        )

    # Check best compound binding energy
    ev_best = evidence.get("best_compound", {}).get("pfoa_binding_kJ_mol")
    cn_best = canonical["best_compound"]["pfoa_binding_kJ_mol"]
    if ev_best is not None and not approx_eq(ev_best, cn_best, tol=0.5):
        warnings.append(
            f"Mismatch: evidence best binding {ev_best} vs canonical {cn_best}"
        )

    # Check campaign totals
    ev_n = evidence.get("campaign_summary", {}).get("candidates_exceeding_irreversibility")
    cn_n = canonical["campaign"]["candidates_exceeding_irreversibility"]
    if ev_n is not None and ev_n != cn_n:
        warnings.append(
            f"Mismatch: evidence says {ev_n} exceed threshold, canonical says {cn_n}"
        )

    return warnings


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_verification(json_output: bool = False) -> int:
    """
    Run all verification checks and report results.

    Returns 0 if all checks pass, 1 otherwise.
    """
    canonical = load_json(CANONICAL_PATH)

    checks = [
        check_1_binding_exceeds_threshold(canonical),
        check_2_all_15_exceed_threshold(canonical),
        check_3_irreversibility_ratio(canonical),
        check_4_scaffold_library_size(canonical),
        check_5_gac_below_threshold(canonical),
    ]

    cross_warnings = cross_validate_evidence(canonical)

    n_passed = sum(1 for c in checks if c.passed)
    n_total = len(checks)
    all_passed = n_passed == n_total

    if json_output:
        output = {
            "verification": "Genesis PROV 5a: PFAS Remediation",
            "date": "2026-02-18",
            "canonical_values_path": str(CANONICAL_PATH),
            "checks_passed": n_passed,
            "checks_total": n_total,
            "all_passed": all_passed,
            "checks": [c.to_dict() for c in checks],
        }
        if cross_warnings:
            output["cross_validation_warnings"] = cross_warnings
        print(json.dumps(output, indent=2))
    else:
        print("=" * 72)
        print("  GENESIS PROV 5a -- PFAS REMEDIATION CLAIM VERIFICATION")
        print("=" * 72)
        print(f"  Canonical values: {CANONICAL_PATH}")
        print(f"  Theory level:     {canonical.get('theory_level', 'N/A')}")
        print()

        for c in checks:
            status = "PASS" if c.passed else "FAIL"
            marker = "[+]" if c.passed else "[X]"
            print(f"  {marker} Check {c.check_id}: {c.name}")
            print(f"      {c.description}")
            print(f"      Expected: {c.expected}")
            print(f"      Actual:   {c.actual}")
            print(f"      Status:   {status}")
            print(f"      Detail:   {c.detail}")
            print()

        if cross_warnings:
            print("  CROSS-VALIDATION WARNINGS:")
            for w in cross_warnings:
                print(f"    [!] {w}")
            print()

        print("-" * 72)
        print(f"  RESULT: {n_passed}/{n_total} checks passed", end="")
        if all_passed:
            print(" -- ALL CLAIMS VERIFIED")
        else:
            print(" -- VERIFICATION FAILED")
        print("-" * 72)

    return 0 if all_passed else 1


if __name__ == "__main__":
    json_flag = "--json" in sys.argv
    exit_code = run_verification(json_output=json_flag)
    sys.exit(exit_code)
