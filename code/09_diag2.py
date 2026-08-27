import pandas as pd, numpy as np
# The mean is dominated by Personal Care (which has more published cells, n=113 vs Food n=77).
# That explains B1_sum n=78. Diagnose per-variable availability and correlation with the mean.
p = pd.read_csv('data/processed/panel.csv')
print("tour_soc_mean nonnull:", p['tour_soc_mean'].notna().sum())
# how many countries have both Food & Personal published?
df = pd.read_pickle('data/raw/aei.pkl')
soc = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start=='2026-05-01')]
mg = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
both = mg[['Food Preparation and Serving Related','Personal Care and Service']].dropna()
print("countries with BOTH groups published:", len(both))
p2 = p.set_index('iso3').join(both, how='inner')
print("both-sample corr with log gdp:", round(p2['tour_soc_mean'].corr(np.log(p2['gdp_pc'])),3))
# corr of mean with each component
d = p.set_index('iso3').join(mg, how='inner')
print("mean vs Food r:", round(d['tour_soc_mean'].corr(d['Food Preparation and Serving Related']),3))
print("mean vs Personal r:", round(d['tour_soc_mean'].corr(d['Personal Care and Service']),3))
