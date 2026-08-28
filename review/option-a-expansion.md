# Option A Expansion — Final Verification (2026-08-28)

## New empirical content (code 21-25, results panel2_*)
1. **3-period panel built** (Aug 2025 weekly + Apr/May 2026 monthly; intermediate releases have no SOC facet — documented in §3.1).
2. **Growth**: 0.25% → 0.84% mean among 12 balanced-panel countries (3.4× in 9 months).
3. **β-convergence**: −0.57 (t=−6.6); LOO range β∈[−0.61,−0.37], t∈[−7.5,−2.9]; driven by Personal Care (−0.95, t=−8.9).
4. **Rank stability**: Spearman ρ=0.87 (Aug 2025 vs May 2026).
5. **Gradient reversal**: +0.09 (t=3.2, n=12, Aug 2025) → +0.01 (t=1.5, n=64, Apr 2026) → −0.01 (t=−1.0, n=77, May 2026). Early adopters richer (log GDP 10.25 vs 9.53) and heavier users (index 2.77 vs 1.57).
6. **Decomposition**: mean rise 0.59pp = within-country growth; entry effect on level only.

## Manuscript changes
- Abstract rewritten (3 snapshots, tripled-in-9-months headline, gradient-reversal).
- §2.4: predictions P1–P5 added (framework → tests mapping).
- §3.1: release-history/schema-harmonization note.
- §4.6: full dynamics section (growth, convergence, reversal, decomposition, 3 implications).
- §5.2: limitation 6 rewritten (panel brevity, scale-invariance).
- §5.3, §6: updated with dynamics findings.
- Table 5 (9 statistics), Figures 5–7, Appendix B extended to B5.
- Word count: 5,124 main text / 7,908 total (script-verified).

## Internal consistency spot-checks
- Table 5 values match panel2_*.csv: VERIFIED
- §4.6 numbers match code outputs: VERIFIED
- Figures 5-7 rendered, vision-checked: PASS (minor axis-note on fig5 spacing—categorical waves; acceptable)

## Verdict
Expanded paper addresses the three structural critiques (no dynamics, no mechanism test, no "so-what"): 
- dynamics → 3-period panel + convergence
- mechanism → gradient reversal = adoption-composition test (P1/P2 confirmed)
- so-what → fastest-growing slice + monitoring implications

Submission-ready at full Q1 length.
