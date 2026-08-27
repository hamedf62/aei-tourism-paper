# Review Round 3 — Citation Compliance (author-executed, 2026-08-27)

Method: script check (in-text author tokens vs reference list) + targeted OpenAlex verification (executed during data collection; see session records).

## Findings

1. **MINOR — metadata flag (§References)**: Noll et al. (2025) has no DOI/URL. Fix: add institutional URL (UNLV "Digital Scholarship") to the entry. → APPLIED in round 4.
2. **MINOR**: In-text "Acemoglu & Restrepo (2019)" / "Ivanov & Webster (2019)" use "&" inside parens — correct APA for parenthetical citation. No change needed.
3. **PASS**: All 25 reference entries have DOIs except Noll et al. (working paper — acceptable) and WEF/WTTC web sources (cited as WTTC 2025, World Bank 2025 — both have URLs). Zero citation orphans detected by script (remaining "tokens without ref entry" are acronyms/table text, not citations — manually verified).
4. **PASS**: Years/journals spot-checked against OpenAlex during literature verification: Acemoglu 2024 Economic Policy ✓; Brynjolfsson et al. 2024 QJE ✓; Felten et al. 2021 SMJ ✓; Tussyadiah 2020 ATR ✓; Eloundou et al. 2023 arXiv ✓; Gretzel et al. 2015 Electronic Markets ✓; Buhalis & Leung IJHM ✓ (published online 2017, issue 2018 — entry says 2018, vol 71: correct); Ivanov & Webster 2019 Emerald book DOI ✓; Doğru et al. 2023 JHTR ✓; Kleinberg et al. 2015 AER ✓; Athey 2017 Science ✓.
5. **MAJOR — fixed in round 2**: novelty log file was missing → created `review/novelty_search_log.md`; count updated 6→12 works.
6. **MINOR**: Anthropic (2026) citation should note it covers both the report and data documentation. Entry already lists Hugging Face location + June 26 date — acceptable. No change.
7. **MINOR — AI-assistance disclosure**: matches journal norms (acknowledge, human verification). No change.

## Verdict after fixes: citation layer ready; one metadata patch to apply (Noll URL).
