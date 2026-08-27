# Review Round 4 — Method & Measurement Review (author-executed devil's-advocate pass, 2026-08-27)

Focus: the two questions a hostile referee would ask about measurement and inference. Per integrity rules, this round argues against the paper and then adjudicates each attack.

## Attack 1: "Tourism SOC intensity is not tourism"
**Claim:** Food Prep & Serving + Personal Care include non-tourism workers (hospital cafeterias, nursing homes, airlines' catering); meanwhile, tourism-firm managers/transport workers sit elsewhere. The proxy is label-inflated.
**Adjudication: VALID concern, partially defused.**
- The measure genuinely captures "occupations where tourism work concentrates," not "tourism industries."
- Counter-evidence in the paper's favor: the two groups map to the core service-delivery labor of hospitality (accommodation-food service + personal services), and the paper never claims industry totals.
- Residual fix (beyond relabeling, already done): none available without industry-level data — acknowledged as inherent data limit (§5.2, third limitation). Status: *acknowledged limitation*, not fatal.

## Attack 2: "The cross-country gradient is Claude-user composition, not labor-market structure"
**Claim:** Rich-country users skew professional; poor-country Claude users may be students/enthusiasts. The negative income gradient may reflect the demographics of Claude adopters, not occupational structure.
**Adjudication: VALID and the strongest attack on the paper.**
- The paper already flags it (platform composition, limitation #1) but §4.3 currently frames composition as *occupational* composition only.
- Fix: §4.3 must explicitly name *user-base composition* as a competing explanation for the gradient, and the abstract's "occupational-structure pattern" framing must absorb it. Status: *fixable by reframing* → applied in round 6 rewrite.
- What would settle it (AI-platform user demographics by country) is proprietary — inherent data limit, acknowledged.

## Attack 3: "No causal content; policy implications unwarranted"
**Adjudication: PARTIALLY VALID.**
- §5.3 policy paragraph over-reads a cross-sectional association. Fix (round 6): recast as *monitoring implications* (what the data can/cannot tell administrators) rather than intervention advice. The travel-exports association is an association; do not recommend programs based on it.

## Attack 4: "First-ness is unverifiable and fragile"
**Adjudication: handled.** Time-stamped search log (review/novelty_search_log.md) now in repo; abstract says "first behavioral evidence" which is precise (not "first AI-tourism study"). Wording kept but anchored.

## Scores after adjudication (0–10)
- Originality 8.5 (genuine data novelty)
- Methodological Rigor 6.5 (honest descriptive work; inherent platform/sample-floor limits)
- Evidence Sufficiency 6.0 (associational; robustness now honestly qualified)
- Argument Coherence 7.5 (composition narrative consistent)
- Writing Quality 8.0

**Verdict: Major-revision issues resolved or explicitly acknowledged; no remaining silent over-claim.**
