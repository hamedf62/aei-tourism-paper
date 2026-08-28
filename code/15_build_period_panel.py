"""Build the country-period panel — weekly schema has major groups at level 0 with variable soc_pct."""
import pandas as pd, numpy as np, os

RAW = 'data/raw/history'
OUT = 'data/processed'
TOUR_MG = ['Food Preparation and Serving Related', 'Personal Care and Service']

def load_weekly(path, period):
    chunks = []
    for chunk in pd.read_csv(path, engine='c', chunksize=500_000, low_memory=False,
                             usecols=['geo_id','facet','level','variable','cluster_name','value'],
                             on_bad_lines='skip'):
        m = chunk[(chunk.facet=='soc_occupation') & (chunk.level==0) &
                  (chunk.variable=='soc_pct') & (chunk.cluster_name.isin(TOUR_MG))]
        if len(m):
            chunks.append(m[['geo_id','cluster_name','value']])
    if not chunks:
        return pd.DataFrame(columns=['geo_id','tour_soc_mean'])
    d = pd.concat(chunks, ignore_index=True)
    d['value'] = pd.to_numeric(d['value'], errors='coerce')
    g = d.dropna().groupby('geo_id')['value'].mean().rename('tour_soc_mean').reset_index()
    g['period'] = period
    return g

frames = []
for tag, per in [('2025-08','2025-08'), ('2025-11','2025-11'), ('2026-02','2026-02')]:
    p = f'{RAW}/aei_{tag}.csv'
    if os.path.exists(p):
        g = load_weekly(p, per)
        print(per, 'loaded:', len(g), 'countries')
        frames.append(g)

if os.path.exists('data/raw/aei.pkl'):
    df = pd.read_pickle('data/raw/aei.pkl')
    for per, ds in [('2026-04','2026-04-01'), ('2026-05','2026-05-01')]:
        soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country') & (df.hierarchy_level==1) & (df.metric_id=='pct') & (df.date_start==ds)]
        mg = soc[soc.node_name.isin(TOUR_MG)]
        g = mg.groupby('geo_id')['value'].mean().rename('tour_soc_mean').rename_axis('geo_id').reset_index()
        g['period'] = per
        frames.append(g)
        print(per, 'loaded:', len(g), 'countries')

panel = pd.concat(frames, ignore_index=True)
panel = panel[panel.tour_soc_mean.notna() & (panel.geo_id.str.len()==3)]
panel.to_csv(f'{OUT}/tour_panel_periods.csv', index=False)
print("\nPanel summary:")
print(panel.groupby('period')['tour_soc_mean'].agg(['count','mean','std','min','max']).round(3).to_string())
cnt = panel.groupby('geo_id').size()
print("\ncountries in all 5 periods:", (cnt==5).sum(), "| in >=4:", (cnt>=4).sum(), "| total:", len(cnt))
