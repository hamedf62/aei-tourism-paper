# Round 4 Citation-Compliance Review — subagent report + author verification & fixes (2026-08-27)

## Subagent verdicts (round 4)
1. Citation↔reference matching: FAIL — Dwivedi et al. (2023) cited but no entry; Athey (2017) & Kleinberg et al. (2015) listed but never cited; Buhalis & Leung year mismatch (2017 in text vs 2018 in refs).
2. APA 7 formatting: FAIL (minor) — Doğru before Duong (ordering); incomplete entries.
3. Bibliographic spot-checks: FAIL — 5 wrong entries; 1 likely fabricated (Filieri et al. 2022, DOI 404s in Crossref/OpenAlex/doi.org).
4. Anthropic citations: PASS (verified arXiv 2511.15080 authors; data documentation).

## Author verification (Crossref/OpenAlex, before applying)
- Dwivedi 2023 IJIM 71:102642 — CONFIRMED (Crossref).
- Filieri DOI 10.1007/s12525-022-00577-4 — CONFIRMED 404; real "state of the art" review = Nannelli et al. 2023. Substitute: Knani, Echchakoui & Ladhari (2022), IJHM 107, 103317 — CONFIRMED (Crossref).
- Acemoglu 2024: Economic Policy 40(121) — CONFIRMED (OpenAlex biblio).
- Brynjolfsson: Crossref print pub 2025-04-08 → QJE 140(2) is 2025 — CONFIRMED (OpenAlex "2024" = online-first year; cite print year 2025).
- Nannelli: EPS 31(7), 1325–1344 — CONFIRMED.
- Doğru et al.: now JHTR 49(2), 235–253, 30 authors, 2025 print — CONFIRMED.
- Duong et al.: Tourism Review 80(4), 813–827, 6 authors, parasocial-interaction subtitle, 2025 — CONFIRMED.
- Pham 2024 third author: Nguyen, G. K. H. — CONFIRMED via OpenAlex authorship.

## Fixes applied (all verified against Crossref/OpenAlex)
1. Dwivedi entry added (Pandey, Currie & Micu as co-authors per Crossref).
2. Filieri entry DELETED (fabricated DOI); §2.2 citation switched to Knani et al. (2022).
3. Acemoglu volume 39→40.
4. Brynjolfsson 2024→2025 in refs + both in-text cites.
5. Nannelli issue/pages corrected.
6. Buhalis & Leung in-text 2017→2018.
7. Doğru entry completed (2025, 49(2), 235–253, 6+ authors with et-al ellipsis).
8. Duong entry corrected (2025, 80(4), 6 authors, correct subtitle).
9. Pham third author corrected.
10. Çolak pages 919–939 added.
11. Alphabetical order restored (Doğru < Duong < Dwivedi… rechecked).
12. Uncited Athey & Kleinberg entries removed.

## Final state
25 reference entries; zero orphans; zero fabricated DOIs; script re-run PASS. Citation layer: READY.
