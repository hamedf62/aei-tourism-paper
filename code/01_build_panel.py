"""Build the country-level analysis panel:
- AEI country-level AI usage (May 2026 release) by SOC major group + overall metrics
- World Bank WDI economic/tourism indicators
Outputs: data/processed/panel.csv + summary CSVs.
"""
import urllib.request, json, time
import pandas as pd

RAW = 'data/raw/aei.pkl'
OUT = 'data/processed'

df = pd.read_pickle(RAW)
MAY = '2026-05-01'

# ---------- 1. AEI country variables ----------
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='country') & (df.hierarchy_level==1) & (df.date_start==MAY)]
mg_pivot = soc[soc.metric_id=='pct'].pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')

# Tourism & hospitality related SOC major groups (2-digit groupings that map to tourism work):
TOUR_MG = {
    'Food Preparation and Serving Related': 'food_serving',
    'Personal Care and Service': 'personal_care',
    'Arts, Design, Entertainment, Sports, and Media': 'arts_media',
    'Sales and Related': 'sales',
    'Transportation and Material Moving': 'transport',
    'Office and Administrative Support': 'office_admin',
}
tour_cols = {}
for name, short in TOUR_MG.items():
    if name in mg_pivot.columns:
        tour_cols[short] = mg_pivot[name]

# Tourism work intensity: mean of the two most tourism-typical groups
tour = pd.DataFrame(tour_cols)
tour['tour_soc_mean'] = tour[['food_serving','personal_care']].mean(axis=1)

# Detailed tourism occupations at global level (level 0) for occupation profiles
det = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==0) & (df.date_start==MAY)]
det_pct = det[det.metric_id=='pct'].set_index('node_name')['value']

# Overall country metrics
ov = df[(df.category_name=='overall') & (df.geo_level=='country') & (df.date_start==MAY)]
ov_pivot = ov.pivot_table(index='geo_id', columns='metric_id', values='value', aggfunc='first')

aei = pd.concat([tour, ov_pivot], axis=1)
aei.index.name = 'iso3'
aei = aei.reset_index()
print("AEI countries:", len(aei))

# ---------- 2. World Bank indicators ----------
INDICATORS = {
    'ST.INT.ARVL': 'arrivals',
    'ST.INT.RCPT.CD': 'tour_receipts',
    'NY.GDP.PCAP.CD': 'gdp_pc',
    'SP.POP.TOTL': 'population',
    'SL.SRV.EMPL.ZS': 'services_emp',
    'BX.GSR.TRVL.ZS': 'travel_exp_share',
    'IT.NET.USER.ZS': 'internet_users',
    'IT.CEL.SETS.P2': 'mobile_subs',
    'SP.POP.1564.TO.ZS': 'working_age_share',
    'SL.UEM.TOTL.ZS': 'unemployment',
    'NV.SRV.TOTL.ZS': 'services_va',
    'BX.GSR.CCIS.ZS': 'ict_exports',
    'NY.GDP.MKTP.KD.ZG': 'gdp_growth',
    'VC.IHR.PSRC.P5': 'homicides',
}
wb_rows = {}
for code, short in INDICATORS.items():
    url = f'http://api.worldbank.org/v2/country/all/indicator/{code}?format=json&per_page=20000&date=2019:2024'
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                d = json.loads(r.read())
            break
        except Exception as e:
            print('retry', code, e); time.sleep(3)
    else:
        print('FAIL', code); continue
    rows = d[1] or []
    recs = {}
    for x in rows:
        if x['value'] is None: continue
        iso3 = x['countryiso3code']
        if not iso3: continue
        # prefer most recent year per country
        if iso3 not in recs or int(x['date']) > int(recs[iso3][0]):
            recs[iso3] = (x['date'], x['value'])
    wb_rows[short] = {k: v[1] for k, v in recs.items()}
    print(code, short, 'countries:', len(recs))
    time.sleep(0.4)

wb = pd.DataFrame(wb_rows)
wb.index.name = 'iso3'
wb = wb.reset_index()

# arrivals per capita
arr = wb.set_index('iso3')
arr['arrivals_pc'] = arr['arrivals'] / (arr['population'] * 1000) if arr['population'].dtype != 'float64' else arr['arrivals'] / arr['population']
# population scale: arrivals are counts, population is counts too
arr['arrivals_pc'] = arr['arrivals'] / arr['population']
arr['tour_receipts_pc'] = arr['tour_receipts'] / arr['population']
wb = arr.reset_index()

# ---------- 3. Merge ----------
panel = aei.merge(wb, on='iso3', how='inner')
print("merged panel:", len(panel))
panel.to_csv(f'{OUT}/panel.csv', index=False)
aei.to_csv(f'{OUT}/aei_only.csv', index=False)
wb.to_csv(f'{OUT}/wb_only.csv', index=False)

# Global detail-occupation shares for Table 1
det_pct.reset_index().rename(columns={'value':'global_pct','node_name':'occupation'}).to_csv(f'{OUT}/global_occupation_shares.csv', index=False)

# Automation vs augmentation by major group (global)
aug = df[(df.category_name=='soc_occupation')&(df.geo_level=='global')&(df.hierarchy_level==1)&
         (df.metric_id.isin(['collaboration_bucket_automation_pct','collaboration_bucket_augmentation_pct']))&(df.date_start==MAY)]
p = aug.pivot_table(index='node_name', columns='metric_id', values='value').reset_index()
p.to_csv(f'{OUT}/augmentation_by_major_group.csv', index=False)

print(panel[['iso3','tour_soc_mean','usage_per_capita_index','gdp_pc','arrivals_pc']].describe().to_string())
