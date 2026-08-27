"""Generate Appendix B robustness tables (B1-B3) promised in the manuscript."""
import pandas as pd, numpy as np

P='data/processed'; R='results'
df = pd.read_pickle('data/raw/aei.pkl')
panel = pd.read_csv(f'{P}/panel.csv').dropna(subset=['tour_soc_mean'])

soc = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')]
mg = soc.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
mg.columns = [c.replace(' ','_') for c in mg.columns]
panel = panel.merge(mg.reset_index().rename(columns={'geo_id':'iso3'}), on='iso3', how='left')

def ols(d, vs, y='tour_soc_mean'):
    d = d.dropna(subset=vs+[y])
    X = np.column_stack([np.ones(len(d))]+[d[v].values for v in vs])
    yv = d[y].values
    beta,*_ = np.linalg.lstsq(X,yv,rcond=None)
    resid = yv - X@beta
    n,k = X.shape
    sigma2 = resid@resid/(n-k)
    se = np.sqrt(np.diag(np.linalg.inv(X.T@X))*sigma2)
    yhat = X@beta
    r2 = 1-((yv-yhat)**2).sum()/((yv-yv.mean())**2).sum()
    out = pd.DataFrame({'term':['const']+vs,'coef':beta,'se':se})
    return out, n, r2

sub = panel.copy()
sub['log_gdp_pc'] = np.log(sub['gdp_pc'])

# ---- B1: alternative intensity definitions ----
defs = {
 'B1_mean_base': ['Food_Preparation_and_Serving_Related','Personal_Care_and_Service'],
 'B1_sum': None,
 'B1_add_sales': ['Food_Preparation_and_Serving_Related','Personal_Care_and_Service','Sales_and_Related'],
 'B1_add_arts': ['Food_Preparation_and_Serving_Related','Personal_Care_and_Service','Arts,_Design,_Entertainment,_Sports,_and_Media'],
}
rows=[]
for name, cols in defs.items():
    d = sub.copy()
    if name=='B1_sum':
        d['y'] = d['Food_Preparation_and_Serving_Related'] + d['Personal_Care_and_Service']
    elif name=='B1_mean_base':
        d['y'] = d[cols].mean(axis=1)
    else:
        d['y'] = d[cols].mean(axis=1)
    coef, n, r2 = ols(d, ['log_gdp_pc'], y='y')
    b = coef[coef.term=='log_gdp_pc'].iloc[0]
    # travel exports corr
    dd = d.dropna(subset=['travel_exp_share'])
    r_travel = dd['y'].corr(dd['travel_exp_share'])
    rows.append({'definition':name,'beta_log_gdp':b['coef'],'se':b['se'],'n':n,'r2':r2,'r_travel_exp':r_travel})
b1 = pd.DataFrame(rows)
b1.to_csv(f'{R}/robustness_b1_definitions.csv', index=False)
print(b1.to_string(index=False))

# ---- B2: exclude top-5 tourism intensity countries ----
top5 = sub.nlargest(5,'tour_soc_mean').iso3.tolist()
d2 = sub[~sub.iso3.isin(top5)]
coef,n,r2 = ols(d2, ['log_gdp_pc'])
b = coef[coef.term=='log_gdp_pc'].iloc[0]
pd.DataFrame([{'excluded':', '.join(top5),'beta_log_gdp':b['coef'],'se':b['se'],'n':n,'r2':r2}]).to_csv(f'{R}/robustness_b2_excl_top5.csv', index=False)
print("\nB2 excluded:", top5, "beta:", round(b['coef'],3), "se:", round(b['se'],3))

# ---- B3: April vs May stability ----
soc_apr = df[(df.category_name=='soc_occupation')&(df.geo_level=='country')&(df.hierarchy_level==1)&(df.metric_id=='pct')&(df.date_start=='2026-04-01')]
mg_apr = soc_apr.pivot_table(index='geo_id', columns='node_name', values='value', aggfunc='mean')
mg_apr.columns = [c.replace(' ','_') for c in mg_apr.columns]
tour_apr = mg_apr[['Food_Preparation_and_Serving_Related','Personal_Care_and_Service']].mean(axis=1).rename('tour_apr')
d3 = sub.set_index('iso3').join(tour_apr, how='inner').reset_index()
r_stab = d3['tour_soc_mean'].corr(d3['tour_apr'])
coef,n,r2 = ols(d3, ['log_gdp_pc'], y='tour_apr')
b = coef[coef.term=='log_gdp_pc'].iloc[0]
pd.DataFrame([{'r_may_apr':r_stab,'beta_apr_log_gdp':b['coef'],'se':b['se'],'n':n}]).to_csv(f'{R}/robustness_b3_month_stability.csv', index=False)
print("\nB3 r(May,Apr):", round(r_stab,3), "| beta(Apr) log_gdp:", round(b['coef'],3), "se:", round(b['se'],3), "n:", n)
