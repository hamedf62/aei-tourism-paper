import pandas as pd
# What facets exist in 2025-11 file?
d = pd.read_csv('data/raw/history/aei_2025-11.csv', engine='c', nrows=300000,
                usecols=['facet','level','variable','cluster_name'], on_bad_lines='skip')
print("facets:", d.facet.value_counts().head(15).to_dict())
# maybe soc is under a different facet name like 'occupation'
occ = d[d.facet.str.contains('occ', case=False, na=False)]
print("\nocc facet rows:", len(occ), "| levels:", occ.level.value_counts().to_dict() if len(occ) else '-')
if len(occ):
    print("variables:", occ.variable.value_counts().head(8).to_dict())
    print("clusters:", occ.cluster_name.dropna().unique()[:8])
