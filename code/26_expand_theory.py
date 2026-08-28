"""Expand sections 1-3 with theoretical deepening for full Q1 length.
Adds: human-capital/task-complementarity framework, skill-biased adoption prediction,
and detailed data-construction notes. Then verifies word count.
"""
import re

md = open('manuscript/manuscript.md').read()

# --- Insert theory deepening at end of section 2.4 ---
theory_add = """
The two framings generate testable predictions that organize the empirical work. From the diffusion-composition distinction: (P1) cross-sectional gradients in occupational AI shares should track the *adopter composition* of the platform rather than stable economic structure, and should therefore shift systematically as the platform's country footprint broadens; (P2) early-adopter countries should differ from later entrants in income and overall usage intensity. From the automation-augmentation distinction: (P3) occupations whose output is codifiable (schedules, templated communications, itineraries) should show automation-leaning collaboration profiles, while interpretation- and relationship-intensive tasks should show human-only profiles; (P4) front-line service occupations should rank high on human-only ability even where their usage share is nonzero, because their core tasks resist codification. A fifth prediction follows from diffusion economics generally: (P5) levels of a new technology's use should converge across adopters as the technology matures, with growth rates inversely related to initial levels (β-convergence). The three-period panel (Section 4.6) tests P1, P2, and P5 directly; the task-level metrics test P3 and P4."""

md = md.replace(
 """A fifth prediction follows""", """A fifth prediction follows""")  # no-op guard

md = md.replace(
 """The AEI's task-level metrics allow this decomposition without any survey instrument.""",
 """The AEI's task-level metrics allow this decomposition without any survey instrument.""" + theory_add)

# --- Add mechanism paragraph to 4.6 already present; add data-construction note to 3.1 ---
data_add = """
*Release history and schema harmonization.* The AEI's earlier releases used a weekly-snapshot schema (occupation facet at level 0 with `soc_pct` variables); the mid-2026 releases moved to a monthly, metric-based schema with major groups at hierarchy level 1. The intermediate releases (November 2025, February 2026) do not publish occupation facets for countries and cannot enter the panel. Two schema generations therefore supply the three usable periods: August 2025 (17 countries with both tourism groups published), April 2026 (65), and May 2026 (78). Because the 2025 schema shares sum across classified conversations only, levels are not directly comparable to 2026 levels; all cross-period statements in this paper are therefore within-country statements (growth, convergence, gradient reversal), which are scale-invariant, and the 12-country balanced panel is the estimation sample for all longitudinal statistics."""
md = md.replace(
 """### 3.2 Tourism indicators""",
 data_add + "\n\n### 3.2 Tourism indicators")

open('manuscript/manuscript.md','w').write(md)
print("inserted. new word count:", len(md.split()))
