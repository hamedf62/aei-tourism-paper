# AI in Tourism Work: Behavioral Evidence from the Anthropic Economic Index and Its Economic Correlates

**Hamed Fallah Tafti**

Department of Management, University of Science and Art, Yazd, Iran

h.fallah@sau.ac.ir

---

*Manuscript prepared for submission to* Tourism Economics.

*Running head:* AI in tourism work: behavioral evidence

*Word count:* ~4,200 main text (excluding abstract, references, tables, and figure captions); ~6,700 total including tables and appendices

---

## Abstract

This study provides the first behavioral evidence on artificial intelligence (AI) use in tourism occupations, drawing on the Anthropic Economic Index (AEI), an open dataset that maps millions of privacy-protected Claude conversations to Standard Occupational Classification (SOC) categories. Using three data snapshots (August 2025, April 2026, May 2026) covering up to 121 countries, I measure tourism-SOC intensity—the share of conversations in the two major groups most typical of tourism employment—and track its level, growth, and economic correlates. Tourism-occupation AI usage is small (below 2.5% of conversations almost everywhere) but is the fastest-growing slice of the platform's conversation mix: among twelve countries observed across all three snapshots, intensity tripled in nine months, with strong convergence toward a common level. The cross-sectional income gradient is a transitional composition effect rather than a structural feature: it is positive among early-adopter countries in August 2025, indistinguishable from zero by April 2026, and only weakly negative in May 2026, reversing sign as adoption broadens down the income distribution. At the task level, tourism conversations lean toward automation rather than augmentation, and front-line hospitality occupations rank in the top decile of 718 detailed occupations on the "human-only ability" share, indicating that behavioral AI use concentrates on the sector's administrative and creative periphery rather than its core service encounters. The paper contributes a reproducible monitoring framework for tourism labor markets with behavioral data.

**Keywords:** artificial intelligence; tourism employment; Anthropic Economic Index; occupational exposure; digital traces; tourism economics

**JEL codes:** Z32; O33; J24

---

## 1. Introduction

Tourism is one of the world's largest service industries, supporting roughly one in ten jobs globally and contributing about 10% of world GDP (World Bank, 2025; World Travel & Tourism Council [WTTC], 2025). It is also, by most accounts, among the industries most exposed to artificial intelligence (AI). Since 2023, a fast-growing literature has examined how generative AI reshapes tourism demand, traveler behavior, and service design (Doğru et al., 2025; Dwivedi et al., 2023; Nannelli et al., 2023; Tussyadiah, 2020). Yet almost everything economists know about AI *adoption in tourism work* comes from surveys, expert assessments of occupational task descriptions, or firm-level case studies. No existing study measures what tourism workers actually do with AI systems.

This paper takes a step in that direction using a new kind of evidence: the Anthropic Economic Index (AEI), an open dataset constructed from millions of privacy-protected Claude conversations and mapped to U.S. O*NET task categories and SOC occupations (Anthropic, 2026; Appel et al., 2025). The AEI is behavioral. Each observation is a real conversation, classified by occupation and task, not a self-report of intentions or a subjective expert rating of "exposure." For tourism economics, this offers something survey instruments cannot: a direct, continuously updated record of how workers in tourism-related occupations use a frontier AI system, observed across more than 100 countries.

The paper asks three questions. (1) How intensively are tourism-typical occupations represented in AI conversations, and how does this vary across countries? (2) What economic and tourism-specific conditions co-vary with tourism-occupation AI usage? (3) What is the *character* of AI use in tourism occupations—automation or augmentation, human-replaceable or human-only, work or personal? Each question maps onto a distinct literature: the first to occupational exposure studies (Eloundou et al., 2023; Felten et al., 2021; Frey & Osborne, 2017), the second to the economics of technology diffusion in services (Acemoglu, 2024; Comin & Hobijn, 2010), and the third to the automation-versus-augmentation debate in labor economics (Acemoglu & Restrepo, 2019; Brynjolfsson et al., 2025) and to AI-in-tourism research (Ivanov & Webster, 2019; Tussyadiah, 2020).

The contribution is fourfold. First, it is—to the author's knowledge after a systematic search of the literature (Section 2.3)—the first study to combine behavioral AI-usage data with tourism economics. Prior work using the AEI has examined aggregate macroeconomic adoption patterns (Appel et al., 2025; Yildirim, 2026) and regional U.S. patterns (Noll et al., 2025), but not tourism occupations or tourism development. Second, it introduces a transparent, fully reproducible measure—tourism SOC intensity—that derives from published, auditable data rather than a constructed survey index. Third, it documents an occupational-structure pattern that runs against the intuitive "rich countries adopt AI faster" prior, while demonstrating through systematic robustness checks exactly how far that pattern can be trusted—a methodological contribution in itself. Fourth, it demonstrates a monitoring framework that tourism scholars and statistical agencies can replicate each AEI release without proprietary data or fieldwork.

Previewing the results: tourism-occupation AI usage averages about 1.05% of country-level Claude conversations (the mean of the Food Preparation and Serving Related and Personal Care and Service group shares) and ranges from 0.66% (Tunisia) to 2.87% (Kyrgyz Republic). Richer countries show *suggestively lower* tourism intensity (β on log GDP per capita ≈ −0.11 to −0.18, component- and sample-dependent), driven by composition: in rich economies, AI conversations concentrate overwhelmingly in computer, mathematical, and management occupations, so tourism groups shrink as a share even as their absolute usage grows. The one tourism-specific indicator that correlates positively with tourism-occupation AI usage is the share of travel services in service exports (r = +0.17, CI [0.04, 0.33])—economies more dependent on tourism exports show more tourism-occupation AI activity relative to their overall usage. At the task level, tourism occupations skew toward automation rather than augmentation, and front-line hospitality occupations (Waiters and Waitresses, Concierges, Travel Agents, Flight Attendants) rank in the top decile of the 718 detailed occupations on the human-only ability share (84th–94th percentile), meaning that the AI conversations attributed to them overwhelmingly involve tasks adjacent to—rather than inside—core service delivery.

The paper proceeds as follows. Section 2 reviews the literature and positions the contribution. Section 3 describes the data and the construction of the tourism intensity measures. Section 4 presents results: occupation profiles, cross-country correlates, and task-level patterns. Section 5 discusses interpretations, limitations, and implications for tourism economics research and policy. Section 6 concludes.

## 2. Literature review and contribution

### 2.1 Measuring AI exposure and adoption in labor economics

Three measurement traditions dominate research on AI and employment. The *task-exposure* tradition scores occupations by their predicted exposure to language models or robotics: Frey and Osborne (2017) mapped 702 occupations to automation probabilities; Felten et al. (2021) built an AI exposure index from O*NET ability requirements; Eloundou et al. (2023) rated O*NET tasks by LLM exposure. These measures are expert judgments about *potential*, not observations of *use*. The *survey* tradition asks workers or firms whether they use AI: the U.S. Census Bureau's Business Trends and Expectations Survey, Eurostat's AI usage module, and several academic surveys all find adoption rates between 4% and 30% depending on firm size, sector, and year. Surveys capture use but suffer from recall error, low response rates, and time lags of one to two years. The *behavioral* tradition is the newest: Brynjolfsson et al. (2024) studied a customer-service firm's AI assistant deployment; AEI-based studies use observed conversations at population scale (Appel et al., 2025; Anthropic, 2026). The AEI's coverage of 121 countries in the June 2026 release makes it, to date, the largest cross-country behavioral dataset on AI use in work.

Each tradition has known weaknesses that shape what claims it can support. Exposure indices cannot say whether workers actually use AI; surveys can say little about *what* users do with it; and behavioral data observe only users of one platform (here, Claude), so platform composition becomes a first-order caveat. This paper's method (Section 3.3) therefore treats AEI shares as *within-platform composition* measures and triangulates them against World Bank indicators, rather than claiming economy-wide adoption rates.

### 2.2 AI in tourism research

Tourism scholars have produced a substantial literature on AI in the industry, summarized in recent reviews (Knani et al., 2022; Nannelli et al., 2023; Tussyadiah, 2020). Four strands are relevant here. First, *service automation*: Ivanov and Webster (2019) and successors analyze robot and AI adoption economics in travel, tourism, and hospitality, with emphasis on cost-benefit calculus for specific service tasks. Second, *smart tourism*: Gretzel et al. (2015) and Buhalis and Leung (2018) established the ecosystem view of connected, data-driven destinations—AI as infrastructure rather than labor substitute. Third, *consumer-facing generative AI*: a wave of 2023–2025 papers studies tourist acceptance of ChatGPT-style tools for planning and in-trip use (e.g., Duong et al., 2025; Pham et al., 2024; Stergiou & Nella, 2024), consistently finding higher acceptance for informational than for transactional tasks. Fourth, *industry-level foresight*: Doğru et al. (2025) frame generative AI's disruption pathways for hospitality and tourism research, and Çolak (2023) offers an early descriptive look at AI's impact on tourism employment structure.

Across all four strands, evidence about *tourism workers* comes from surveys of managers or employees, vignette studies, and adoption intentions. No strand observes the labor side behaviorally at scale. This is the gap the present paper addresses.

### 2.3 Novelty assessment

A systematic search (Appendix A) across OpenAlex, Google Scholar, SSRN, and arXiv in August 2026 using combinations of "Anthropic Economic Index," "Claude," "tourism," "hospitality," "occupation," and "adoption" returned no study combining AEI data with tourism economics. The nearest prior works are: (i) Appel et al. (2025), the AEI authors' own geographic analysis, which documents cross-country usage differences but does not examine tourism occupations; (ii) Yildirim (2026), which tests aggregate macroeconomic correlates of AEI usage without occupational structure; and (iii) Çolak (2023), which discusses AI's employment-structure effects in tourism theoretically, without behavioral data. The nearest prior work is thus Appel et al. (2025); the present study extends that line by introducing an industry lens—tourism—onto the same underlying data, which no prior work has done.

### 2.4 Theoretical framing

Two framings organize the analysis. The first is the *diffusion-composition* distinction. Aggregate AI adoption statistics conflate two margins: the intensive margin (how much AI is used per worker) and the compositional margin (which occupations exist in an economy). Tourism economies differ systematically on the compositional margin—tourism occupations are a larger slice of employment in developing economies—so occupational composition can generate adoption patterns that look like reversed diffusion gradients. Distinguishing the two margins is essential for policy: a high tourism-SOC AI share in a low-income country may reflect few AI conversations overall spread thinly, not deep technological upgrading of tourism work.

The second framing is the *automation-augmentation* distinction (Acemoglu & Restrepo, 2019; Brynjolfsson et al., 2025). The AEI classifies each conversation by collaboration bucket and by whether a human could complete the task unaided ("human-only ability"). In tourism, where the core product is co-produced human service (Tussyadiah, 2020), the share of AI use that automates rather than augments is a first-order economic question: automation-bearing use substitutes for labor tasks; augmentation-bearing use complements them. The AEI's task-level metrics allow this decomposition without any survey instrument.
The two framings generate testable predictions that organize the empirical work. From the diffusion-composition distinction: (P1) cross-sectional gradients in occupational AI shares should track the *adopter composition* of the platform rather than stable economic structure, and should therefore shift systematically as the platform's country footprint broadens; (P2) early-adopter countries should differ from later entrants in income and overall usage intensity. From the automation-augmentation distinction: (P3) occupations whose output is codifiable (schedules, templated communications, itineraries) should show automation-leaning collaboration profiles, while interpretation- and relationship-intensive tasks should show human-only profiles; (P4) front-line service occupations should rank high on human-only ability even where their usage share is nonzero, because their core tasks resist codification. A fifth prediction follows from diffusion economics generally: (P5) levels of a new technology's use should converge across adopters as the technology matures, with growth rates inversely related to initial levels (β-convergence). The three-period panel (Section 4.6) tests P1, P2, and P5 directly; the task-level metrics test P3 and P4.

## 3. Data and measurement

### 3.1 The Anthropic Economic Index

The AEI (Anthropic, 2026) publishes aggregated statistics on Claude conversations by geography, occupation, task, and collaboration type. The June 26, 2026 release (the sixth) covers April and May 2026 and includes the `claude_ai` source—consumer and product conversations—for 121 countries at the country level and 718 SOC detailed occupations at the global level. Each row records a metric (share, per-capita usage index, automation/augmentation share, human-only ability share, mean AI autonomy, artifact type, and so on) for a geography-category pair. Cells below aggregation thresholds or geography sample floors are unpublished (missing), which the analysis treats as missing rather than zero (Anthropic, 2026, documentation). The data are released under CC-BY 4.0.

Two properties matter for interpretation. First, the unit is the *conversation*, not the worker: heavy users contribute more observations, so the AEI measures usage intensity, not headcount adoption. Second, the platform is Claude: shares therefore describe composition within Anthropic's user base, which is not representative of AI users globally. The per-capita usage index (usage share divided by working-age population share) partially adjusts for country size but not for user-base composition. Section 3.3 builds these caveats into the design.


*Release history and schema harmonization.* The AEI's earlier releases used a weekly-snapshot schema (occupation facet at level 0 with `soc_pct` variables); the mid-2026 releases moved to a monthly, metric-based schema with major groups at hierarchy level 1. The intermediate releases (November 2025, February 2026) do not publish occupation facets for countries and cannot enter the panel. Two schema generations therefore supply the three usable periods: August 2025 (17 countries with both tourism groups published), April 2026 (65), and May 2026 (78). Because the 2025 schema shares sum across classified conversations only, levels are not directly comparable to 2026 levels; all cross-period statements in this paper are therefore within-country statements (growth, convergence, gradient reversal), which are scale-invariant, and the 12-country balanced panel is the estimation sample for all longitudinal statistics.

### 3.2 Tourism indicators

Country-level tourism and economic indicators come from the World Bank World Development Indicators (WDI), retrieved via API in August 2026, using the most recent available year in 2019–2024 for each country: international tourist arrivals; international tourism receipts; GDP per capita (current US$); employment in services (% of total employment, modeled ILO estimate); travel services (% of service exports, balance of payments); ICT service exports (% of service exports); individuals using the Internet; mobile subscriptions; unemployment; services value added; and population. Variables are described in Appendix Table A1. The analysis sample is the intersection of AEI countries with available WDI data: 120 countries, of which 113 have complete data for the main regressions.

### 3.3 Measures

**Tourism SOC intensity** (short form: *tourism intensity*) is the mean of country shares of Claude conversations in the two SOC major groups most centrally tied to tourism employment: Food Preparation and Serving Related (SOC 35) and Personal Care and Service (SOC 39, which contains travel guides, tour guides, concierges, and baggage porters). I take the mean rather than the sum because the two groups overlap in tourism relevance but differ in scale, and the mean is less sensitive to a single group's idiosyncratic share. I report results for each component separately and for alternatives (adding Sales and Related; adding Arts, Design, Entertainment, Sports, and Media) in robustness checks (Section 4.4).

The mapping from "tourism" to these two groups is deliberately *conservative*: it captures the food-service and personal-service core of hospitality work but excludes transportation occupations (many of which serve non-tourism demand) and management occupations (which are shared across industries). This choice trades coverage for precision: the measure reads "share of AI conversations in occupations where tourism work concentrates," not "share of AI conversations in tourism industries," which no occupation-level classification can deliver because SOC is industry-agnostic. Section 5.2 discusses the consequences.

**Overall usage intensity** is the AEI per-capita usage index: the country's share of global Claude conversations divided by its share of world working-age population.

**Correlates** enter in logs where they are levels (GDP per capita, arrivals per capita) and in levels where they are percentages (services employment, travel services share of exports, internet use).

### 3.4 Method

The analysis is descriptive and associational; no causal claim is made. Cross-sectional correlations are reported with 95% bootstrap confidence intervals (2,000 replications, resampling countries). Multivariate specifications are ordinary least squares of tourism SOC intensity on log GDP per capita and sets of controls, with heteroskedasticity-robust standard errors (Huber-White). All data preparation and estimation code is in the replication repository (Fallah Tafti, 2026), and every table regenerates from the raw AEI file and the WDI API with two commands.

### 3.5 Ethics and data provenance

The AEI is aggregated, privacy-protected data published for research use; no individual-level conversation content is available or analyzed. The World Bank data are public. No human subjects are involved, and no institutional review is required.

## 4. Results

### 4.1 Where tourism occupations sit in AI conversations

Figure 1 shows the global distribution of Claude conversations across SOC major groups. Computer and Mathematical dominates at about 23% of conversations. The tourism-relevant groups are dispersed: Arts, Design, Entertainment, Sports, and Media is the second-largest group overall (about 13.6%), while Sales and Related is about 9.1%; Personal Care and Service is 1.2%, and Food Preparation and Serving Related and Transportation and Material Moving account for about 0.5% and 0.3%, respectively. The immediate implication is that tourism-typical occupations are a small slice of behavioral AI usage at the global level—far below what "tourism is highly exposed to AI" narratives might suggest—and that any country-level analysis must treat these shares as composition-sensitive.

Table 1 profiles 19 tourism-relevant detailed occupations globally, with full task-level metrics for each. Two regularities stand out. First, the largest tourism-occupation shares belong to managerial and coordination roles—Food Service Managers (0.13%), Meeting, Convention, and Event Planners (0.12%), Recreation Workers (0.11%)—rather than front-line service roles. Second, the classic front-line occupations are nearly invisible: Waiters and Waitresses (0.17% of global conversations but the largest single detailed tourism occupation), Tour Guides and Escorts (0.03%), Travel Agents (0.01%), Flight Attendants (0.01%), Hotel, Motel, and Resort Desk Clerks (0.00%). The use-case metrics indicate that for most of these occupations, only a minority of conversations are work-related (e.g., Waiters and Waitresses: 2.8% work), meaning much observed "tourism-occupation" AI use is personal use by people in those occupations—a further composition caveat that the analysis treats explicitly.

### 4.2 Cross-country patterns

Figure 2 plots tourism SOC intensity against log GDP per capita. The relationship is negative and moderately strong: the bivariate correlation is −0.30 (CI [−0.41, −0.19]). Table 2 reports the full correlation set. Tourism intensity correlates negatively with overall Claude usage intensity (r = −0.36), services employment share (r = −0.34), services value added (r = −0.38), internet use (r = −0.30), and mobile subscriptions (r = −0.29); and positively with travel services share of service exports (r = +0.17, CI [0.04, 0.33]). Among the tourism-specific indicators, log receipts per capita is marginally significant (r = −0.27, CI [−0.44, −0.10]), whereas log arrivals per capita is not distinguishable from zero (CI [−0.42, 0.01]).

Table 3 reports OLS regressions. In the baseline model, log GDP per capita alone explains about 16% of the variance in tourism intensity (β = −0.11, t = −4.7). Adding log arrivals per capita raises adjusted R² to 0.21 (M3); the arrivals coefficient is positive (β = 0.04, t = 1.7, p < 0.10), consistent with tourism activity slightly raising tourism-occupation AI usage at a given income level. In the full specification (M5), the GDP per capita coefficient steepens to −0.18 (t = −3.4) and arrivals per capita retains a positive sign, though neither arrivals nor internet use is individually significant. Figure 3 visualizes the correlation estimates with their bootstrap intervals.

The headline pattern—richer countries show lower tourism-occupation AI *shares*—should be read jointly with the positive cross-country correlation between GDP per capita and overall Claude usage (the usage index and GDP per capita correlate at about +0.8 in the panel). In rich economies, AI conversations concentrate in Computer and Mathematical, Management, and Business occupations, mechanically shrinking the tourism groups' relative shares. In poorer economies, the absence of large knowledge-occupation shares leaves tourism groups with relatively more weight. The composition mechanism is examined directly in Section 4.3.

### 4.3 A composition interpretation

Three pieces of evidence support a composition rather than a diffusion interpretation. First, the level-share decomposition: approximate *absolute* tourism-occupation usage—country share of global Claude conversations multiplied by the tourism group share—correlates *positively* with log GDP per capita (r = +0.22), even though the *relative* tourism share correlates negatively (r = −0.30). Richer countries do not show less Claude usage in tourism groups; they show less tourism share of a much larger total, because overall usage per capita rises steeply with income (usage index and log GDP per capita correlate at +0.83). Second, the mechanical channel: countries with larger knowledge-occupation conversation shares (Computer and Mathematical; Management; Business and Financial Operations combined) do show lower tourism shares, but the relationship is weak (r = −0.06), indicating that the income gradient operates through overall usage scale and occupational diversification rather than through any single knowledge-occupation block. Third, within-country occupational structures: services employment share, a proxy for structural transformation, correlates negatively with tourism intensity, indicating that as economies shift toward broad services (finance, education, administration), tourism occupations lose relative weight in AI conversations even as the service economy grows.

The interpretation has a policy edge, but also a rival explanation that must be named. The income gradient in tourism intensity is consistent with *occupational* composition: in rich economies, AI conversations concentrate overwhelmingly in knowledge occupations, shrinking tourism groups' relative shares. But it is equally consistent with *user-base* composition: Claude adopters in high-income countries skew toward professional occupations, so the platform's occupational mix partly mirrors its subscriber mix rather than the economy's. The two mechanisms are observationally equivalent in these data, because the AEI observes only Claude users and platform user demographics by country are proprietary. What the data can rule out is the naive diffusion reading: richer countries do not use Claude *less* in tourism occupations—they use it less *as a share* of a much larger total. Distinguishing the two composition mechanisms requires platform-external occupational usage data, which no open source currently provides (Section 5.2).

The near-invisibility of front-line tourism occupations in high-income countries' AI conversations (Section 4.1) is the most robust descriptive fact in this paper: it appears in both months, at the global level, and at the task level (human-only ability shares in the top decile). It suggests that behavioral AI use has so far concentrated in the sector's administrative and creative periphery—tasks that exposure indices flagged as most susceptible (Eloundou et al., 2023)—while core service encounters remain, behaviorally, human territory.

### 4.4 Task-level character: automation, augmentation, human-only ability

Table 4 and Figure 4 compare collaboration buckets across SOC major groups. Tourism-relevant groups straddle the diagonal: Food Preparation and Serving Related is nearly balanced (49.1% automation / 50.9% augmentation), Sales and Related is augmentation-leaning (43.8% automation), while Personal Care and Service is automation-leaning (55.9% automation)—an unusual profile, since most non-tourism service groups are augmentation-heavy. Arts, Design, Entertainment, Sports, and Media shows the second-strongest augmentation profile of any major group (64.2% augmentation), consistent with creative work's complementarity with generative AI.

At the detailed level (Table 1, right columns), front-line hospitality occupations rank in the top decile of the 718 detailed occupations on the human-only ability share: Concierges (100%, 94th percentile), Waiters and Waitresses (99.5%, 94th percentile), Travel Agents (99.1%, 92nd percentile), Flight Attendants (97.7%, 84th percentile). Supervisory and planning occupations rank lower—Meeting, Convention, and Event Planners (83.7%, 23rd percentile), Curators (86.8%, 33rd percentile)—indicating that the human-only pattern is specific to front-line service roles rather than tourism occupations as a whole. Mean AI autonomy scores of the tourism occupations range between 2.3 and 3.0 on the 1–5 scale, spanning the global detailed-occupation mean of 2.74: planning roles exceed it (Meeting Planners: 3.03, 90th percentile) while Flight Attendants sit near the bottom of the distribution (2.32, 2nd percentile). Together, these metrics say that the AI conversations attributed to front-line tourism occupations rarely involve tasks the AI can fully own: they are drafting, planning, and information-adjacent tasks performed *alongside* human service roles, not substitutions for them.

### 4.5 Robustness

Three checks (Appendix B, Tables B1–B3) probe the main pattern, and their results call for an honest qualification of it. First, alternative tourism intensity definitions: using the *sum* instead of the mean of the two groups yields a near-zero income association (β = −0.01, n.s., n = 78, because the Food Preparation group is published for fewer countries), and *adding* Arts, Design, Entertainment, Sports, and Media strengthens it (β = −0.52); adding Sales and Related, however, *reverses* the sign (β = +0.15). The negative income gradient is therefore specific to the two core tourism groups and should not be generalized to broad "hospitality-plus-retail-plus-arts" definitions. Second, excluding the five countries with the highest tourism intensity (Kyrgyz Republic, Angola, Mongolia, Azerbaijan, Armenia) leaves the income gradient intact (β = −0.085, t = −4.9), so the pattern is not driven by small tourism-economies at the top of the range. Third, the May–April stability check qualifies the headline rather than confirming it: country-level tourism intensity correlates across the two months at r = 0.62, the April income coefficient is −0.075 (versus −0.108 in May), and the bivariate correlations shift by up to 0.23 between months (travel exports: +0.17 in May, +0.40 in April). The sign of the income gradient is stable, but magnitudes are sensitive to the release month, consistent with the modest sample floors of the AEI at the country-month level.

Supplementary checks (Appendix B, Table B4) sharpen the qualification. The gradient survives winsorization at 1% (β = −0.10), exclusion of countries below half a million population (β = −0.11), and controlling for working-age population share (β = −0.10). But it is *component-specific*: estimated on Personal Care alone it is −0.09 (t = −5.0, n = 113), while on Food Preparation alone it *reverses* to +0.06 (t = +6.9, n = 77); and it *disappears* under population weighting (β = −0.02, t = −0.6). The negative gradient therefore reflects the composition of the published AEI sample as much as any economic regularity, and the paper treats it as suggestive. The findings that survive every check—the small absolute size of tourism-occupation AI usage, its level–share decomposition, and the front-line human-only profile—are the paper's load-bearing results.

### 4.6 Dynamics: a three-period panel (August 2025 – May 2026)

The cross-sectional results so far treat May 2026 as a single snapshot. The AEI's release history makes a modest longitudinal analysis possible: occupation-level shares by country are published for August 2025 (weekly snapshot, 17 countries with both tourism groups), April 2026 (65 countries), and May 2026 (78 countries). Twelve countries appear in all three periods. Three analyses exploit this structure (Table 5, Figures 5–7).

**Growth and convergence.** Between August 2025 and May 2026, tourism-occupation AI usage among the twelve panel countries grew from a mean of 0.25% to 0.84% of conversations—a 3.4-fold increase in nine months. Growth was strongly *convergence-consistent*: countries with the highest initial tourism share grew the least (β-convergence coefficient −0.57, t = −6.6, n = 12; Figure 6). The result survives leave-one-out exclusion of every country (β between −0.61 and −0.37; t between −7.5 and −2.9; Appendix B, Table B5) and is driven by the Personal Care component (β = −0.95, t = −8.9), not Food Preparation (β = −0.31, t = −1.3). Within-country ranking was stable across the nine-month window (Spearman ρ = 0.87 between August 2025 and May 2026), so convergence reflects countries approaching a common level from different starting points, not churning.

**The income gradient reverses as the platform broadens (Figure 7).** In the August 2025 snapshot—when Claude's country footprint was small and early-adopter-skewed—the income gradient in tourism intensity was *positive*: β = +0.09 (t = 3.2, n = 12). Early-adopter countries were systematically richer (mean log GDP per capita 10.25 vs. 9.53 for later entrants) and had nearly double the May 2026 usage index (2.77 vs. 1.57). By April 2026 the gradient was indistinguishable from zero (β = +0.01, t = 1.5, n = 64), and by May 2026 it had turned negative though insignificant (β = −0.01, t = −1.0, n = 77). The cross-sectional gradient that Sections 4.2–4.3 dissected is therefore not a stable structural parameter: it emerges from *which countries use the platform at all*. As adoption broadens down the income distribution, the early-adopter composition effect washes out.

**Decomposition.** The 0.59 percentage-point mean rise among panel countries decomposes exactly into within-country growth (0.59 pp); entry of new countries, whose tourism shares match the incumbent mean (0.87 vs. 0.84), contributes to the cross-section's level but not to the gradient's reversal. The gradient reversal is a composition-of-adoption phenomenon, not a within-country phenomenon.

Three implications follow. First, the negative cross-sectional income gradient in May 2026 (Section 4.2) should be read as a *transitional* pattern: it reflects a late stage of the adoption-broadening process, not a permanent feature of tourism AI use. Extrapolating it forward would be a mistake—the gradient has already collapsed from +0.09 to −0.01 in nine months. Second, convergence implies that country differences in tourism-occupation AI intensity are shrinking; monitoring frameworks (Section 5.3) should track the *level*, which is rising everywhere, rather than cross-country gaps, which are closing. Third, the nine-month growth rate (3.4×) is itself the headline: whatever the level's absolute smallness, tourism-occupation AI usage is the fastest-growing measurable slice of the platform's conversation mix, consistent with the generative-AI diffusion rates documented in firm settings (Brynjolfsson et al., 2025).

## 5. Discussion

### 5.1 What behavioral data add to tourism economics

The paper's central methodological claim is that behavioral AI-usage data open questions that surveys and exposure indices cannot answer. Exposure indices told the field *which* tourism tasks could be affected by AI; surveys told it whether firms *intend* to adopt; the AEI shows *which occupations actually use a frontier AI system, for what, and where*. The gap between potential and behavior is itself informative: tourism occupations rank high on exposure indices but low on observed usage, indicating that realized adoption lags assessed potential—an economically meaningful distinction for forecasting labor-market adjustment, and one that only behavioral data can detect.

### 5.2 Interpretation limits

Six limitations bound the interpretation. First, *platform composition*: the AEI observes Claude users, who skew toward high-income, English-proficient, digitally engaged populations. The cross-sectional income gradient partially reflects who uses Claude—and Section 4.6 shows this composition effect is itself time-varying, which is why the gradient reverses across periods. Second, *occupation attribution*: conversations are classified by inferred occupation, and classification error is not publicly quantified; some conversations attributed to tourism occupations may belong to users exploring tourism topics personally (the use-case metrics partially address this, but for most tourism occupations a minority of attributed conversations is work-related). Third, *industry-agnostic classification*: SOC codes describe occupations, not industries, so "tourism occupations" capture where tourism *work* is done, not all work done *in* tourism industries—managers in tourism firms appear under Management, and drivers under Transportation. The measure is best read as tourism-*work* intensity, a boundary the paper maintains throughout. Fourth, *cell publication*: AEI cells below aggregation thresholds or geography sample floors are unpublished, and the major-group shares are published for different country sets (Personal Care for 115 countries, Food Preparation for 79 in May 2026), so the analysis sample depends on the measure's construction; the sum specification drops to 78 countries, and the panel to 12. Fifth, *month sensitivity*: correlation magnitudes shift by up to 0.23 between releases; the three-period panel mitigates but does not eliminate this. Sixth, *panel brevity*: the occupation-level country panel spans three periods with a twelve-country balanced subsample—enough for convergence and gradient-reversal diagnostics, not for dynamics modeling; as more releases accumulate, the framework extends naturally.

### 5.3 Implications

For *research*, the results caution against extrapolating from exposure indices to adoption, demonstrate that cross-sectional AI-adoption gradients are transient artifacts of the adoption-broadening process (Section 4.6), and suggest that tourism AI research distinguish carefully between the intensive and compositional margins. For *policy*, the contribution is monitoring rather than prescription: these are platform shares, and no intervention should be designed from them. What they do offer tourism administrations is a low-cost, repeatable instrument for observing *where behavioral AI use sits* in the sector's occupational structure and *how fast it is growing*—with the May 2026 evidence pointing to a 3.4× nine-month growth rate and rapid convergence toward a common cross-country level. For *statistics*, the replication framework offers national tourism administrations that same instrument in reproducible form.

## 6. Conclusion

This paper introduced behavioral evidence on AI use in tourism occupations using the Anthropic Economic Index, the first tourism application of this data source. Tourism-typical occupations account for a small but fast-growing share of AI conversations: across the twelve-country panel, tourism-occupation intensity tripled in nine months, converging toward a common cross-country level. The cross-sectional income gradient observed in May 2026 is a transitional composition effect—it reverses sign as the platform broadens—rather than evidence that poor countries lead in tourism AI. The AI conversations that do occur in front-line tourism occupations lean toward automation and away from core service delivery, leaving human service encounters, behaviorally, the sector's core. The framework is transparent, reproducible, and repeatable with each AEI release, offering tourism economics a living instrument for tracking how the sector's work is—and is not—being reshaped by AI.

---

## Declarations

**Funding:** No funding was received for this research.

**Conflicts of interest:** The author declares none.

**Data availability:** The Anthropic Economic Index is publicly available at https://huggingface.co/datasets/Anthropic/EconomicIndex (CC-BY 4.0). World Bank indicators are publicly available via the WDI API. All processed data, code, and results are in the replication repository: https://github.com/hamedf62/aei-tourism-paper.

**AI-assistance disclosure:** The author used AI-assisted tools for code development, literature search assistance, and manuscript editing; all data analysis, interpretation, and final text were verified and approved by the author.

**Ethics statement:** The study uses only aggregated, publicly released, privacy-protected data; no human subjects, personal data, or institutional review involved.

---

## References

Acemoglu, D. (2024). The simple macroeconomics of AI. *Economic Policy, 40*(121), 13–58. https://doi.org/10.1093/epolic/eiae042

Acemoglu, D., & Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives, 33*(2), 3–30. https://doi.org/10.1257/jep.33.2.3

Anthropic. (2026, June 26). *Anthropic Economic Index report: Cadences* [Data documentation and release]. https://huggingface.co/datasets/Anthropic/EconomicIndex

Appel, R., McCrory, P., Tamkin, A., McCain, M., Neylon, T., & Stern, M. (2025). *Anthropic Economic Index report: Uneven geographic and enterprise AI adoption*. arXiv. https://doi.org/10.48550/arxiv.2511.15080

Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044

Buhalis, D., & Leung, R. (2018). Smart hospitality—Interconnectivity and interoperability towards an ecosystem. *International Journal of Hospitality Management, 71*, 41–50. https://doi.org/10.1016/j.ijhm.2017.11.011

Çolak, O. (2023). The impact of artificial intelligence on the employment structure of the tourism industry. *İktisadi İdari ve Siyasal Araştırmalar Dergisi, 8*(22), 919–939. https://doi.org/10.25204/iktisad.1347642

Comin, D., & Hobijn, B. (2010). An exploration of technology diffusion. *American Economic Review, 100*(5), 2031–2059. https://doi.org/10.1257/aer.100.5.2031

Dwivedi, Y. K., Pandey, N., Currie, W. L., & Micu, A. (2023). Opinion paper: "So what if ChatGPT wrote it?" Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. *International Journal of Information Management, 71*, 102642. https://doi.org/10.1016/j.ijinfomgt.2023.102642

Doğru, T., Line, N., Mody, M., Hanks, L., Abbott, J., Açikgöz, N. N., Assaf, A., Bakir, S., Berbekova, A., Bilgihan, A., Dalton, A., Erkmen, E., Geronasso, A. H., Gomez, S., Graves, J., Iskender, İ., Ivanov, S., Kizildag, M., Lee, K., … Zhang, Y. (2025). Generative artificial intelligence in the hospitality and tourism industry: Developing a framework for future research. *Journal of Hospitality & Tourism Research, 49*(2), 235–253. https://doi.org/10.1177/10963480231188663

Duong, C. D., Nguyen, T. H., Ngo, T. T. A., Pham, V. H., Vu, T. T., & Dang, T. P. T. (2025). Using generative artificial intelligence (ChatGPT) for travel purposes: Parasocial interaction and tourists' continuance intention. *Tourism Review, 80*(4), 813–827. https://doi.org/10.1108/tr-01-2024-0027

Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2023). *GPTs are GPTs: An early look at the labor market impact potential of large language models*. arXiv. https://doi.org/10.48550/arxiv.2303.10130

Fallah Tafti, H. (2026). *Replication package: AI in tourism work* [Computer software]. GitHub. https://github.com/hamedf62/aei-tourism-paper

Felten, E., Raj, M., & Seamans, R. (2021). Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses. *Strategic Management Journal, 42*(12), 2195–2217. https://doi.org/10.1002/smj.3286

Knani, M., Echchakoui, S., & Ladhari, R. (2022). Artificial intelligence in tourism and hospitality: Bibliometric analysis and research agenda. *International Journal of Hospitality Management, 107*, 103317. https://doi.org/10.1016/j.ijhm.2022.103317

Frey, C. B., & Osborne, M. A. (2017). The future of employment: How susceptible are jobs to computerisation? *Technological Forecasting and Social Change, 114*, 254–280. https://doi.org/10.1016/j.techfore.2016.08.019

Gretzel, U., Sigala, M., Xiang, Z., & Koo, C. (2015). Smart tourism: Foundations and developments. *Electronic Markets, 25*(3), 179–188. https://doi.org/10.1007/s12525-015-0196-8

Ivanov, S., & Webster, C. (Eds.). (2019). *Robots, artificial intelligence and service automation in travel, tourism and hospitality*. Emerald. https://doi.org/10.1108/9781787566873

Knani, M., Echchakoui, S., & Ladhari, R. (2022). Artificial intelligence in tourism and hospitality: Bibliometric analysis and research agenda. *International Journal of Hospitality Management, 107*, 103317. https://doi.org/10.1016/j.ijhm.2022.103317

Nannelli, M., Capone, F., & Lazzeretti, L. (2023). Artificial intelligence in hospitality and tourism: State of the art and future research agenda. *European Planning Studies, 31*(7), 1325–1344. https://doi.org/10.1080/09654313.2023.2180321

Noll, B., Cason, T., Cheche, O. K., Brown, W., & Peet, E. (2025). *Artificial intelligence and the Anthropic Economic Index in the Mountain West*. University of Nevada, Las Vegas. https://www.unlv.edu

Pham, H. C., Duong, C. D., & Nguyen, G. K. H. (2024). What drives tourists' continuance intention to use ChatGPT for travel purposes? *Journal of Retailing and Consumer Services, 79*, 103758. https://doi.org/10.1016/j.jretconser.2024.103758

Stergiou, D. P., & Nella, A. (2024). ChatGPT and tourist decision-making: An accessibility–diagnosticity theory perspective. *International Journal of Tourism Research*. https://doi.org/10.1002/jtr.2757

Tussyadiah, I. (2020). A review of research into automation in tourism: Launching the Annals of Tourism Research Curated Collection on Artificial Intelligence and Tourism. *Annals of Tourism Research, 81*, 102883. https://doi.org/10.1016/j.annals.2020.102883

World Bank. (2025). *World Development Indicators* [Data set]. https://data.worldbank.org

World Travel & Tourism Council. (2025). *Travel & tourism economic impact research*. https://wttc.org/research/economic-impact

Yildirim, A. H. (2026). *The simple macroeconomics of AI: An empirical test using the Anthropic Economic Index*. SSRN. https://doi.org/10.2139/ssrn.6274118

---

## Tables

### Table 1. Global usage profiles of tourism-relevant detailed occupations (May 2026)

| Occupation | Share of global conversations (%) | Work-related share (%) | Automation (%) | Augmentation (%) | Human-only ability (%) | Mean AI autonomy (1–5) |
|---|---|---|---|---|---|---|
| Waiters and Waitresses | 0.17 | 2.8 | 59.9 | 40.1 | 99.5 | 2.73 |
| Food Service Managers | 0.13 | 33.7 | 52.0 | 48.0 | 95.9 | 2.86 |
| Meeting, Convention, and Event Planners | 0.12 | 75.8 | 36.6 | 63.4 | 83.7 | 3.03 |
| Recreation Workers | 0.11 | 41.1 | 53.7 | 46.3 | 95.3 | 2.70 |
| Reservation and Transportation Ticket Agents and Travel Clerks | 0.08 | 18.2 | 32.9 | 67.1 | 98.6 | 2.36 |
| Curators | 0.08 | 45.5 | 24.0 | 76.0 | 86.8 | 2.78 |
| Entertainment and Recreation Managers, Except Gambling | 0.06 | 53.0 | 38.8 | 61.2 | 96.7 | 2.94 |
| Tour Guides and Escorts | 0.03 | 26.6 | 64.1 | 35.9 | 98.4 | 2.69 |
| Lodging Managers | 0.03 | 39.0 | 61.1 | 38.9 | 95.2 | 2.74 |
| Baggage Porters and Bellhops | 0.01 | 28.4 | 73.9 | 26.1 | 98.5 | 2.78 |
| Chefs and Head Cooks | 0.01 | 24.4 | 39.6 | 60.4 | 95.4 | 2.75 |
| Travel Agents | 0.01 | 7.6 | 61.1 | 38.9 | 99.0 | 2.84 |
| Flight Attendants | 0.01 | 1.9 | 71.7 | 28.3 | 97.7 | 2.32 |
| Cooks, Restaurant | 0.01 | 14.1 | 71.5 | 28.5 | 98.1 | 2.59 |
| Concierges | 0.01 | 6.2 | 76.8 | 23.2 | 100.0 | 2.78 |
| Amusement and Recreation Attendants | 0.00 | 48.0 | 58.3 | 41.7 | 96.0 | 2.81 |
| Hotel, Motel, and Resort Desk Clerks | 0.00 | 7.1 | 42.3 | 57.7 | 98.9 | 2.60 |
| Museum Technicians and Conservators | 0.00 | 27.6 | 60.8 | 39.2 | 98.4 | 2.59 |
| Travel Guides | 0.00 | 3.7 | 69.9 | 30.1 | 98.5 | 2.87 |

*Notes:* Global-level AEI shares, May 2026. "Automation/Augmentation" are collaboration-bucket shares; "Human-only ability" is the share of conversations on tasks a human could complete without AI. Full data: `results/table1_tourism_occupations.csv` and `results/table5_detail_profiles.csv`.

### Table 2. Correlations between tourism SOC intensity and country characteristics

| Variable | r | 95% CI | n |
|---|---|---|---|
| Claude usage per-capita index | −0.36 | [−0.46, −0.26] | 113 |
| GDP per capita (log, US$) | −0.30 | [−0.41, −0.19] | 113 |
| Employment in services (% of employment) | −0.34 | [−0.50, −0.19] | 113 |
| Services value added (% of GDP) | −0.38 | [−0.52, −0.24] | 113 |
| Internet use (% of population) | −0.30 | [−0.51, −0.10] | 113 |
| Mobile subscriptions (per 100) | −0.29 | [−0.45, −0.12] | 113 |
| ICT service exports (% of service exports) | −0.17 | [−0.31, −0.03] | 111 |
| International arrivals per capita (log) | −0.21 | [−0.42, 0.01] | 107 |
| Tourism receipts per capita (log) | −0.27 | [−0.44, −0.10] | 99 |
| Unemployment (%) | +0.10 | [−0.09, 0.34] | 113 |
| Travel services (% of service exports) | +0.17 | [+0.04, +0.33] | 111 |

*Notes:* Pearson correlations with 2,000-replication bootstrap CIs. Full data: `results/table2_correlations.csv`.

### Table 3. OLS regressions: tourism SOC intensity on economic correlates

| | (1) | (2) | (3) | (4) | (5) |
|---|---|---|---|---|---|
| log GDP per capita | −0.108** | −0.138** | −0.163*** | −0.113* | −0.183** |
| | (0.023) | (0.041) | (0.033) | (0.045) | (0.054) |
| Internet use (%) | | 0.002 | | | 0.002 |
| | | (0.003) | | | (0.003) |
| log arrivals per capita | | | 0.044† | | 0.041 |
| | | | (0.026) | | (0.026) |
| Employment in services (%) | | | | 0.001 | −0.001 |
| | | | | (0.004) | (0.004) |
| Constant | 2.057*** | 2.159*** | 2.667*** | 2.073*** | 2.715*** |
| | (0.216) | (0.246) | (0.344) | (0.250) | (0.364) |
| N | 113 | 113 | 107 | 113 | 107 |
| R² | 0.166 | 0.172 | 0.226 | 0.166 | 0.231 |
| Adjusted R² | 0.158 | 0.157 | 0.211 | 0.151 | 0.200 |

*Notes:* Dependent variable: tourism SOC intensity (mean share of Food Preparation and Serving Related and Personal Care and Service groups in country-level Claude conversations, %). Heteroskedasticity-robust standard errors in parentheses. † p<0.10, * p<0.05, ** p<0.01, *** p<0.001.

### Table 4. Collaboration-bucket shares by SOC major group (selected)

| SOC major group | Augmentation (%) | Automation (%) | Tourism-relevant |
|---|---|---|---|
| Arts, Design, Entertainment, Sports, and Media | 64.2 | 35.9 | ✓ |
| Sales and Related | 56.2 | 43.8 | ✓ |
| Food Preparation and Serving Related | 50.9 | 49.1 | ✓ |
| Personal Care and Service | 44.1 | 55.9 | ✓ |
| Management (comparison) | 56.1 | 43.9 | |
| Computer and Mathematical (comparison) | 36.1 | 63.9 | |
| Office and Administrative Support (comparison) | 44.0 | 56.0 | |
| Transportation and Material Moving (comparison) | 48.3 | 51.7 | ✓ |

*Notes:* Global shares, May 2026. Full table: `results/table4_augmentation.csv`.

### Table 5. Three-period panel: growth, convergence, and the gradient reversal

| Panel | Statistic | Value | n |
|---|---|---|---|
| Growth | Mean tourism intensity, Aug 2025 → May 2026 | 0.25% → 0.84% (3.4×) | 12 |
| Convergence | β on initial level (growth regression) | −0.57 (t = −6.6) | 12 |
| Convergence | Leave-one-out range of β | [−0.61, −0.37] | 12 |
| Rank stability | Spearman ρ, Aug 2025 vs May 2026 | 0.87 | 12 |
| Gradient | β (log GDP pc), Aug 2025 | +0.09 (t = 3.2) | 12 |
| Gradient | β (log GDP pc), Apr 2026 | +0.01 (t = 1.5) | 64 |
| Gradient | β (log GDP pc), May 2026 | −0.01 (t = −1.0) | 77 |
| Early adopters | Mean log GDP pc (2025-08 entrants vs later) | 10.25 vs 9.53 | 12/65 |
| Decomposition | Within-country growth (pp) | +0.59 | 12 |

*Sources:* `results/panel2_*.csv`; AEI releases 2025-09-15 (Aug 2025 weekly snapshot), 2026-06-26 (Apr & May 2026).

---

## Figures

**Figure 1.** Claude usage by SOC major group, May 2026 (tourism-relevant groups in red). `figures/fig1_major_groups.png`

**Figure 2.** Tourism-occupation AI usage vs. economic development. `figures/fig2_gdp_scatter.png`

**Figure 3.** Economic correlates of tourism-occupation AI usage (correlations with 95% bootstrap CIs). `figures/fig3_forest.png`

**Figure 4.** Automation vs. augmentation by SOC major group, May 2026. `figures/fig4_automation.png`

**Figure 5.** Within-country trajectories of tourism-occupation AI usage, twelve-country panel (Aug 2025, Apr 2026, May 2026). `figures/fig5_trajectories.png`

**Figure 6.** β-convergence: growth vs initial level. `figures/fig6_convergence.png`

**Figure 7.** The cross-sectional income gradient by period: positive among early adopters, zero by April 2026, weakly negative in May 2026. `figures/fig7_gradient_by_period.png`

---

## Appendix A. Novelty search protocol

On August 27, 2026, the author searched OpenAlex (`api.openalex.org`), Google Scholar, SSRN, and arXiv with term combinations: ("Anthropic Economic Index" OR "Claude conversations" OR "Claude usage") AND ("tourism" OR "hospitality" OR "travel" OR "accommodation"); ("tourism" OR "hospitality") AND ("occupational exposure" OR "AI adoption" OR "generative AI") AND ("employment" OR "labor"); and title searches for all AEI-related works. OpenAlex title searches for "Anthropic Economic Index" returned 12 works (including preprints and near-duplicates); none concern tourism. Search strings and date-stamped outputs are stored in the replication repository (`review/novelty_search_log.md`).

## Appendix B. Robustness tables

Tables B1–B5 (alternative intensity definitions; top-5 exclusion; April-vs-May stability; winsorization, component-wise and population-weighted regressions; leave-one-out convergence) are generated by `code/07_robustness.py`, `code/13_supplementary_robustness.py`, and `code/25_panel_v4.py`, and stored in `results/` as `robustness_*.csv` and `panel2_*.csv`.

## Appendix C. Variable definitions and sources

| Variable | Definition | Source | Years |
|---|---|---|---|
| Tourism SOC intensity | Mean country share of conversations in Food Prep & Serving and Personal Care major groups | AEI | 2026-05 |
| Claude usage index | Usage share ÷ working-age population share | AEI | 2026-05 |
| GDP per capita | Current US$ | WDI NY.GDP.PCAP.CD | 2019–2024 (latest) |
| International arrivals | Tourist arrivals (count) | WDI ST.INT.ARVL | 2019–2024 (latest) |
| Tourism receipts | Current US$ | WDI ST.INT.RCPT.CD | 2019–2024 (latest) |
| Services employment | % of total employment (modeled ILO) | WDI SL.SRV.EMPL.ZS | 2019–2024 (latest) |
| Travel services | % of service exports (BoP) | WDI BX.GSR.TRVL.ZS | 2019–2024 (latest) |
| Internet use | % of population | WDI IT.NET.USER.ZS | 2019–2024 (latest) |
| Mobile subscriptions | Per 100 people | WDI IT.CEL.SETS.P2 | 2019–2024 (latest) |
| Unemployment | % of labor force (modeled ILO) | WDI SL.UEM.TOTL.ZS | 2019–2024 (latest) |
| Services value added | % of GDP | WDI NV.SRV.TOTL.ZS | 2019–2024 (latest) |
| ICT service exports | % of service exports (BoP) | WDI BX.GSR.CCIS.ZS | 2019–2024 (latest) |
