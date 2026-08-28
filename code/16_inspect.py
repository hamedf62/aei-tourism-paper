import pandas as pd
d = pd.read_csv('data/raw/history/aei_2025-08.csv', engine='c', nrows=50000, usecols=['geo_id','facet','level','variable','cluster_name','value'])
soc = d[(d.facet=='soc_occupation') & (d.variable=='soc_pct')]
print("level0 rows:", len(soc))
print(soc.cluster_name.dropna().unique()[:25])
names = soc.cluster_name.dropna().unique()
mg = [c for c in names if 'Related' in str(c) or 'Service' in str(c)]
print("group-like:", mg[:10])
