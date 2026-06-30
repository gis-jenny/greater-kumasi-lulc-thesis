# Thesis Status — Last Updated: June 29, 2026

## 🔴 Currently Working On

- **Ch. 4 (Results & Discussion)** and **Ch. 5 (Conclusions & Recommendations)** — Chapters 1–3 are now structurally complete; the manuscript is ready to advance into Results.
- Filling missing citations for in-text references introduced during the audit rewrite (see Open Issues).

## ✅ Completed Sections

- [x] Chapter 1: Introduction (1.1 Background → 1.8 Structure) — reorganized and expanded
- [x] Chapter 2: Literature Review (2.1 → 2.11) — restructured with Buffer Zone, UHI/Flooding, Garden City, and Research Gap sections added
- [x] Chapter 3: Study Area & Methodology (3.1 → 3.7 with 3.2.1–3.2.3) — rewritten and renumbered
- [ ] Chapter 4: Results & Analysis
- [ ] Chapter 5: Conclusions & Recommendations

## 🔁 Recent Changes (Last 3 Sessions)

- **[2026-06-29] Audit-driven rewrite pass on Ch. 1–3:**
  - Removed off-topic material (school infrastructure paragraph, Pearl River Delta example, dams digression).
  - Updated title to road-infrastructure scope: "Assessing the impact of road infrastructure development on LULC change in Greater Kumasi using remote sensing and GIS."
  - Reorganized Ch. 1 to 1.1–1.8 (removed Prior Works, added Significance, Scope and Limitations, and Structure sections).
  - Restructured Ch. 2 with new sections 2.8 (Buffer Zone Analysis), 2.9 (Urban Heat Island & Flooding), 2.10 (Garden City history), 2.11 (Research Gap).
  - Rewrote Ch. 3 with proper 3.1 → 3.7 numbering and nested subsections 3.2.1–3.2.3.
  - Filled empty §3.7 Accuracy Assessment with full methodology (Olofsson et al. 2014 protocol, ~250 stratified random points, OA ≥ 85% / Kappa ≥ 0.80 thresholds, bias-adjusted areas).
  - Resolved LULC class scheme inconsistency: now uses **Forest, Settlement, Water, Farmland** throughout. Grep confirms zero remaining 5-class terms (`built-up`, `bare land`).
  - Fixed bug in rewrite script where old Ch. 3 body was not being deleted (Phase F deletion block now uses element-walk on live predicates; 110 orphan paragraphs removed on last run).
- [2026-06-29] Created memory entries: `doc-file-location.md`, `lulc-classes.md`.
- [2025-06-24] Initialized project memory system and CLAUDE.md.
- [2025-06-24] Confirmed tools, software, institution — all open issues resolved.

## 🔍 Gaps Found in the Methodology (Ch. 3) — to resolve

1. **Reference data sources and citation completeness** — the new §3.2 cites Olofsson et al. (2014), Anderson (1976), Seto et al. (2012), Akinbode et al. (2016), Stenhoff (2018), Douglas et al. (2008), Oteng-Ababio (2010), Abiodun (2017), Yiran & Ablo (2019), Owusu (2015), Ghana Statistical Service (2021). Most still need full APA 7 entries inserted into a References list.
2. **Software versions not documented** — QGIS version, SCP plugin version, and the Python environment for statistics are not specified in §3.3–§3.6.
3. **Sample size justification** — the "minimum of 50 training pixels per class" in §3.4.2 is a rule of thumb; brief justification or a citation (e.g., Congalton & Green) would strengthen it.
4. **Buffer stratification rationale** — §3.6 adopts four rings (0–500 m, 500 m–1 km, 1–2 km, 2–5 km) without citing the source for these widths; the 500 m threshold is common in corridor studies but should be referenced.
5. **Statistical test detail** — the chi-square test mentioned in §3.6 for "LULC composition differs between inner ring (0–1 km) and outer ring (2–5 km)" needs a stated null hypothesis and degrees of freedom convention.
6. **No figure/table placeholders for Chapter 3** — references to Table 3.1 (data sources), Table 3.2 (class definitions), Figure 3.1 (locator map), and Figure 3.2 (road network) exist in the text but no actual tables/figures are inserted in the document yet.
7. **Inter-rater reliability for GCPs** — §3.7 says GCPs were used but does not state who labelled them or whether inter-rater reliability was assessed.
8. **`According to ,` citation blanks** — at least one remaining citation blank in Ch. 2 (the "concept of sustainable development" attribution) still needs an author and year.

## ⚠️ Open Issues / Decisions Pending

- **References list** — populate with full APA 7 entries for every in-text citation in Ch. 1–3 (currently the doc ends with a bare "References" heading and no entries).
- **Citations introduced during rewrite** — confirm or replace the following: Seto et al. (2012), Akinbode et al. (2016), Stenhoff (2018), Douglas et al. (2008), Oteng-Ababio (2010), Abiodun (2017), Yiran & Ablo (2019), Owusu (2015).
- **Confirm supervisor name** (still missing in CLAUDE.md).
- **Sentinel-2** — CLAUDE.md lists as "possibly"; confirm excluded or supplementary before Ch. 3 freeze.
- **Tables/Figures for Ch. 3** — produce Table 3.1, Table 3.2, Figure 3.1 (locator map), Figure 3.2 (road network) and embed in docx.
- **LULC class scheme now finalized as 4 classes** (Forest / Settlement / Water / Farmland) per user decision 2026-06-29. Update memory and CHAPTER_MAP §3.4 to match.

## 📌 Where to Resume Next Session

1. Populate the References list with full APA 7 entries for all in-text citations in Ch. 1–3.
2. Resolve the eight methodology gaps listed above (especially figures/tables for Ch. 3 and the chi-square test detail).
3. Begin drafting Ch. 4 (Results & Discussion):
   - Per-epoch class area table (Forest, Settlement, Water, Farmland × 1995, mid-decade, 2024).
   - Transition matrix for each epoch pair.
   - Buffer-stratified LULC composition and per-ring percentage change.
   - Chi-square test result for corridor effect.
   - Accuracy assessment results (OA, Kappa per epoch).
4. Verify the empty `According to ,` blank has been resolved (audit run shows it as fixed in 1 paragraph; spot-check).

## 🗓️ Deadline Countdown

- **Submission**: July 31st, 2025
- ⚠️ **Note**: The deadline date in CLAUDE.md predates today (2026-06-29) — confirm with supervisor whether the submission date has been pushed, or whether this should be interpreted as the originally planned deadline that has already passed. Update CLAUDE.md accordingly.

## ✅ Confirmed Project Details

- **Institution**: Kwame Nkrumah University of Science and Technology (KNUST)
- **Degree**: MPhil Geographic Information System
- **GIS Software**: QGIS ✓ (version to be documented in §3.3)
- **Classification Method**: Maximum Likelihood ✓
- **Statistical Analysis**: Python ✓
- **Remote Sensing**: Landsat (primary) — Sentinel-2 TBC ✓
- **Accuracy Assessment**: Kappa coefficient + Overall Accuracy, ≥ 85% / ≥ 0.80 thresholds ✓
- **Citation Style**: APA 7th edition ✓
- **Study Period**: 1995–2024 ✓
- **LULC Classes (final)**: Forest, Settlement, Water, Farmland ✓
- **Title (final)**: "Assessing the impact of road infrastructure development on LULC change in Greater Kumasi using remote sensing and GIS" ✓
- **Scope (final)**: Road infrastructure only (airport, Boankra, Kejetia noted for context, not analysed) ✓
- **Ch. 4 / Ch. 5 split (final)**: Kept merged — single "Results and Discussion" chapter ✓

## 📁 Key Files in Project Root

- `thesis.docx` — current manuscript (242 paragraphs)
- `thesis.docx.bak` — pre-rewrite backup
- `rewrite_thesis.py` — master rewrite script (Phases A–J, currently passing all checks)
- `extract_thesis.py` — paragraph extractor for verification
- `thesis_extracted.txt` — last extraction
- `CHAPTER_MAP.md` — chapter outlines and argument structure
- `DECISIONS.md` — rationale for methodological and writing choices
- `SOURCES.md` — citation registry (to be populated)
- `CLAUDE.md` — project instructions
- `CLAUDE.local.md` — personal workflow preferences