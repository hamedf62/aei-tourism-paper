import pandas as pd, numpy as np
df = pd.read_pickle('data/raw/aei.pkl')
p = pd.read_csv('data/processed/panel.csv')
soc = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start=='2026-05-01')]
mg = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
p = p.set_index('iso3')
mg = mg.join(p['tour_soc_mean'], how='inner')
know = mg[['Computer and Mathematical','Management','Business and Financial Operations']].sum(axis=1)
print("corr tour_soc vs knowledge groups:", round(mg['tour_soc_mean'].corr(know),3))
ov = df[(df.category_name=='overall')&(df.geo_level=='country')&(df.metric_id=='usage_pct')&(df.date_start=='2026-05-01')]
share = ov.set_index('geo_id')['value']
mg2 = mg.join(share.rename('global_share'), how='inner')
mg2['tour_abs'] = mg2['global_share']*mg2['tour_soc_mean']/100
p2 = p.join(mg2[['tour_abs']], how='inner')
print("corr tour_abs vs log gdp_pc:", round(mg2['tour_abs'].corr(np.log(p2['gdp_pc'])),3))
print("n:", len(p2))
print("corr usage index vs log gdp:", round(p2['usage_per_capita_index'].corr(np.log(p2['gdp_pc'])),3))
