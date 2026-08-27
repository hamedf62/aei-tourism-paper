"""Regenerate manuscript Table 1 markdown from the filled table5_detail_profiles.csv."""
import pandas as pd

pt = pd.read_csv('results/table5_detail_profiles.csv')

def fmt(v, dec=2):
    return "—" if pd.isna(v) else f"{v:.{dec}f}"

lines = ["| Occupation | Share of global conversations (%) | Work-related share (%) | Automation (%) | Augmentation (%) | Human-only ability (%) | Mean AI autonomy (1–5) |",
         "|---|---|---|---|---|---|---|"]
for _, r in pt.iterrows():
    lines.append(f"| {r['occupation']} | {r['global_pct']:.2f} | {fmt(r['use_case_work_pct'],1)} | {fmt(r['collaboration_bucket_automation_pct'],1)} | {fmt(r['collaboration_bucket_augmentation_pct'],1)} | {fmt(r['human_only_ability_pct'],1)} | {fmt(r['ai_autonomy_mean'])} |")

table = "\n".join(lines)
open('results/table1_markdown.md','w').write(table)
print(table)
