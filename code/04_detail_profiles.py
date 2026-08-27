import pandas as pd
d = pd.read_csv('results/table1_tourism_occupations.csv')
print(d.to_string(index=False))
aug = pd.read_csv('results/table4_augmentation.csv')
print(aug[aug.tourism_flag][['node_name','collaboration_bucket_augmentation_pct','collaboration_bucket_automation_pct']].to_string(index=False))
df = pd.read_pickle('data/raw/aei.pkl')
det = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==0)&(df.date_start=='2026-05-01')]
keys = ['Waiters and Waitresses','Travel Agents','Tour Guides and Escorts','Hotel, Motel, and Resort Desk Clerks','Lodging Managers','Flight Attendants','Concierges','Food Service Managers','Chefs and Head Cooks','Cooks, Restaurant','Reservation and Transportation Ticket Agents and Travel Clerks','Meeting, Convention, and Event Planners']
sub = det[det.node_name.isin(keys) & det.metric_id.isin(['pct','collaboration_bucket_automation_pct','collaboration_bucket_augmentation_pct','human_only_ability_pct','ai_autonomy_mean','use_case_work_pct','multitasking_pct'])]
pt = sub.pivot_table(index='node_name', columns='metric_id', values='value', aggfunc='first')
pt = pt.sort_values('pct', ascending=False)
print(pt.to_string())
pt.reset_index().to_csv('results/table5_detail_profiles.csv', index=False)
