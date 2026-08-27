"""Check human-only percentile for the front-line hospitality occupations cited in the paper."""
import pandas as pd, numpy as np
df = pd.read_pickle('data/raw/aei.pkl')
det = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==0)&(df.date_start=='2026-05-01')]
ho_all = det[det.metric_id=='human_only_ability_pct'].dropna(subset=['value'])
for occ in ['Waiters and Waitresses','Concierges','Travel Agents','Flight Attendants','Tour Guides and Escorts','Meeting, Convention, and Event Planners','Curators','Lodging Managers','Food Service Managers']:
    v = det[(det.node_name==occ)&(det.metric_id=='human_only_ability_pct')]['value']
    if len(v):
        print(occ, round(v.iloc[0],2), "-> percentile:", round(100*(ho_all['value']<v.iloc[0]).mean(),1))
print("n occs:", ho_all['node_name'].nunique())
