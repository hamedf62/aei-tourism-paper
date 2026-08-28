"""Final period panel builder — corrected understanding:
- 2025-08 (Aug 2025 weekly): soc at level 0, variable=soc_pct, group shares are the SOC major group share
  of that week's classified conversations. Note: 2025 schema shares may be scaled differently
  (values ~0.2-0.6 vs 2026 ~1.0) because 'not_classified' and different normalization. Investigate & harmonize.
- 2025-11 & 2026-02 releases: NO soc facet — cannot use for occupation panel.
- 2026-04, 2026-05: monthly schema (metric pct, level 1).

=> Usable occupation panel: T=3 periods (2025-08, 2026-04, 2026-05), with harmonization check.
"""
import pandas as pd, numpy as np, os

RAW = 'data/raw/history'
OUT = 'data/processed'
TOUR_MG = ['Food Preparation and Serving Related', 'Personal Care and Service']

# --- 2025-08 weekly ---
d = pd.read_csv(f'{RAW}/aei_2025-08.csv', engine='c', low_memory=False,
                usecols=['geo_id','facet','level','variable','cluster_name','value'], on_bad_lines='skip')
m = d[(d.facet=='soc_occupation') & (d.level==0) & (d.variable=='soc_pct') & (d.cluster_name.isin(TOUR_MG))]
g8 = m.groupby(['geo_id','cluster_name'])['value'].mean().unstack()
g8.columns = ['food','personal']
g8['tour_soc_mean'] = g8[['food','personal']].mean(axis=1)
g8 = g8[g8[['food','personal']].notna().all(axis=1)].reset_index().rename(columns={'geo_id':'iso3'})
g8['period'] = '2025-08'
print("2025-08:", len(g8), "countries with both groups")

# --- monthly (existing pickle) ---
frames = [g8[['iso3','period','tour_soc_mean','food','personal']]]
if os.path.exists('data/raw/aei.pkl'):
    df = pd.read_pickle('data/raw/aei.pkl')
    for per, ds in [('2026-04','2026-04-01'), ('2026-05','2026-05-01')]:
        soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country') & (df.hierarchy_level==1) & (df.metric_id=='pct') & (df.date_start==ds)]
        mg = soc[soc.node_name.isin(TOUR_MG)]
        p = mg.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
        p.columns = ['food','personal']
        p['tour_soc_mean'] = p.mean(axis=1)
        p = p[p[['food','personal']].notna().all(axis=1)].reset_index().rename(columns={'geo_id':'iso3'})
        p['period'] = per
        frames.append(p[['iso3','period','tour_soc_mean','food','personal']])
        print(per, ":", len(p), "countries with both groups")

panel = pd.concat(frames, ignore_index=True)
panel.to_csv(f'{OUT}/tour_period_panel.csv', index=False)

print("\n=== Harmonization check: scale of shares across periods ===")
print(panel.groupby('period')[['food','personal','tour_soc_mean']].describe().T.round(3).to_string())

# within-country continuity: countries in both 2025-08 and 2026-05
w = panel.pivot_table(index='iso3', columns='period', values='tour_soc_mean')
both = w[['2025-08','2026-05']].dropna()
print("\ncountries in both 2025-08 and 2026-05:", len(both))
if len(both) > 3:
    print("correlation 2025-08 vs 2026-05:", round(both['2025-08'].corr(both['2026-05']), 3))
    print("mean ratio 2026-05 / 2025-08:", round((both['2026-05']/both['2025-08']).median(), 2))
print("\ncountries per period:")
print(panel.groupby('period').size().to_string())
