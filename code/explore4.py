import pandas as pd
df = pd.read_pickle('data/raw/aei.pkl')
# What soc codes exist in the dataset (global level-0 detail rows)? count and check coverage of tourism-relevant codes
det = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==0)]
codes = det[det.metric_id=='pct'].node_external_id.unique()
print("n unique detailed SOC codes:", len(codes))
tour_codes = ['35-3031','11-9081','39-7011','39-7012','41-3041','43-4181','53-2031','39-6012','39-6011','35-1011','35-2014','11-9051','13-1121','25-4012','11-9072','39-9032','43-4081','39-3091']
print("tour codes present:", [c for c in tour_codes if any(c in x for x in codes)])
# check country-level detail availability: is 'pct' at level 0 for countries available?
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country') & (df.hierarchy_level==0)]
print("country detail rows:", len(soc), "| n countries:", soc.geo_id.nunique())
print("metrics for country detail:", soc.metric_id.value_counts().to_dict())
# work pct by country overall
w = df[(df.category_name=='overall')&(df.geo_level=='country')&(df.metric_id=='use_case_work_pct')&(df.date_start=='2026-05-01')]
print("n countries work_pct:", w.geo_id.nunique())
print(w[['geo_id','value']].sort_values('value',ascending=False).head(10).to_string(index=False))
# automation/augmentation by major group globally
aug = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==1)&(df.metric_id.isin(['collaboration_bucket_automation_pct','collaboration_bucket_augmentation_pct']))&(df.date_start=='2026-05-01')]
p = aug.pivot_table(index='node_name', columns='metric_id', values='value')
print(p.sort_values('collaboration_bucket_automation_pct', ascending=False).to_string())
