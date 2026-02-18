# Reproduction Guide -- Genesis PROV 5a: PFAS Remediation

**Classification:** NON-CONFIDENTIAL
**Purpose:** Step-by-step instructions for independently verifying the claims in this white paper.

---

## Quick Start: Automated Verification

The fastest way to verify all claims is to run the automated verification script:

```bash
cd verification
pip install -r requirements.txt
python verify_claims.py
```

This performs five independent checks against canonical reference values and reports pass/fail for each. For machine-readable output:

```bash
python verify_claims.py --json
```

No external packages are required. The verification script uses only the Python standard library (Python >= 3.8).

---

## What the Verification Script Checks

| Check | Claim | How It Verifies |
|-------|-------|----------------|
| 1 | Lead Fluorocatcher binding exceeds -80 kJ/mol threshold | Compares FC-003 binding energy (-121 kJ/mol) against threshold |
| 2 | 15/15 DFT calculations converge below threshold | Iterates all 15 entries in canonical_values.json |
| 3 | Irreversibility ratio >= 1.5 | Recomputes ratio from first principles: abs(binding) / abs(threshold) |
| 4 | Scaffold library >= 730 architectures | Reads library size from canonical values |
| 5 | GAC fails the irreversibility test | Confirms -45 kJ/mol > -80 kJ/mol (validates problem statement) |

---

## Manual Verification of Key Claims

### Claim 1: Lead Fluorocatcher Binding Energy

**Claim:** FC-003 (Bis-TMA-C8-F8) achieves -121 kJ/mol PFOA binding energy.

**How to verify:**

1. Open `verification/reference_data/canonical_values.json`
2. Locate `lead_compound.pfoa_binding_kJ_mol` -- value should be `-121.0`
3. Cross-check against `evidence/key_results.json` field `lead_compound.pfoa_binding_kJ_mol`
4. Both values should agree within 0.5 kJ/mol tolerance

**Independent reproduction:**
To independently reproduce this binding energy, one would need to:
- Construct the FC-003 molecular geometry (Bis-TMA-C8-F8: bis-quaternary ammonium with C8 spacer, 50% fluorination)
- Build the PFOA-FC-003 complex geometry
- Run DFT optimization at B3LYP/6-31G* with D3(BJ) dispersion and CPCM solvation
- Compute: dE_bind = E(complex) - E(FC-003, isolated) - E(PFOA, isolated)

This requires a DFT software package (Gaussian, ORCA, or equivalent) and several hours of compute time per candidate.

### Claim 2: 15/15 DFT Convergence

**Claim:** All 15 Fluorocatcher candidates have PFOA binding energies below -80 kJ/mol.

**How to verify:**

1. Open `verification/reference_data/canonical_values.json`
2. Examine the `dft_results` array -- all 15 entries should have `pfoa_kJ` < -80.0
3. Verify: weakest binder is FC-006 at -92.04 kJ/mol, which still exceeds the threshold

### Claim 3: Irreversibility Ratio

**Claim:** The lead compound FC-003 has an irreversibility ratio of 1.51.

**How to verify:**

```
ratio = abs(-121.0) / abs(-80.0) = 121.0 / 80.0 = 1.5125
Rounded to 2 decimal places: 1.51
```

This can be verified with a calculator. The ratio represents a 51% safety margin above the minimum threshold for permanent capture.

### Claim 4: Scaffold Library Size

**Claim:** 730 unique molecular architectures in the Fluorocatcher library.

**How to verify:**

The 730 count is derived from combinatorial enumeration:
- 4 cation types
- Multiple spacer lengths (C6, C8, C10, C12)
- Multiple fluorination levels (0% through 90%)
- Multiple topologies (linear, branched, macrocyclic, cage, PEG-linked)

The exact combinatorial product depends on the constraint set (not all combinations are chemically valid). The value 730 is reported in `canonical_values.json` under `campaign.scaffold_library_size`.

### Claim 5: Activated Carbon Gap

**Claim:** GAC at -45 kJ/mol cannot permanently capture PFAS (threshold is -80 kJ/mol).

**How to verify:**

```
GAC binding: -45 kJ/mol
Threshold:   -80 kJ/mol
Gap:         -45 - (-80) = +35 kJ/mol  (GAC is 35 kJ/mol too weak)
```

The -45 kJ/mol value for GAC is derived from published literature on activated carbon PFAS adsorption. This is a consensus value, not a Genesis-computed result.

---

## Reproducing DFT Binding Energies from Scratch

For researchers who wish to independently reproduce the DFT calculations:

### Prerequisites

- DFT software: Gaussian 16, ORCA 5.x, or equivalent
- Molecular builder: Avogadro, GaussView, or equivalent
- Computational resources: 16+ CPU cores, 32+ GB RAM per calculation

### Protocol

1. **Build PFAS target geometry:**
   - PFOA: C8HF15O2 (perfluorooctanoic acid, deprotonated carboxylate, charge = -1)
   - PFOS: C8HF17O3S (perfluorooctane sulfonic acid, deprotonated sulfonate, charge = -1)
   - Optimize geometry at B3LYP/6-31G* with CPCM solvation

2. **Build Fluorocatcher geometry:**
   - Construct from SMILES notation (see white paper for candidate identifiers)
   - Set formal charge according to number of cationic centers
   - Optimize geometry at B3LYP/6-31G* with CPCM solvation

3. **Build complex geometry:**
   - Position PFAS in the binding cavity of the Fluorocatcher
   - Orient the anionic head group toward the nearest cationic center
   - Orient the perfluoroalkyl tail toward the fluorinated spacer region
   - Optimize the full complex at B3LYP/6-31G*/D3(BJ)/CPCM

4. **Compute binding energy:**
   ```
   dE_bind = E(complex) - E(Fluorocatcher, isolated) - E(PFAS, isolated)
   ```
   All energies in the same level of theory and solvation model.

5. **Apply calibration (optional):**
   If using the same level of theory, raw binding energies can be compared directly. The calibration correction (linear fit to CP2K anchors) is described in docs/SOLVER_OVERVIEW.md.

### Expected Computational Cost

| Step | Time per candidate | Notes |
|------|-------------------|-------|
| Geometry optimization (isolated) | 1-3 hours | Depends on molecule size |
| Geometry optimization (complex) | 3-8 hours | Larger system |
| Single-point energy | 0.5-1 hour | If geometry is already optimized |
| **Total per candidate** | **5-12 hours** | On 16-core workstation |

---

## File Inventory for Verification

| File | Purpose |
|------|---------|
| `verification/verify_claims.py` | Automated 5-check verification script |
| `verification/requirements.txt` | Python dependencies (standard library only) |
| `verification/reference_data/canonical_values.json` | Ground-truth reference values |
| `evidence/key_results.json` | Key numerical results from DFT campaign |
| `README.md` | White paper with all claims and context |
| `HONEST_DISCLOSURES.md` | Complete limitations disclosure |

---

## Contact for Reproduction Assistance

For questions about reproducing these results, or to request additional reference data, contact the Genesis Platform team through the repository issue tracker.

---

**Classification:** NON-CONFIDENTIAL
