# HONEST DISCLOSURES -- Genesis PROV 5a: PFAS Remediation

**Purpose:** Complete transparency about what this work is and what it is not.
**Last Updated:** February 18, 2026

---

## 1. All Results Are Computational -- No Experimental Validation

Every binding energy, isotherm prediction, regeneration estimate, and performance claim in this repository is derived from computational chemistry (density functional theory) and thermodynamic modeling. No physical experiment has been conducted.

Specifically:

- **No Fluorocatcher molecules have been synthesized.** The 730 scaffolds and 15 DFT-validated candidates exist only as computational models.
- **No experimental binding isotherms have been measured.** The Langmuir isotherm analysis (K_bind = 10^17 L/mol) is computed from DFT binding energies using standard thermodynamic relationships, not from experimental adsorption data.
- **No filtration tests have been conducted.** No water has been passed through any Fluorocatcher-based filter medium. Claims about EPA MCL compliance at 4 ppt are thermodynamic predictions, not measured performance.
- **No pilot-scale or field tests exist.** The application scenarios described (municipal water treatment, DoD site remediation, industrial PFAS capture) are projected use cases based on computed performance, not demonstrated installations.

**What would change this:** Synthesizing the top 3 Fluorocatcher candidates and measuring experimental binding isotherms at PFAS concentrations from 4 ppt to 1 ppb. Estimated cost: $50,000. Estimated timeline: 4-8 weeks at a university chemistry partnership. This is the single highest-value next step for the entire PFAS program.

---

## 2. DFT Method Limitations

### Level of Theory: B3LYP/6-31G*/D3(BJ)/CPCM

This is a mid-tier computational chemistry method. It is widely used and well-validated for organic molecular systems, but it has known limitations:

- **B3LYP functional:** Systematic errors of 5-15 kJ/mol for non-covalent interactions. The functional tends to slightly underestimate dispersion interactions even with D3 correction. For our application, this means reported binding energies may be slightly less negative (weaker) than the true values, which would make our claims conservative.

- **6-31G* basis set:** A medium-sized Pople basis set with polarization functions on heavy atoms. Larger basis sets (e.g., 6-311++G(2d,2p) or cc-pVTZ) would reduce basis set superposition error and improve accuracy, but at substantially higher computational cost.

- **D3(BJ) dispersion correction:** Essential for this application because fluorine-fluorine van der Waals interactions contribute substantially to total binding energy. Without D3, DFT would grossly underestimate Fluorocatcher performance. The D3(BJ) parameterization is well-validated for this class of interaction.

- **CPCM implicit solvation:** Models the aqueous environment as a dielectric continuum. This captures the bulk electrostatic effect of water but does not model specific hydrogen bonding between water molecules and the Fluorocatcher-PFAS complex. At the binding interface, explicit water molecules may stabilize or destabilize the complex in ways not captured by CPCM.

### Calibration Limitations

The 15/15 PFAS DFT campaign uses a calibrated B3LYP model anchored to 2 higher-level CP2K reference calculations:
- Anchor 1: FC-001 (Bis-TMA-C8 baseline) at -97 kJ/mol
- Anchor 2: FC-003 (Bis-TMA-C8-F8) at -121 kJ/mol

A linear calibration fit with only 2 anchor points has no degrees of freedom for error estimation. The calibration improves absolute accuracy for molecules similar to the anchors but may introduce systematic errors for molecules with very different architectures (e.g., the cage/cryptand topologies FC-010, FC-011, FC-015).

**What would improve this:** Running 5-10 additional CP2K reference calculations spanning the full range of Fluorocatcher architectures. Alternatively, running coupled-cluster CCSD(T) calculations on small model systems to establish benchmark binding energies.

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

## 4. The 730 Scaffolds Are Computationally Designed, Not Synthesized

The 730-scaffold library was generated through combinatorial enumeration of molecular building blocks:
- 4 cation types
- Multiple spacer lengths
- Multiple fluorination levels
- Multiple topologies

These scaffolds are data structures in a computational library. None have been synthesized. Importantly:

- **Synthetic accessibility has not been individually assessed** for all 730 scaffolds. Some may be synthetically challenging or impractical.
- **Stability in aqueous solution** has not been modeled for all scaffolds. Some cation types (e.g., iminium) may be hydrolytically unstable at neutral pH.
- **Toxicity has not been assessed.** Fluorinated molecules can themselves be environmentally problematic. The irony of using fluorinated sorbents to capture fluorinated pollutants is noted. Any commercialization path must include environmental fate assessment of the Fluorocatcher molecules themselves.

---

## 5. Conformational Sampling Limitations

Each DFT binding energy calculation uses a single low-energy conformer per Fluorocatcher-PFAS complex. This is a common approximation in computational screening but has limitations:

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
| 15/15 DFT calculations converged with binding > -80 kJ/mol | Binding energies are accurate to chemical accuracy |
| 730 scaffolds computationally designed | 730 scaffolds synthesized or tested |
| Irreversibility ratio > 1.5 for lead compound | Permanent capture demonstrated in filtration test |
| Compatible design with existing infrastructure | Drop-in replacement tested in actual water treatment plant |
| Thermodynamic advantage at 4 ppt concentrations | Measured performance at 4 ppt PFOA/PFOS |

---

**Classification:** NON-CONFIDENTIAL PUBLIC DISCLOSURE
*Honest disclosure of limitations strengthens scientific credibility.*
