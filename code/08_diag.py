import pandas as pd, numpy as np
df = pd.read_pickle('data/raw/aei.pkl')
panel = pd.read_csv('data/processed/panel.csv')
soc = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start=='2026-05-01')]
mg = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
p = panel.set_index('iso3').join(mg, how='inner')
print("n joint:", len(p))
for c in ['Food Preparation and Serving Related','Personal Care and Service','Sales and Related','Arts, Design, Entertainment, Sports, and Media']:
    print(c, "| r with log gdp:", round(p[c].corr(np.log(p['gdp_pc'])),3))
print("missing Food:", p['Food Preparation and Serving Related'].isna().sum(), "missing Personal:", p['Personal Care and Service'].isna().sum())
# n=78 in B1_sum vs 113: panel.csv tour_soc_mean dropna 113, but Food col may have more missing than Personal.
print("panel rows:", len(panel), "| tour_soc_mean nonnull:", panel['tour_soc_mean'].notna().sum())
