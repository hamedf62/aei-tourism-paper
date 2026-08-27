import pandas as pd
df = pd.read_pickle('data/raw/aei.pkl')
# global detailed occupation pct values for tourism SOC codes
det = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==0) & (df.metric_id=='pct')]
tour_names = [
 'Travel Agents','Tour Guides and Escorts','Travel Guides','Flight Attendants','Concierges',
 'Hotel, Motel, and Resort Desk Clerks','Lodging Managers','Food Service Managers',
 'Chefs and Head Cooks','Cooks, Restaurant','Waiters and Waitresses','Reservation and Transportation Ticket Agents and Travel Clerks',
 'Meeting, Convention, and Event Planners','Amusement and Recreation Attendants','Recreation Workers',
 'Baggage Porters and Bellhops','Entertainment and Recreation Managers, Except Gambling','Curators','Museum Technicians and Conservators']
sub = det[det.node_name.isin(tour_names)].sort_values('value', ascending=False)
print(sub[['node_name','value','node_external_id']].to_string(index=False))
print()
# overall global metrics
ov = df[(df.category_name=='overall') & (df.geo_level=='global')]
m = ov[ov.date_start=='2026-05-01'].set_index('metric_id').value
for k in ['use_case_work_pct','use_case_personal_pct','use_case_coursework_pct','collaboration_bucket_automation_pct','collaboration_bucket_augmentation_pct','human_only_ability_pct']:
    print(k, m.get(k))
# check a few countries for usage_per_capita_index + a share of tourism SOC
print()
upi = df[(df.category_name=='overall')&(df.geo_level=='country')&(df.metric_id=='usage_per_capita_index')&(df.date_start=='2026-05-01')]
print("n countries with UPI May2026:", upi.geo_id.nunique())
print(upi[['geo_id','value']].sort_values('value',ascending=False).head(15).to_string(index=False))
