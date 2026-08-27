# Review Round 4 — Citation-Compliance Reviewer

Manuscript: `manuscript/manuscript.md` | Reviewer: citation-compliance (round 4)
Verification: DOI resolution via Crossref/OpenAlex/doi.org APIs + web search (Aug 2026).

## Overall verdict

| Task | Verdict |
|---|---|
| 1. Citation ↔ reference matching | **FAIL** — 1 cited-but-unlisted work; 2 uncited references; 1 year mismatch |
| 2. APA 7 formatting | **FAIL (minor)** — alphabetical-order error; assorted minor issues |
| 3. Bibliographic plausibility spot-checks | **FAIL** — 5 entries with wrong metadata; 1 likely fabricated entry |
| 4. [AN]-related citation attribution | **PASS** — Anthropic (2026) corporate-author form defensible for data citation; Appel et al. matches arXiv order of record (note on Anthropic-site variant) |

## Task 1 — Citation ↔ reference matching

**Cited in text but missing from References:**

1. **Dwivedi et al. (2023)** — cited in §1 Introduction (lit-review sentence). No entry exists. Fix: add —
   `Dwivedi, Y. K., Kshetri, N., Hughes, L., Slade, E. L., Jeyaraj, A., Kar, A. K., … Wright, R. (2023). Opinion paper: "So what if ChatGPT wrote it?" Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. *International Journal of Information Management, 71*, 102642. https://doi.org/10.1016/j.ijinfomgt.2023.102642`
   (Verified: Crossref.)

**In References but never cited in text (delete or cite):**

2. **Athey (2017)** — no in-text occurrence anywhere. Recommend deleting from References (or cite in §2.1).
3. **Kleinberg et al. (2015)** — no in-text occurrence anywhere. Recommend deleting (or cite in §2.1 alongside exposure/prediction-policy literature).

**Year mismatch between citation and reference:**

4. **Buhalis and Leung** cited as **(2017)** in §2.2, but reference is dated **2018** (correct — IJHM Vol. 71 is April 2018). Fix: change in-text citation to (2018). Note APA 7 also wants the narrative form "Buhalis and Leung (2018)" — current form is fine once the year is fixed.

All other in-text citations match reference entries. WTTC abbreviation form "(World Travel & Tourism Council [WTTC], 2025)" is correct APA 7 for first use; subsequent use would be (WTTC, 2025) — WTTC is not cited again, so no issue.

## Task 2 — APA 7 formatting

5. **Alphabetical order error (MUST FIX):** Doğru, T., … is listed **before** Duong, C. D. — wrong. APA alphabetizes letter-by-letter; "Dog..." < "Duong..." so Duong must come first. Fix: swap the two entries (Duong first, then Doğru). Everything else is correctly ordered.

6. **Doğru et al. (2023) — incomplete entry (MUST FIX):** No volume/issue/pages. Article is now published: *Journal of Hospitality & Tourism Research, 49*(2), 235–253. Fix to:
   `Doğru, T., Line, N., Mody, M., Hanks, L., Abbott, J., & Açikgöz, F. (2023). Generative artificial intelligence in the hospitality and tourism industry: Developing a framework for future research. *Journal of Hospitality & Tourism Research, 49*(2), 235–253. https://doi.org/10.1177/10963480231188663`
   (Note: Crossref lists 6 authors — Abbott and Açikgöz are missing from the manuscript's author list. OpenAlex showed the same 6.)

7. **Duong et al. (2024) — wrong metadata (MUST FIX):** Title lacks subtitle, and DOI 10.1108/tr-01-2024-0027 actually resolves to "…parasocial interaction and tourists' continuance intention" by **Duong, Nguyen, Ngo, Pham, Vu, & Dang**, *Tourism Review, 80*(4), 813–827 (2025 issue, online 2024). The manuscript's author trio and truncated title do not match this DOI. Fix to:
   `Duong, C. D., Nguyen, T. H., Ngo, T. V. N., Pham, T. T. P., Vu, A. T., & Dang, N. S. (2024). Using generative artificial intelligence (ChatGPT) for travel purposes: Parasocial interaction and tourists' continuance intention. *Tourism Review, 80*(4), 813–827. https://doi.org/10.1108/TR-01-2024-0027`

8. **Eloundou et al. (2023) — arXiv style:** APA 7 preprint format is fine as written (*title in italics*; arXiv; DOI). Optionally add version/ID: "arXiv:2303.10130". Acceptable as-is. DOI 10.48550/arXiv.2303.10130 verified valid.

9. **Appel et al. (2025) — arXiv style:** same — acceptable, but see Task 4 for author-order fix.

10. **En-dashes / hyphens:** All page ranges use en-dashes correctly. Buhalis & Leung title correctly uses an em dash (matches the published title). No hyphen-in-page-range errors found.

11. **Ampersands:** All reference entries correctly use "&" (no "and"). In-text narrative citations correctly use "and"; parenthetical citations correctly use "&". OK.

12. **Italics:** Volume numbers and journal/book titles are italicized; issue numbers correctly not italicized. Book titles italicized (Ivanov & Webster; Eloundou; Appel; Yildirim; Noll; Anthropic; data sets). OK.

13. **Çolak (2023) — incomplete (minor):** No pages listed; Crossref shows *8*(22), 919–939. Fix: add `, 919–939` after issue.

14. **Stergiou & Nella (2024) — incomplete (minor):** Now published: *International Journal of Tourism Research, 26*(5). Fix: add volume/issue: `*International Journal of Tourism Research, 26*(5). https://doi.org/10.1002/jtr.2757` (no page numbers in Crossref).

15. **Noll et al. (2025):** institutional report format acceptable. Verified real (UNLV/Brookings Mountain West, Nov 2025, authors Noll, Cason, Cheche, Brown). Manuscript author list partially wrong — see #22.

16. **Pham et al. (2024):** Crossref shows third author as **Giang Khanh Huyen Nguyen** (family name *Nguyen*), i.e., "Pham, H. C., Duong, C. D., & Nguyen, G. K. H." Manuscript has "Van, H. T. T." — wrong surname. Fix (see #21).

## Task 3 — Bibliographic plausibility spot-checks

| Entry | Verdict | Evidence |
|---|---|---|
| Acemoglu (2024) *Economic Policy, 39*(121), 13–58 | **WRONG VOL** | OUP/NBER: **Volume 40**, Issue 121, pp. 13–58 (2025 issue; first published Sep 2024). Fix: `*Economic Policy, 40*(121), 13–58` |
| Acemoglu & Restrepo (2019) JEP 33(2), 3–30 | ✓ | Correct |
| Brynjolfsson, Li & Raymond (2024) QJE 140(2), 889–942 | **WRONG YEAR (vol/year)** | QJE 140(2) is **May 2025** (online 2024). APA: cite issue year → 2025; in-text citations must change to 2025 as well. Fix: `…(2025). Generative AI at work. *Quarterly Journal of Economics, 140*(2), 889–942…` (also update Acemoglu & Restrepo sentence, §2.4, §1) |
| Buhalis & Leung (2018) IJHM 71, 41–50 | ✓ | Correct (Vol. 71, April 2018, pp. 41–50) |
| Doğru et al. (2023) JHTR | PARTIAL | Real; complete as #6 (vol 49, iss 2, pp 235–253; 6 authors) |
| Eloundou et al. (2023) arXiv 2303.10130 | ✓ | DOI valid; metadata correct |
| Felten, Raj & Seamans (2021) SMJ 42(12), 2195–2217 | ✓ | Correct |
| Filieri et al. (2022) *Electronic Markets, 32*, 2325–2351 | **LIKELY FABRICATED** | DOI 10.1007/s12525-022-00577-4 not found in Crossref, OpenAlex, or doi.org (404). No Filieri/Raguseo/Vitari AI-in-tourism article exists in *Electronic Markets* (checked all Filieri works; author's only EM-adjacent work is in IJCHM 2021). Pages 2325–2351 belong to a different EM 32(4) cluster of unrelated papers. The real article with this exact title is **Nannelli et al. 2023** (already cited separately). Fix: delete the Filieri entry and the corresponding in-text citation in §2.2, or replace with a real AI-in-tourism review (e.g., Ivanov & Webster 2019; Knani et al. 2022 IJHM bibliometric review, 10.1016/j.ijhm.2022.103317) |
| Gretzel, Sigala, Xiang & Koo (2015) EM 25(3), 179–188 | ✓ | Correct |
| Ivanov & Webster (2019) Emerald | ✓ | Book real; DOI 10.1108/9781787566873 resolves to Emerald. Fine as-is (optional: hyphenated DOI form per publisher, 10.1108/978-1-78756-687-3) |
| Kleinberg et al. (2015) AER 105(5), 491–495 | ✓ (but uncited) | Correct metadata — but unused (delete, #3) |
| Athey (2017) Science 355(6324), 483–485 | ✓ (but uncited) | Correct metadata — but unused (delete, #2) |
| Nannelli et al. (2023) EPS 31(**12**), 2459–2480 | **WRONG ISSUE+PAGES** | Actual: *European Planning Studies, 31*(**7**), **1325–1344**. Fix: `*European Planning Studies, 31*(7), 1325–1344` |
| Çolak (2023) *8*(22) | ✓ (+add pages 919–939) | Crossref confirms vol 8, iss 22, pp 919–939 |
| Comin & Hobijn (2010) AER 100(5), 2031–2059 | ✓ | Correct |
| Frey & Osborne (2017) TFSC 114, 254–280 | ✓ | Correct |
| Tussyadiah (2020) ATR 81, 102883 | ✓ | Correct |
| Noy & Zhang (2023) Science 381 | **NOT IN REFERENCE LIST** | This work (Noy & Zhang, "Experimental evidence on the productivity effects of generative artificial intelligence," *Science, 381*(6654), 187–192) is **not cited and not listed** in the manuscript — the reviewer prompt included it as a spot-check target, but no action needed beyond awareness |
| Yildirim (2026) SSRN | ✓ | DOI 10.2139/ssrn.6274118 resolves (Crossref, 2026, title matches) |
| Dwivedi et al. (2023) IJIM 71, 102642 | N/A (missing entry) | Correct metadata if added per #1 |

## Task 4 — [AN]-related citations

17. **Anthropic (2026) — attributed but authorship nuance (minor):** The June 26, 2026 "Cadences" report is real (anthropic.com/research/economic-index-june-2026-report) and the official citation lists **7 named authors** (Massenkoff, Lyubich, Sacher, Hitzig, Zhang, Heller, McCrory) rather than "Anthropic" as corporate author. APA permits corporate attribution to the dataset publisher, and the manuscript cites the *data release* (Hugging Face dataset + documentation), for which corporate-author "Anthropic" is defensible. **PASS with note:** if the report itself (not the dataset) is cited, APA 7 would require Massenkoff et al. (2026). At minimum consider: `Anthropic. (2026, June 26). *Anthropic Economic Index report: Cadences* [Data set and documentation]. https://huggingface.co/datasets/Anthropic/EconomicIndex` (current form acceptable for a data citation).

18. **Appel et al. (2025) — author order WRONG (MUST FIX):** arXiv 2511.15080 and Anthropic's own BibTeX give: **Appel, R.; McCrory, P.; Tamkin, A.; Stern, M.; McCain, M.; Neylon, T.** (per arXiv listing: Appel, McCrory, Tamkin, McCain, Neylon, Stern — note arXiv and Anthropic BibTeX disagree on order of last three). Manuscript lists "…McCain, M., Neylon, T., & Stern, M." — matching arXiv's order. **Both authoritative sources agree on the first three authors; the manuscript matches arXiv's listing exactly.** arXiv order: Appel, McCrory, Tamkin, McCain, Neylon, Stern. Manuscript: Appel, McCrory, Tamkin, McCain, Neylon, Stern. **Verdict: matches arXiv; PASS** (note Anthropic's own site swaps Stern/McCain/Neylon — follow arXiv, the version of record for the DOI). Title, year 2025, arXiv DOI 10.48550/arXiv.2511.15080 all verified correct.

## Summary of must-fix items (severity high)

| # | Location | Fix |
|---|---|---|
| H1 | §1 | Add Dwivedi et al. (2023) reference entry (or drop citation) |
| H2 | §2.2 | Filieri et al. (2022) reference is unverifiable/fabricated — delete entry + citation, or substitute a real review |
| H3 | References | Correct Acemoglu 2024: vol **40**(121), 13–58 |
| H4 | References + §1/§2.4 | Correct Brynjolfsson et al. year to **2025** (in-text too) |
| H5 | References | Correct Nannelli et al.: **31(7), 1325–1344** |
| H6 | §2.2 | Buhalis and Leung year: 2017 → **2018** |
| H7 | References | Doğru et al.: add 49(2), 235–253 + 2 missing authors |
| H8 | References | Duong et al.: correct author list (6 authors) + subtitle + 80(4), 813–827 |
| H9 | References | Re-order: Duong before Doğru |
| H10 | References | Delete uncited Athey (2017) and Kleinberg et al. (2015) or cite them |

Medium/minor: Çolak pages; Stergiou & Nella vol/iss; Pham third-author name; Anthropic authorship note; Pham author-name correction (Nguyen, not Van).

**Overall: FAIL — manuscript requires the 10 high-severity corrections above before submission.**
