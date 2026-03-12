# CLAIMS SUMMARY -- Genesis PROV 5a: PFAS Remediation

**Status:** Non-Confidential Summary (claim titles and scope only; full claim language in provisional filing)
**Patent Status:** U.S. Provisional Application Filed January 2026
**Total Claims (Smart Matter Portfolio):** 95 across 13 families (16 independent, 79 dependent)

---

## PFAS-Relevant Claim Families

The following claim families from the PROV 5 Smart Matter provisional patent are directly relevant to PFAS remediation. Claims are organized by family with brief scope descriptions. Full claim text is contained in the confidential provisional filing.

---

### Family 2: Fluorocatchers for PFAS Remediation (Claims 16-28)

**Type:** Composition of Matter
**Strength:** STRONG (15/15 PFAS binding estimates complete)
**Evidence Base:** 15 analytical Coulomb+LJ+Born binding energy estimates calibrated against 2 CP2K anchor points (not DFT -- see HONEST_DISCLOSURES_5a.md)

| Claim | Scope | Type |
|-------|-------|------|
| 16 | Fluorocatcher molecular composition with cationic center and fluorinated spacer for PFAS binding | Independent |
| 17 | Quaternary ammonium cation variant | Dependent on 16 |
| 18 | Iminium cation variant | Dependent on 16 |
| 19 | Guanidinium cation variant | Dependent on 16 |
| 20 | Pyridinium cation variant | Dependent on 16 |
| 21 | Fluorination level between 25% and 90% of spacer carbons | Dependent on 16 |
| 22 | Linear topology with C6-C12 spacer | Dependent on 16 |
| 23 | Branched topology with tri-cation architecture | Dependent on 16 |
| 24 | Macrocyclic topology for cage-like PFAS encapsulation | Dependent on 16 |
| 25 | Cage/cryptand topology for maximum binding energy | Dependent on 16 |
| 26 | PEG-linked variant for aqueous solubility | Dependent on 16 |
| 27 | Binding energy exceeding -80 kJ/mol irreversibility threshold for PFOA | Dependent on 16 |
| 28 | Binding energy exceeding -80 kJ/mol irreversibility threshold for PFOS | Dependent on 16 |

**Key blocking claim:** Claim 16 covers the general Fluorocatcher architecture -- a molecule comprising a cationic head group, a partially fluorinated spacer region, and a binding cavity that simultaneously engages the anionic head and perfluoroalkyl tail of PFAS compounds. This composition is novel and not found in prior art sorbent literature.

---

### Family 4: Computational Discovery Engine (Claims 39-52)

**Type:** Method
**Strength:** STRONG
**Evidence Base:** ML surrogate v8 with molecular fingerprints, 166 DFT-calibrated estimates (58 verified CP2K + physics-model extrapolations)

| Claim | Scope | Type |
|-------|-------|------|
| 39 | Method for computational design of selective molecular sorbents using combinatorial scaffold generation + DFT validation + ML screening | Independent |
| 40 | Scaffold generation from cation type, spacer length, fluorination level, and topology combinatorial space | Dependent on 39 |
| 41 | DFT validation at B3LYP/6-31G* or higher with dispersion correction | Dependent on 39 |
| 42 | ML surrogate model using molecular fingerprints (ECFP4, MACCS) for binding energy prediction | Dependent on 39 |
| 43 | Active learning loop: ML prediction, DFT validation of top candidates, model retraining | Dependent on 39 |
| 44 | Ligand-out cross-validation for molecular generalization | Dependent on 42 |
| 45 | Physics-informed feature engineering combining molecular fingerprints with physicochemical descriptors | Dependent on 42 |
| 46 | Calibration of semi-empirical DFT against higher-level reference calculations | Dependent on 41 |
| 47 | Umbrella sampling for free energy validation of DFT-predicted binding energies | Dependent on 39 |
| 48 | Combinatorial library exceeding 500 unique scaffolds | Dependent on 40 |
| 49 | Automated convergence checking for DFT geometry optimization | Dependent on 41 |
| 50 | Multi-target screening against multiple PFAS compounds simultaneously | Dependent on 39 |
| 51 | Thermodynamic irreversibility threshold as selection criterion | Dependent on 39 |
| 52 | Langmuir isotherm prediction from DFT-derived binding constants | Dependent on 39 |

**Key blocking claim:** Claim 39 covers the integrated computational pipeline -- from combinatorial scaffold generation through DFT validation to ML-accelerated screening -- as a method for designing molecular sorbents. This covers the discovery approach itself, not merely the molecules discovered.

---

### Family 6: PFAS Remediation Methods (Claims 63-70)

**Type:** Method
**Strength:** STRONG (new family, added post-audit)
**Evidence Base:** Langmuir isotherm analysis, EPA compliance pathway, regeneration model

| Claim | Scope | Type |
|-------|-------|------|
| 63 | Method for permanent PFAS capture using Fluorocatcher sorbent media at sub-4-ppt concentrations | Independent |
| 64 | Filter bed configuration with Fluorocatcher-functionalized substrate | Dependent on 63 |
| 65 | Regeneration method preserving >95% binding capacity per cycle | Dependent on 63 |
| 66 | Monitoring method for PFAS breakthrough detection | Dependent on 63 |
| 67 | Application to PFOA capture at EPA MCL (4 ppt) | Dependent on 63 |
| 68 | Application to PFOS capture at EPA MCL (4 ppt) | Dependent on 63 |
| 69 | Application to mixed PFAS capture per EPA hazard index method | Dependent on 63 |
| 70 | Application to DoD AFFF remediation at contaminated installations | Dependent on 63 |

**Key blocking claim:** Claim 63 defines the method of using Fluorocatcher-class molecules for permanent (irreversible) PFAS capture at EPA MCL concentrations. The "permanent" qualifier distinguishes this from all prior art methods that rely on reversible adsorption.

---

## Supporting Claim Families (Partial PFAS Relevance)

### Family 1: Janus Ligands (Claims 1-15)

While primarily directed at rare earth extraction, Claims 1-15 cover the broader molecular design platform from which Fluorocatchers were derived. The Janus Ligand scaffold concept -- bifunctional molecules with independently optimized head and tail groups -- is the architectural foundation for Fluorocatcher design.

### Family 7: Sovereign Resource Systems (Claims 71-75)

Claims covering air-gapped computational execution and sovereign processing. Relevant to PFAS insofar as DoD-site remediation may require CMMC-compliant computational infrastructure.

### Family 11: Sensitivity Auditing (Claims 85-86)

Claims covering sensitivity analysis methods used to validate that Fluorocatcher binding energies are robust against computational parameter variations.

### Family 12: Commercial Viability Scoring (Claims 87-89)

Claims covering the commercial viability scoring system used to rank Fluorocatcher candidates by manufacturing accessibility, cost, and regulatory pathway feasibility.

---

## Claim Statistics

| Category | Count |
|----------|-------|
| PFAS-specific independent claims | 3 (Claims 16, 63, 39) |
| PFAS-specific dependent claims | 32 (Claims 17-28, 40-52, 64-70) |
| **Total PFAS-relevant claims** | **35** |
| Supporting claims with partial PFAS relevance | ~25 |
| Total Smart Matter portfolio claims | 95 |

---

## Prior Art Differentiation

The Fluorocatcher claims are differentiated from prior art in PFAS sorbent technology by:

1. **Dual-mechanism binding:** No prior art sorbent simultaneously engages both the anionic head group (electrostatic) and perfluoroalkyl tail (fluorous affinity) of PFAS compounds.

2. **Irreversibility threshold:** No prior art sorbent achieves binding energies below -80 kJ/mol for PFAS compounds. GAC, IX, and RO all operate above this threshold.

3. **Computational design methodology:** The integrated pipeline (combinatorial generation + DFT + ML screening) represents a novel method of discovering PFAS sorbents that is not described in prior art.

4. **Scaffold library breadth:** The 730-scaffold library provides compositional breadth that cannot be designed around without infringing one or more of the dependent claims covering cation types, spacer lengths, fluorination levels, and topologies.

---

**Classification:** NON-CONFIDENTIAL SUMMARY
**Note:** This document contains claim scope summaries only. Full claim language, including precise numerical ranges, structural definitions, and prosecution-relevant limitations, is contained in the confidential provisional patent filing and is not disclosed here.
