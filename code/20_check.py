import pandas as pd
# 2025-11 has NO soc facet at all (pre-SOC release). Same check for 2026-02, and 2025-08 availability stats.
import os
for f in ['aei_2026-02.csv']:
    allf=set()
    for chunk in pd.read_csv(f'data/raw/history/{f}', engine='c', chunksize=1_000_000,
                             usecols=['facet'], on_bad_lines='skip', low_memory=False):
        allf.update(chunk.facet.dropna().unique())
    soc_ok = any('soc' in x.lower() for x in allf)
    print(f, "has soc:", soc_ok)

# 2025-08: how many countries have both tourism groups? (loaded 25 but only 16 mean-values)
d = pd.read_csv('data/raw/history/aei_2025-08.csv', engine='c', low_memory=False,
                usecols=['geo_id','facet','level','variable','cluster_name','value'], on_bad_lines='skip')
m = d[(d.facet=='soc_occupation') & (d.level==0) & (d.variable=='soc_pct') & (d.cluster_name.isin(['Food Preparation and Serving Related','Personal Care and Service']))]
g = m.groupby('geo_id').cluster_name.nunique()
print("\n2025-08: countries with 2 groups:", (g==2).sum(), "| with 1:", (g==1).sum())
# what are value magnitudes
print(m.groupby('cluster_name')['value'].describe().round(3).to_string())
