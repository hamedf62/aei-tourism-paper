import pandas as pd
df = pd.read_pickle('data/raw/aei.pkl')
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country')]
print("soc country rows:", len(soc))
print("levels:", soc.hierarchy_level.value_counts().to_dict())
print("metrics:", soc.metric_id.value_counts().to_dict())
mg = soc[soc.hierarchy_level==1]
print(list(mg.node_name.unique())[:30])
ov = df[(df.category_name=='overall') & (df.geo_level=='country')]
print("overall country metrics:", list(ov.metric_id.unique()))
print("n countries overall:", ov.geo_id.nunique())
gl = df[(df.category_name=='soc_occupation') & (df.geo_level=='global')]
print("soc global metrics:", list(gl.metric_id.unique()), "levels:", gl.hierarchy_level.value_counts().to_dict())
