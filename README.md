# AI in Tourism Work: Behavioral Evidence from the Anthropic Economic Index

**Repo for the manuscript:** "AI in Tourism Work: Behavioral Evidence from the Anthropic Economic Index and Its Economic Correlates" (target: *Tourism Economics*).

## Structure

```
code/        01_build_panel.py   — AEI + World Bank data assembly
             02_analysis.py      — correlations, OLS, figures 1-4
             03_fix_figures.py   — figure polish
data/processed/  panel.csv + AEI/WB extracts (reproducible)
figures/     fig1-fig4 (300 DPI PNG)
manuscript/  manuscript.md (+ submission files)
results/     all tables as CSV
review/      10 review rounds (reports + revision log)
```

## Data

- **Anthropic Economic Index**, release 2026-06-26 (`aei_claude_ai_2026-06-26.csv`), Hugging Face `Anthropic/EconomicIndex`, CC-BY-4.0. Download via:
  `curl -L https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_06_26/data/aei_claude_ai_2026-06-26.csv -o data/raw/`
- **World Bank WDI** via API (2019–2024, latest available per country).
- Raw AEI file (~220 MB) is not committed; `code/01_build_panel.py` rebuilds everything from it.

## Reproduce

```bash
python3 code/01_build_panel.py
python3 code/02_analysis.py
python3 code/03_fix_figures.py
```

Requires: `pandas`, `numpy`, `matplotlib`.

## Key findings (preview)

- Tourism-occupation AI usage (SOC major groups: Food Prep & Serving, Personal Care) is a small slice of Claude work conversations (~1–2% per group) but is measurable and varies ~4× across countries.
- It correlates **negatively** with GDP per capita (r ≈ −0.30), overall Claude usage intensity (r ≈ −0.36), and services employment — and **positively** with travel services share of exports (r ≈ +0.17).
- Tourism groups sit at a distinct automation/augmentation profile (Food Prep ≈ balanced; Arts/Media augmentation-heavy).

## License & attribution

AEI data © Anthropic, CC-BY-4.0; not endorsed by Anthropic. Code and manuscript in this repo: MIT.
