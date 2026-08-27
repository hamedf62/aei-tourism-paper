import pandas as pd
df = pd.read_pickle('data/raw/aei.pkl')
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country') & (df.hierarchy_level==1)]
piv = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
cols = ['Food Preparation and Serving Related','Personal Care and Service','Sales and Related','Arts, Design, Entertainment, Sports, and Media','Accommodation','Travel']
for c in cols:
    if c in piv.columns:
        print(c, "| n countries:", piv[c].notna().sum(), "| median:", round(piv[c].median(),3), "| max:", piv[c].idxmax(), round(piv[c].max(),2))
print()
# detailed occupations (level 0) global — search tourism-related
det = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==0) & (df.metric_id=='pct')]
names = det.node_name.unique()
kw = ['travel','tour','accommodat','hotel','lodging','food','chef','cook','waiter','server','guide','flight attend','concierge','reservation','transportation','recreation','gaming','leisure','event','museum','curator','baggage','tour']
hits = sorted(set(n for n in names if any(k in n.lower() for k in kw)))
print(len(hits), "tourism-related detailed occupations:")
for h in hits: print(" -", h)
