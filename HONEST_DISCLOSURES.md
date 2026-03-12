# HONEST DISCLOSURES -- Genesis PROV 5a: PFAS Remediation

**Purpose:** Complete transparency about what this work is and what it is not.
**Last Updated:** February 18, 2026

---

## 1. All Results Are Computational -- No Experimental Validation

Every binding energy, isotherm prediction, regeneration estimate, and performance claim in this repository is derived from computational modeling. For PFAS binding, the method is an analytical Coulomb+LJ+Born model (classical physics), NOT quantum DFT -- see Section 2 below. Only 2 of the 15 PFAS binding energies come from actual quantum DFT (CP2K). No physical experiment has been conducted.

Specifically:

- **No Fluorocatcher molecules have been synthesized.** The 405 scaffolds (in `expanded_candidates.sdf`) and 15 computationally-estimated candidates exist only as computational models.
- **No experimental binding isotherms have been measured.** The Langmuir isotherm analysis (K_bind = 10^17 L/mol) is computed from analytical binding energy estimates using standard thermodynamic relationships, not from experimental adsorption data.
- **No filtration tests have been conducted.** No water has been passed through any Fluorocatcher-based filter medium. Claims about EPA MCL compliance at 4 ppt are thermodynamic predictions, not measured performance.
- **No pilot-scale or field tests exist.** The application scenarios described (municipal water treatment, DoD site remediation, industrial PFAS capture) are projected use cases based on computed performance, not demonstrated installations.

**What would change this:** Synthesizing the top 3 Fluorocatcher candidates and measuring experimental binding isotherms at PFAS concentrations from 4 ppt to 1 ppb. Estimated cost: $50,000. Estimated timeline: 4-8 weeks at a university chemistry partnership. This is the single highest-value next step for the entire PFAS program.

---

## 2. Binding Energy Method: Analytical Coulomb+LJ+Born Model (NOT Quantum DFT)

### CRITICAL CORRECTION: The PFAS binding energies are NOT computed using quantum DFT.

The 15/15 PFAS binding energy estimates use an **analytical Coulomb+Lennard-Jones+Born model** -- a classical physics approximation, not an electronic structure calculation. No quantum mechanical calculation (B3LYP, HF, or any other level of theory) is performed for the 13 expanded candidates (PFAS_Capture_002 through _014). The method computes:

- **Coulombic interaction** between cationic Fluorocatcher centers and anionic PFAS head groups (classical electrostatics with effective dielectric screening)
- **Lennard-Jones van der Waals** terms for fluorine-fluorine contacts (using OPLS-AA parameters, not quantum-derived)
- **Born desolvation penalty** for partial stripping of hydration shells (continuum solvation approximation)
- **Empirical dispersion** correction term

These four classical terms are summed and then **linearly calibrated** against 2 CP2K anchor points (PFAS_Capture_000 at -97 kJ/mol and PFAS_Capture_001 at -121 kJ/mol). The calibration maps the raw analytical energies to a scale anchored by actual DFT calculations, but the underlying physics is classical, not quantum mechanical.

### What this means for accuracy

- The method is appropriate for **relative ranking** of candidates (which Fluorocatcher binds more strongly)
- It is NOT appropriate for **absolute binding energy prediction** -- the 2-point linear calibration has no degrees of freedom for error estimation
- Molecules very different from the two anchors (e.g., cage/cryptand topologies FC-010, FC-011, FC-015) may have larger systematic errors
- The method does not capture quantum effects such as charge transfer, orbital interactions, or explicit electron correlation

### Why this matters

Previous versions of this repository labeled the method as "B3LYP/6-31G*/D3(BJ)/CPCM" in output JSON files, which implied quantum DFT calculations were performed. This was misleading. The JSON files have been corrected to show "analytical_Coulomb_LJ_Born" as the method. The Python code (`complete_pfas_dft.py`) contains a transparency banner explaining this correction.

Only 2 of the 15 PFAS binding energies come from actual quantum DFT (CP2K PBE/DZVP). The other 13 are analytical estimates.

**What would improve this:** Running actual quantum DFT (e.g., B3LYP/6-31G* or higher) on all 15 Fluorocatcher-PFAS complexes, or running explicit-solvent molecular dynamics with free energy perturbation methods.

---

## 3. No Fabricated Filtration Devices

No physical device of any kind has been built:

- No filter cartridges
- No packed bed columns
- No membrane modules
- No point-of-use water treatment units
- No pilot plant installations

The claim that Fluorocatchers are compatible with "existing filter bed and column geometries" is a design intent statement based on the molecular dimensions and physical properties of the computed scaffolds, not a demonstrated engineering result.

### Regeneration Claims Are Modeled, Not Measured

The regeneration model (98.5% capacity retention per cycle, >200 cycle lifetime) is derived from thermodynamic modeling of the desorption energy barrier at elevated temperatures. This has not been validated by cycling experiments on physical sorbent media.

---

## 4. The 405 Scaffolds Are Computationally Designed, Not Synthesized

The 405-scaffold expanded library (`expanded_candidates.sdf`) was generated through combinatorial enumeration of molecular building blocks:
- 4 cation types
- Multiple spacer lengths
- Multiple fluorination levels
- Multiple topologies

These scaffolds are data structures in a computational library. None have been synthesized. Importantly:

- **Synthetic accessibility has not been individually assessed** for all 405 scaffolds. Some may be synthetically challenging or impractical.
- **Stability in aqueous solution** has not been modeled for all scaffolds. Some cation types (e.g., iminium) may be hydrolytically unstable at neutral pH.
- **Toxicity has not been assessed.** Fluorinated molecules can themselves be environmentally problematic. The irony of using fluorinated sorbents to capture fluorinated pollutants is noted. Any commercialization path must include environmental fate assessment of the Fluorocatcher molecules themselves.

---

## 5. Conformational Sampling Limitations

Each binding energy estimate uses a single low-energy conformer per Fluorocatcher-PFAS complex. This is a common approximation in computational screening but has limitations:

- Flexible molecules (especially those with C10 or C12 spacers) can adopt multiple binding poses
- The true binding free energy is a Boltzmann-weighted average over all accessible conformations
- The single-conformer approximation may overestimate binding if the selected conformer happens to be an unusually favorable pose, or underestimate it if a more favorable pose exists but was not sampled
- Entropy effects (conformational entropy loss upon binding) are not explicitly computed

---

## 6. Environmental and Regulatory Considerations Not Addressed

This work does not address:

- **NSF/ANSI 53 certification** requirements for drinking water treatment chemicals (estimated 12-18 months)
- **EPA registration** requirements for novel water treatment media
- **Environmental fate** of Fluorocatcher molecules (are they biodegradable? do they leach from filter media?)
- **Toxicity testing** of Fluorocatcher molecules (Ames test, aquatic toxicity, mammalian toxicity)
- **Disposal pathway** for spent Fluorocatcher media loaded with captured PFAS

These are essential steps on any path to commercialization and have not been initiated.

---

## 7. The Irreversibility Threshold Is a Modeling Construct

The -80 kJ/mol irreversibility threshold is derived from thermodynamic analysis of desorption kinetics at ambient temperature. It is a useful quantitative benchmark, but:

- The exact threshold depends on temperature, pH, ionic strength, and competing sorbate concentrations
- In real water matrices with complex chemistry (natural organic matter, competing anions, varying pH), the effective threshold may be higher (more negative) than -80 kJ/mol
- The threshold has not been experimentally validated for PFAS-sorbent systems specifically

---

## 8. Market Size Estimates Are External

The $20-40 billion PFAS remediation market estimate and $50 billion+ municipal compliance cost are drawn from public EPA, DoD, and industry analyst reports. We have not independently verified these figures and do not make proprietary market sizing claims.

---

## Summary: What We Claim vs. What We Do Not Claim

| We Claim | We Do NOT Claim |
|----------|-----------------|
| Fluorocatchers computationally bind PFAS 2-6x stronger than GAC | Fluorocatchers have been experimentally proven to capture PFAS |
| 15/15 analytical binding estimates exceed -80 kJ/mol (only 2 are actual DFT) | Binding energies are accurate to chemical accuracy |
| 405 scaffolds computationally designed | 405 scaffolds synthesized or tested |
| Irreversibility ratio > 1.5 for lead compound | Permanent capture demonstrated in filtration test |
| Compatible design with existing infrastructure | Drop-in replacement tested in actual water treatment plant |
| Thermodynamic advantage at 4 ppt concentrations | Measured performance at 4 ppt PFOA/PFOS |

---

**Classification:** NON-CONFIDENTIAL PUBLIC DISCLOSURE
*Honest disclosure of limitations strengthens scientific credibility.*
