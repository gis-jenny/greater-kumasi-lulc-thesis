# Assessing the Impact of Road Infrastructure Development on Land Use and Land Cover (LULC) Change in Greater Kumasi

A remote sensing and GIS-based thesis examining how transport corridors have reshaped the landscape of Greater Kumasi over the 1995–2024 period.

## Overview

Road networks are reshaping Greater Kumasi as the primary driver of landscape transformation. This study uses multi-temporal Landsat satellite imagery to compare land cover across decades, classifying terrain into **forests, settlements, water bodies, and farmlands/agricultural land**. Change detection techniques pinpoint how much natural greenery has been converted by urban expansion, while buffer zone analysis around major highways reveals how development intensity varies with distance from transport corridors.

**Core narrative**: Buildings and businesses aggressively cluster along new transport corridors → forests are fragmented → Kumasi loses its "Garden City" status → impervious surfaces trap heat (Urban Heat Island effect) → loss of wetlands worsens seasonal flash flooding.

## Research Objectives

1. Map and quantify the spatial-temporal dynamics of LULC changes in Greater Kumasi over **1995–2024**.
2. Evaluate how proximity to major transport corridors accelerates the loss of agricultural livelihoods and ecological zones.

## Study Area

**Greater Kumasi** — the metropolitan area of Kumasi in the Ashanti Region of Ghana.

## Methodology

- **Imagery**: Landsat (primary), possibly Sentinel-2
- **GIS Software**: QGIS
- **Classification**: Maximum Likelihood
- **Accuracy Assessment**: Kappa coefficient, Overall Accuracy
- **Statistical Analysis**: Python
- **Spatial Analysis**: Buffer zone analysis around transport corridors; multi-temporal change detection

## LULC Classes

| Class | Description |
|---|---|
| Forest | Natural and semi-natural tree cover |
| Settlement | Built-up / impervious surfaces |
| Water bodies | Rivers, lakes, wetlands |
| Farmland | Agricultural land |

## Tools & Software

- **Remote Sensing**: Landsat (primary), possibly Sentinel-2
- **GIS Software**: QGIS
- **Classification method**: Maximum Likelihood
- **Accuracy assessment**: Kappa coefficient, Overall Accuracy
- **Statistical analysis**: Python

## Key Concepts

- **LULC** — Land Use and Land Cover
- **Transport corridors** — major road networks/highways
- **Buffer zone analysis** — spatial method for proximity-based assessment
- **Urban Heat Island (UHI)** — heat effect from impervious surface expansion
- **Fragmentation** — forest/habitat breakup
- **Garden City** — Kumasi's historical identity

## Repository Structure

```
.
├── README.md            # This file
├── CLAUDE.md            # Project instructions for AI assistants
├── CHAPTER_MAP.md       # Chapter outlines and argument flow
├── DECISIONS.md         # Rationale for key methodological and writing choices
├── ch1_CLAUDE.md        # Chapter 1 guidance
├── thesis.docx          # Thesis manuscript
└── Claude/
    └── files.zip        # Auxiliary files
```

## Citation Style

APA 7th edition.

## Academic Details

- **Degree**: MPhil Geographic Information System
- **Institution**: Kwame Nkrumah University of Science and Technology
- **Supervisor**: [Supervisor Name]
- **Submission Deadline**: July 31st, 2025

---

*This repository accompanies the MPhil thesis submitted to the Department of Geomatic Engineering, KNUST.*