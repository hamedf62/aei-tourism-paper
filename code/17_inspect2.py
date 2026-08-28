import pandas as pd
# Why do 2025-11 and 2026-02 fail? Inspect soc_occupation rows in those files
d = pd.read_csv('data/raw/history/aei_2025-11.csv', engine='c', nrows=100000,
                usecols=['geo_id','facet','level','variable','cluster_name','value'], on_bad_lines='skip')
soc = d[d.facet=='soc_occupation']
print("2025-11 soc rows:", len(soc))
print("levels:", soc.level.value_counts().to_dict() if len(soc) else "none")
print("variables:", soc.variable.value_counts().head(8).to_dict() if len(soc) else "none")
if len(soc):
    print("clusters sample:", soc.cluster_name.dropna().unique()[:10])
