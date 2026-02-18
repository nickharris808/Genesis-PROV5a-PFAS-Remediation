# Solver Overview -- Genesis PROV 5a: PFAS Remediation

**Classification:** NON-CONFIDENTIAL
**Purpose:** Explain the computational methods used to generate PFAS Fluorocatcher results, without disclosing solver source code or patent-protected algorithms.

---

## Density Functional Theory (DFT) Method

All binding energies in this repository were computed using density functional theory at the following level:

| Parameter | Value |
|-----------|-------|
| Functional | B3LYP (Becke 3-parameter, Lee-Yang-Parr hybrid) |
| Basis set | 6-31G* (Pople split-valence with d-polarization on heavy atoms) |
| Dispersion | D3(BJ) -- Grimme D3 with Becke-Johnson damping |
| Solvation | CPCM (conductor-like polarizable continuum model, water, epsilon=78.4) |
| Grid | UltraFine (99,590) for DFT numerical integration |

### Why This Level of Theory

**B3LYP** is the most widely-used hybrid DFT functional in organic chemistry. It provides a good balance between accuracy and computational cost for non-covalent interactions in molecular complexes.

**D3(BJ) dispersion correction** is essential for this application. Fluorine-fluorine van der Waals interactions between the PFAS perfluoroalkyl tail and the Fluorocatcher fluorinated cavity contribute a substantial fraction of the total binding energy. Without the D3 correction, DFT would systematically underestimate these interactions.

**CPCM implicit solvation** models the aqueous environment as a dielectric continuum. This captures the bulk electrostatic screening effect of water but does not model explicit hydrogen bonds at the binding interface. This is a known limitation (see HONEST_DISCLOSURES.md).

**6-31G*** is a medium-sized Pople basis set adequate for screening purposes. Larger basis sets (cc-pVTZ, aug-cc-pVDZ) would reduce basis set superposition error but at significantly higher computational cost.

---

## Binding Energy Definition

The binding energy is defined as:

```
dE_bind = E(complex) - E(fluorocatcher, isolated) - E(PFAS, isolated)
```

where all three energies are computed in implicit aqueous solvent. A more negative binding energy indicates stronger binding.

Key thermodynamic thresholds:

| Threshold | Value | Significance |
|-----------|-------|-------------|
| GAC baseline | -45 kJ/mol | Activated carbon binding (literature consensus) |
| IX resin baseline | -50 kJ/mol | Ion exchange resin binding (literature) |
| **Irreversibility threshold** | **-80 kJ/mol** | Below this, desorption is kinetically negligible at 298 K |

---

## Calibration Methodology

Raw B3LYP/6-31G* binding energies were calibrated against two higher-level reference calculations performed with CP2K using the PBE functional and DZVP-MOLOPT basis set:

| Anchor | Candidate | Calibrated Binding (kJ/mol) |
|--------|-----------|----------------------------|
| PFAS_Capture_000 | FC-001 (Bis-TMA-C8 baseline) | -97.0 |
| PFAS_Capture_001 | FC-003 (Bis-TMA-C8-F8) | -121.0 |

A linear correction was applied:

```
dE_corrected = a * dE_raw + b
```

where `a` and `b` are fit to reproduce the two CP2K anchor values exactly. This calibration improves absolute accuracy for molecules with architectures similar to the anchors. It is based on only 2 points, which is a known limitation.

---

## Binding Energy Components

The total binding energy arises from four physical contributions:

1. **Coulombic attraction** -- Electrostatic interaction between the cationic center(s) of the Fluorocatcher and the anionic head group of PFAS (carboxylate for PFOA, sulfonate for PFOS). This is the dominant contribution for most candidates.

2. **Fluorophilic van der Waals** -- Favorable F...F contacts between the perfluoroalkyl tail of PFAS and the fluorinated spacer region of the Fluorocatcher. Optimal F...F distance: 2.94 Angstrom (2x fluorine van der Waals radius of 1.47 Angstrom). Parameterized from OPLS-AA Lennard-Jones parameters.

3. **Dehydration penalty** -- Partial loss of the solvation shell around the cationic centers upon PFAS approach. Estimated from the Born model for ionic desolvation. This is a positive (unfavorable) contribution that partially offsets the electrostatic attraction.

4. **London dispersion** -- Long-range dispersion interaction between PFAS and the Fluorocatcher cavity, captured by the D3(BJ) empirical correction. Scales approximately with total molecular weight of the complex.

---

## Computational Pipeline

The discovery pipeline operates in three stages:

### Stage 1: Scaffold Generation

Combinatorial enumeration of molecular architectures from:
- 4 cation types: quaternary ammonium, iminium, guanidinium, pyridinium
- Spacer lengths: C6, C8, C10, C12
- Fluorination levels: 0%, 25%, 33%, 50%, 67%, 75%, 90%
- Topologies: linear, branched, macrocyclic, cage, PEG-linked

This produces the 730-scaffold Fluorocatcher library.

### Stage 2: DFT Validation

High-priority candidates undergo full DFT geometry optimization and binding energy calculation at B3LYP/6-31G*/D3(BJ)/CPCM. Each calculation requires several hours of compute time. 15 candidates have been validated to date, representing all major architectural families.

### Stage 3: ML Surrogate Screening

A machine learning surrogate model (trained on DFT results) enables rapid pre-screening of the full library. The surrogate uses molecular fingerprints (ECFP4 + MACCS keys) and physicochemical descriptors as features, with binding energy as the target variable. Candidates predicted to exceed the irreversibility threshold are prioritized for full DFT validation.

---

## Umbrella Sampling (Free Energy Profiles)

For selected Fluorocatcher-PFAS complexes, potential of mean force (PMF) calculations were performed using umbrella sampling molecular dynamics:

- **Simulation length:** 10 ns per umbrella window (publication standard)
- **Method:** Weighted Histogram Analysis Method (WHAM)
- **Reference:** Roux & Berneche, Biophysical Journal 82, 1681-1684 (2002)

The PMF confirms that:
- The binding well depth is consistent with DFT-predicted energies
- The kinetic barrier to desorption exceeds 25 kT at 298 K
- The binding is effectively irreversible on engineering timescales

---

## What Is NOT Disclosed

The following are protected by patent and are not included in this repository:

- Solver source code for DFT calculations
- ML surrogate model weights and training code
- Scaffold generation algorithm implementation
- Internal optimization parameters and convergence criteria
- Raw Gaussian/CP2K output files

Only validated results and published equations are disclosed here.

---

**Classification:** NON-CONFIDENTIAL
