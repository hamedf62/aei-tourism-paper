"""Round 7 — supplementary robustness: winsorized + population-weighted + component-wise regressions."""
import pandas as pd, numpy as np

P='data/processed'; R='results'
df = pd.read_pickle('data/raw/aei.pkl')
panel = pd.read_csv(f'{P}/panel.csv').dropna(subset=['tour_soc_mean'])
soc = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start=='2026-05-01')]
mg = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
mg.columns=[c.replace(' ','_') for c in mg.columns]
panel = panel.merge(mg.reset_index().rename(columns={'geo_id':'iso3'}), on='iso3', how='left')
panel['log_gdp_pc'] = np.log(panel['gdp_pc'])

def ols(d, vs, y='tour_soc_mean'):
    d = d.dropna(subset=vs+[y])
    X = np.column_stack([np.ones(len(d))]+[d[v].values for v in vs])
    yv = d[y].values
    beta,*_ = np.linalg.lstsq(X,yv,rcond=None)
    resid = yv - X@beta
    n,k = X.shape
    se = np.sqrt(np.diag(np.linalg.inv(X.T@X))*(resid@resid/(n-k)))
    yhat = X@beta
    r2 = 1-((yv-yhat)**2).sum()/((yv-yv.mean())**2).sum()
    return dict(beta=beta[1], se=se[1], t=beta[1]/se[1], n=n, r2=r2)

rows=[]
# 1. winsorized top/bottom 1% of tour_soc_mean
d = panel.copy()
lo, hi = d['tour_soc_mean'].quantile([0.01,0.99])
d['tour_w'] = d['tour_soc_mean'].clip(lo,hi)
r = ols(d, ['log_gdp_pc'], y='tour_w'); rows.append({'check':'winsorized_1pct','beta':r['beta'],'se':r['se'],'t':r['t'],'n':r['n']})
# 2. component-wise: Food only, Personal only
for col, lab in [('Food_Preparation_and_Serving_Related','food_only'),('Personal_Care_and_Service','personal_only')]:
    r = ols(panel, ['log_gdp_pc'], y=col); rows.append({'check':lab,'beta':r['beta'],'se':r['se'],'t':r['t'],'n':r['n']})
# 3. weighted by population (larger countries carry more weight)
d = panel.dropna(subset=['log_gdp_pc','tour_soc_mean','population'])
X = np.column_stack([np.ones(len(d)), d['log_gdp_pc'].values]); yv=d['tour_soc_mean'].values; w=d['population'].values
W = np.diag(w/w.sum()*len(d))
beta = np.linalg.lstsq(np.sqrt(W)@X, np.sqrt(W)@yv, rcond=None)[0]
resid = yv - X@beta
se = np.sqrt(np.diag(np.linalg.inv(X.T@W@X))*(resid@resid/(len(d)-2)))
rows.append({'check':'population_weighted','beta':beta[1],'se':se[1],'t':beta[1]/se[1],'n':len(d)})
# 4. excluding micro-countries (pop < 500k)
d2 = panel[panel['population']>=5e5]
r = ols(d2, ['log_gdp_pc']); rows.append({'check':'excl_pop_lt_500k','beta':r['beta'],'se':r['se'],'t':r['t'],'n':r['n']})
# 5. controlling for working-age share + urbanization proxy (internet) jointly
r = ols(panel, ['log_gdp_pc','working_age_share']); rows.append({'check':'ctrl_working_age','beta':r['beta'],'se':r['se'],'t':r['t'],'n':r['n']})

out = pd.DataFrame(rows)
out.to_csv(f'{R}/robustness_b4_supplementary.csv', index=False)
print(out.round(4).to_string(index=False))
