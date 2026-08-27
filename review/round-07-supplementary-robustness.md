# Review Round 7 — Supplementary Robustness (executed, 2026-08-27)

New checks (code/13, results/robustness_b4_supplementary.csv):

| Check | β (log GDP) | t | n | Reading |
|---|---|---|---|---|
| Winsorized 1% | −0.103 | −4.9 | 113 | Gradient not outlier-driven |
| Food Prep only | **+0.060** | +6.9 | 77 | **Reverses** — rich countries have MORE Food Prep share |
| Personal Care only | −0.093 | −5.0 | 113 | Gradient lives here |
| Population-weighted | −0.017 | −0.6 | 113 | **Dies** when weighting by population |
| Excl. pop < 500k | −0.108 | −4.7 | 113 | Not micro-state driven |
| + working-age control | −0.102 | −3.8 | 113 | Not demographic share driven |

## Interpretation (must reach the paper)
The negative income gradient is NOT robust to population weighting and is component-specific: it comes entirely from Personal Care (n=113), while Food Prep alone flips positive (n=77, published for fewer/richer-set countries). This strengthens the paper's §4.3/§4.5 honesty but undermines any strong cross-country claim. The paper's defensible core: (a) the level–share decomposition, (b) the front-line human-only finding, (c) the monitoring framework. The gradient should be presented as "suggestive, composition- and sample-dependent".

**Fixes applied (§4.5 + §5.2 update):** add supplementary checks with component-wise and population-weighted results; recast gradient as suggestive. → round 8 rewrite.
