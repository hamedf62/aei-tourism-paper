"""Round 3 fixes:
- Recompute Table 2 arrivals/receipts correlations on LOG variables (match text labels)
- Extract full metric profile for all 19 tourism occupations from raw AEI (fill Table 1 dashes)
- Global benchmark: mean AI autonomy across all 718 detailed occupations
- Global shares for Sales and Related / Personal Care (May 2026) exact values
"""
import pandas as pd, numpy as np

df = pd.read_pickle('data/raw/aei.pkl')
P='data/processed'; R='results'
MAY='2026-05-01'

# ---------- 1. Table 2 rows on log variables ----------
panel = pd.read_csv(f'{P}/panel.csv').dropna(subset=['tour_soc_mean'])
panel['log_arrivals_pc'] = np.log(panel['arrivals_pc'].clip(lower=1e-4))
panel['log_receipts_pc'] = np.log(panel['tour_receipts_pc'].clip(lower=1e-4))

def corr_ci(x, y, n_boot=2000, seed=42):
    d = pd.concat([x, y], axis=1).dropna()
    r = d.iloc[:,0].corr(d.iloc[:,1])
    rng = np.random.default_rng(seed)
    boots = [d.sample(len(d), replace=True, random_state=int(rng.integers(0,1e9))).corr().iloc[0,1] for _ in range(n_boot)]
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return r, lo, hi, len(d)

t2 = pd.read_csv(f'{R}/table2_correlations.csv')
for v, lab in [('log_arrivals_pc','arrivals_pc'), ('log_receipts_pc','tour_receipts_pc')]:
    r, lo, hi, n = corr_ci(panel['tour_soc_mean'], panel[v])
    idx = t2.index[t2.variable==lab]
    t2.loc[idx, ['r','ci_lo','ci_hi','n']] = [r, lo, hi, n]
    print(lab, "-> log:", round(r,3), [round(lo,2), round(hi,2)], "n=", n)
t2.to_csv(f'{R}/table2_correlations.csv', index=False)

# ---------- 2. Full profiles for 19 tourism occupations ----------
tour_names = [
 'Travel Agents','Tour Guides and Escorts','Travel Guides','Flight Attendants','Concierges',
 'Hotel, Motel, and Resort Desk Clerks','Lodging Managers','Food Service Managers',
 'Chefs and Head Cooks','Cooks, Restaurant','Waiters and Waitresses',
 'Reservation and Transportation Ticket Agents and Travel Clerks',
 'Meeting, Convention, and Event Planners','Amusement and Recreation Attendants',
 'Recreation Workers','Baggage Porters and Bellhops',
 'Entertainment and Recreation Managers, Except Gambling','Curators','Museum Technicians and Conservators']
det = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==0)&(df.date_start==MAY)]
METRICS = ['pct','use_case_work_pct','collaboration_bucket_automation_pct','collaboration_bucket_augmentation_pct','human_only_ability_pct','ai_autonomy_mean']
sub = det[det.node_name.isin(tour_names) & det.metric_id.isin(METRICS)]
pt = sub.pivot_table(index='node_name', columns='metric_id', values='value', aggfunc='first')
pt = pt.sort_values('pct', ascending=False)
pt.index.name='occupation'; pt.columns.name=None
pt = pt.reset_index().rename(columns={'pct':'global_pct'})
pt.to_csv(f'{R}/table5_detail_profiles.csv', index=False)
print("\nfull profiles n rows:", len(pt))
print(pt.to_string(index=False))

# ---------- 3. Global autonomy benchmark over all 718 detail occupations ----------
aut_all = det[det.metric_id=='ai_autonomy_mean']
print("\nglobal detail-occupation autonomy mean:", round(aut_all['value'].mean(),3),
      "| median:", round(aut_all['value'].median(),3), "| n occs:", aut_all['node_name'].nunique())
# percentile ranks for tourism occupations
def pct_rank(v):
    return round(100*(aut_all['value'] < v).mean(),1)
for occ in ['Waiters and Waitresses','Concierges','Travel Agents','Flight Attendants','Meeting, Convention, and Event Planners','Curators','Lodging Managers']:
    v = pt.loc[pt.occupation==occ,'ai_autonomy_mean']
    if len(v):
        ho = det[(det.node_name==occ)&(det.metric_id=='human_only_ability_pct')]['value']
        hv = ho.iloc[0] if len(ho) else np.nan
        print(occ, "| autonomy:", round(v.iloc[0],2), "| percentile:", pct_rank(v.iloc[0]), "| human-only:", hv)

# human-only percentile for Waiters (target top-decile check)
ho_all = det[det.metric_id=='human_only_ability_pct'].dropna(subset=['value'])
w = det[(det.node_name=='Waiters and Waitresses')&(det.metric_id=='human_only_ability_pct')]['value'].iloc[0]
print("\nhuman-only percentile (Waiters):", round(100*(ho_all['value']<w).mean(),1), "| n occs:", ho_all['node_name'].nunique())

# ---------- 4. Exact global group shares ----------
g = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start==MAY)]
gs = g.groupby('node_name')['value'].mean()
for k in ['Sales and Related','Personal Care and Service','Food Preparation and Serving Related','Arts, Design, Entertainment, Sports, and Media','Transportation and Material Moving']:
    print(k, "=", round(gs[k],2))
