"""Panel econometrics on the 3-period (Aug 2025, Apr 2026, May 2026) country panel.
Merges WDI time-invariant covariates; estimates:
 1. Pooled OLS with period dummies
 2. Country fixed effects (within estimator)
 3. First-difference / growth regressions (2025-08 -> 2026-05 change)
 4. Switching-analysis: does the income gradient strengthen/weaken as adoption grows?
Outputs results/panel_*.csv
"""
import pandas as pd, numpy as np

P='data/processed'; R='results'
panel = pd.read_csv(f'{P}/tour_period_panel.csv')
wb = pd.read_csv(f'{P}/wb_only.csv')
panel = panel.merge(wb[['iso3','gdp_pc','population','arrivals_pc','services_emp','travel_exp_share','internet_users','usage_per_capita_index' if 'usage_per_capita_index' in wb.columns else 'gdp_growth']], on='iso3', how='left')

# usage index is period-specific (only May); make a time-invariant proxy: log gdp pc
panel['log_gdp_pc'] = np.log(panel['gdp_pc'])
panel['t_num'] = panel['period'].map({'2025-08':0,'2026-04':1,'2026-05':2})

def ols(d, X_cols, y, weights=None):
    d = d.dropna(subset=X_cols+[y])
    X = np.column_stack([np.ones(len(d))]+[d[c].values for c in X_cols])
    yv = d[y].values
    if weights is not None:
        w = d[weights].values
        sw = np.sqrt(w/w.mean())
        X = X * sw[:,None]; yv = yv*sw
    beta,*_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X@beta
    n,k = X.shape
    se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(resid@resid/(n-k)))
    return pd.DataFrame({'term':['const']+X_cols,'coef':beta,'se':se,'t':beta/se}), n

rows=[]; notes=[]
# M1: pooled with period dummies
d = panel.copy()
for t in [1,2]:
    d[f'd{t}'] = (d.t_num==t).astype(int)
c1, n1 = ols(d, ['log_gdp_pc','d1','d2'], 'tour_soc_mean')
c1.insert(0,'model','pooled_period_dummies'); rows.append((c1,n1)); notes.append(('pooled_period_dummies',n1))

# M2: country FE (within)
dm = panel.dropna(subset=['log_gdp_pc'])
ybar = dm.groupby('iso3')['tour_soc_mean'].transform('mean')
xbar = dm.groupby('iso3')['log_gdp_pc'].transform('mean')
dm['y_w'] = dm['tour_soc_mean'] - ybar
dm['x_w'] = dm['log_gdp_pc'] - xbar
d = dm.dropna(subset=['y_w','x_w'])
X = d[['x_w']].values; yv = d['y_w'].values
beta = (X.T@X).astype(float)
coef = float((np.linalg.pinv(beta)@X.T@yv)[0])
resid = yv - X.flatten()*coef
se = float(np.sqrt((resid@resid)/(len(d)-1) * np.linalg.pinv(beta)[0,0]))
fe_row = pd.DataFrame({'model':['country_FE'],'term':['log_gdp_pc (within)'],'coef':[coef],'se':[se],'t':[coef/se]})
n_fe = len(d)

# M3: change regression (within-country growth of tourism share vs gdp)
w = panel.pivot_table(index='iso3', columns='period', values='tour_soc_mean')
w['delta'] = w['2026-05'] - w['2025-08']
wd = w.dropna().reset_index().merge(wb[['iso3','gdp_pc']], on='iso3', how='left')
wd['log_gdp_pc'] = np.log(wd['gdp_pc'])
c3, n3 = ols(wd.dropna(subset=['log_gdp_pc']), ['log_gdp_pc'], 'delta')
c3.insert(0,'model','delta_202508_202605'); rows.append((c3,n3))

# assemble
out = pd.concat([r[0] for r in rows], ignore_index=True)
out = pd.concat([out, fe_row], ignore_index=True)
out.to_csv(f'{R}/panel_regressions.csv', index=False)
pd.DataFrame(notes, columns=['model','n']).to_csv(f'{R}/panel_model_n.csv', index=False)

print(out.round(4).to_string(index=False))
print("\nFE model n:", n_fe)
print("\nDelta regression n:", n3)
print("\nDelta descriptives:", wd['delta'].describe().round(3).to_dict())
