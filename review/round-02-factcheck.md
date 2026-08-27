# Review Round 1 — Fact-Checking (subagent, 2026-08-27)

**Verdict: FAIL on robustness section; PASS on empirical core.**

## CRITICAL
1. §4.5 robustness claims contradict CSVs (B1: −0.006/+0.154/−0.517 not "−0.08..−0.19"; B2: β=−0.085, t=−4.94 not "−0.10, −3.6"; B3: r(May,Apr)=0.62, β_Apr=−0.075 — "±0.02" claim false).
2. §4.4/Abstract: "autonomy below global average ~3.3" — actual global mean 2.74; tourism occs at/above average. Invert or delete.

## MAJOR
3. Abstract/§3.3 denominator: measure is share of ALL conversations, not work conversations only (country SOC shares uncorrelated with work share; mean work share ≈41%). Relabel everywhere.
4. §4.1 Sales and Related = 9.14% (May), not 8.7%.
5. Table 1 dashes: raw AEI publishes full metrics for all 7 dashed rows (extraction gap in 04_detail_profiles.py); "twelve largest" framing wrong.
6. §2.3/App A: OpenAlex AEI title search now returns 12 works (not 6); novelty still holds. review/novelty_search_log.md missing — must add.
7. §4.2: receipts CI [−0.27,−0.03] excludes zero — "not significant" wrong for receipts.

## MINOR
8. "about 1% or less" — Personal Care global 1.23%.
9. Autonomy range endpoint 3.03 not 3.0.
10. Abstract rounding 0.7–2.9 → state 0.66–2.87.
11. Table 2 labels arrivals/receipts "(log)" but CSV computed on levels (−0.141/−0.118; log versions −0.205/−0.266). Relabel or recompute.
12. Word count "~7,500" unverified.

## Verified correct (spot-checks 1–20)
Headline stats, T1–T4 values, correlations, regressions, country examples, n's — all match CSVs exactly.

## Decision (author)
- Recompute Table 2 arrivals/receipts rows on logs (matches text labels) — do it, cleaner.
- Fill Table 1 dashes from raw; fix "twelve largest" wording.
- Rewrite §4.5 honestly; add composition-sensitivity of B1 (Sales flip).
- Fix autonomy benchmark; Sales 9.14%; receipts wording; Personal Care 1.23%.
- Add novelty log; update count to 12 works.
- Abstract: relabel denominator; use 0.66–2.87.
