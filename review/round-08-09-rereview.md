# Review Rounds 8–9 — Re-Review (verification) & Final Number Audit (executed, 2026-08-27)

## Round 8: verification that claimed fixes landed (grep-checked in manuscript.md)

| # | Round-2/4 finding | Claimed fix | Verified? |
|---|---|---|---|
| 1 | §4.5 robustness contradictions | Rewritten with true B1/B2/B3 numbers | ✅ text matches robustness CSVs |
| 2 | Autonomy benchmark inversion | Now "spanning the global mean of 2.74", percentiles given | ✅ |
| 3 | Work-conversation denominator | Abstract/intro now say "Claude conversations" | ✅ |
| 4 | Sales 8.7% | Now 9.1% | ✅ |
| 5 | Personal Care "≤1%" | Now 1.2% | ✅ |
| 6 | Receipts "not significant" | Now "marginally significant, CI excludes 0"; arrivals separate | ✅ |
| 7 | Table 1 dashes | All 19 rows fully populated from raw AEI | ✅ |
| 8 | "twelve largest" | Removed; "full task-level metrics for each" | ✅ |
| 9 | Novelty count 6→12 + log | Updated; review/novelty_search_log.md exists | ✅ |
| 10 | Table 2 log labels | Arrivals/receipts rows now log values (−0.21/−0.27) matching labels | ✅ |
| 11 | Causal policy language | §5.3 recast as monitoring-not-prescription | ✅ |
| 12 | User-base composition rival | Named in §4.3 as observationally equivalent; limitation cross-ref | ✅ |
| 13 | Gradient component-specificity | §4.5 + abstract now "suggestive", component/weighting caveats | ✅ |
| 14 | Short-form terminology | Defined in §3.3 | ✅ |
| 15 | Abstract length | ~250 words | ✅ |

No regressions found. One new check: contribution paragraph updated to frame robustness honesty as a contribution — consistent with §4.5. ✅

## Round 9: final number audit (script 05 + manual)

- All Table 1–4 values re-verified against CSVs after edits: MATCH
- Abstract numbers (0.66/2.87/1.05/−0.30/−0.36/+0.17): MATCH
- §4.5 numbers (−0.01/+0.15/−0.52/−0.085/−4.9/0.62/−0.075/+0.40): MATCH robustness CSVs
- §4.4 percentiles (94/94/92/84/23/33/90/2): MATCH code/10 output
- No orphan citations (script); 25 refs, all with DOI or working-paper URL
- Word count main text (script-measured): ~3,600 words body + abstract; total file ~6,200 incl. tables/references — the title-page "~7,500" line replaced with accurate count

**Final verdict: manuscript internally consistent, honestly qualified, submission-ready.**
