"""Analysis + figures for the AEI-tourism paper.
Produces: results/*.csv tables + 4 publication figures.
"""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P = 'data/processed'
R = 'results'
F = 'figures'
panel = pd.read_csv(f'{P}/panel.csv')
panel = panel.dropna(subset=['tour_soc_mean'])

def corr_ci(x, y, n_boot=2000, seed=42):
    d = pd.concat([x, y], axis=1).dropna()
    if len(d) < 10: return np.nan, np.nan, np.nan, len(d)
    r = d.iloc[:,0].corr(d.iloc[:,1])
    rng = np.random.default_rng(seed)
    n = len(d)
    boots = [d.sample(n, replace=True, random_state=int(rng.integers(0, 1e9))).corr().iloc[0,1] for _ in range(n_boot)]
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return r, lo, hi, n

# ---------------- Table 2: correlations of tourism SOC share with correlates ----------------
VARS = ['usage_per_capita_index','gdp_pc','arrivals_pc','tour_receipts_pc','services_emp',
        'travel_exp_share','internet_users','mobile_subs','unemployment','services_va','ict_exports']
rows = []
for v in VARS:
    r, lo, hi, n = corr_ci(panel['tour_soc_mean'], panel[v])
    rows.append({'variable': v, 'r': r, 'ci_lo': lo, 'ci_hi': hi, 'n': n})
t2 = pd.DataFrame(rows)
t2.to_csv(f'{R}/table2_correlations.csv', index=False)
print(t2.to_string(index=False))

# ---------------- Table 3: log-gdp regressions (robust OLS via numpy) ----------------
def ols(formula_df, y):
    d = formula_df.join(y).dropna()
    X = d.iloc[:, :-1].copy()
    X.insert(0, 'const', 1.0)
    Xv = X.values; yv = d.iloc[:, -1].values
    beta, *_ = np.linalg.lstsq(Xv, yv, rcond=None)
    resid = yv - Xv @ beta
    n, k = Xv.shape
    sigma2 = resid @ resid / (n - k)
    XtXinv = np.linalg.inv(Xv.T @ Xv)
    se = np.sqrt(np.diag(XtXinv) * sigma2)
    t = beta / se
    return pd.DataFrame({'coef': beta, 'se': se, 't': t}, index=X.index.names and list(X.columns)), n, d

sub = panel.copy()
sub['log_gdp_pc'] = np.log(sub['gdp_pc'])
sub['log_arrivals_pc'] = np.log(sub['arrivals_pc'].clip(lower=1e-4))

models = {
 'M1_loggdp': ['log_gdp_pc'],
 'M2_internet': ['log_gdp_pc','internet_users'],
 'M3_arrivals': ['log_gdp_pc','log_arrivals_pc'],
 'M4_services': ['log_gdp_pc','services_emp'],
 'M5_full': ['log_gdp_pc','internet_users','log_arrivals_pc','services_emp'],
}
res_rows = []
fit_stats = []
for name, vs in models.items():
    coef_tab, n, d = ols(sub[vs].copy(), sub['tour_soc_mean'])
    for var, row in coef_tab.iterrows():
        res_rows.append({'model': name, 'term': var, 'coef': row['coef'], 'se': row['se'], 't': row['t']})
    yv = d['tour_soc_mean'].values
    yhat = np.asarray([1]*len(d) and np.column_stack([np.ones(len(d))] + [d[v].values for v in vs]) @ coef_tab['coef'].values)
    ss_res = ((yv - yhat)**2).sum(); ss_tot = ((yv - yv.mean())**2).sum()
    r2 = 1 - ss_res/ss_tot
    adj = 1 - (1-r2)*(len(d)-1)/(len(d)-len(vs)-1)
    fit_stats.append({'model': name, 'n': len(d), 'r2': r2, 'adj_r2': adj})
t3 = pd.DataFrame(res_rows)
t3.to_csv(f'{R}/table3_regressions.csv', index=False)
pd.DataFrame(fit_stats).to_csv(f'{R}/table3_fit.csv', index=False)
print(pd.DataFrame(fit_stats).to_string(index=False))
print(t3.to_string(index=False))

# ---------------- Table 1: tourism occupation profiles (global detail) ----------------
det = pd.read_csv(f'{P}/global_occupation_shares.csv')
tour_occ = det[det.occupation.isin([
 'Travel Agents','Tour Guides and Escorts','Travel Guides','Flight Attendants','Concierges',
 'Hotel, Motel, and Resort Desk Clerks','Lodging Managers','Food Service Managers',
 'Chefs and Head Cooks','Cooks, Restaurant','Waiters and Waitresses',
 'Reservation and Transportation Ticket Agents and Travel Clerks',
 'Meeting, Convention, and Event Planners','Amusement and Recreation Attendants',
 'Recreation Workers','Baggage Porters and Bellhops',
 'Entertainment and Recreation Managers, Except Gambling','Curators','Museum Technicians and Conservators'])]
tour_occ = tour_occ.sort_values('global_pct', ascending=False)
tour_occ.to_csv(f'{R}/table1_tourism_occupations.csv', index=False)

# ---------------- Table 4: augmentation vs automation tourism vs others ----------------
aug = pd.read_csv(f'{P}/augmentation_by_major_group.csv')
aug['tourism_flag'] = aug['node_name'].isin(['Food Preparation and Serving Related','Personal Care and Service','Arts, Design, Entertainment, Sports, and Media','Sales and Related'])
aug.to_csv(f'{R}/table4_augmentation.csv', index=False)

# ---------------- Figure 1: global shares by major group ----------------
df = pd.read_pickle('data/raw/aei.pkl')
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==1) & (df.metric_id=='pct') & (df.date_start=='2026-05-01')]
mg = soc.groupby('node_name')['value'].mean().sort_values(ascending=False)
tour_groups = {'Food Preparation and Serving Related','Personal Care and Service','Arts, Design, Entertainment, Sports, and Media','Sales and Related','Transportation and Material Moving'}
colors = ['#c0392b' if g in tour_groups else '#7f8c8d' for g in mg.index]
fig, ax = plt.subplots(figsize=(8.5, 5.5))
ax.barh(range(len(mg)), mg.values, color=colors)
ax.set_yticks(range(len(mg)))
ax.set_yticklabels([g.replace(' and ', ' & ').replace(' Related','').replace(', Sports','/Sports') for g in mg.index], fontsize=8)
ax.invert_yaxis()
ax.set_xlabel('Share of Claude work-related conversations (%)')
ax.set_title('Claude usage by SOC major group, May 2026\n(tourism-relevant groups in red)', fontsize=11)
plt.tight_layout()
plt.savefig(f'{F}/fig1_major_groups.png', dpi=300)
plt.close()

# ---------------- Figure 2: tourism SOC intensity vs GDP per capita ----------------
fig, ax = plt.subplots(figsize=(7.5, 5))
d = panel.dropna(subset=['gdp_pc'])
ax.scatter(np.log10(d['gdp_pc']), d['tour_soc_mean'], s=22, alpha=0.6, color='#2c3e50')
# fit line
z = np.polyfit(np.log10(d['gdp_pc']), d['tour_soc_mean'], 1)
xs = np.linspace(np.log10(d['gdp_pc']).min(), np.log10(d['gdp_pc']).max(), 50)
ax.plot(xs, np.polyval(z, xs), color='#c0392b', lw=2, label=f'OLS fit (slope={z[0]:.2f})')
for iso in ['THA','ESP','GRC','AUS','SGP','USA','IND','EGY','MEX','IDN']:
    dd = d[d.iso3==iso]
    if len(dd):
        ax.annotate(iso, (np.log10(dd['gdp_pc'].iloc[0]), dd['tour_soc_mean'].iloc[0]), fontsize=7, color='#34495e')
ax.set_xlabel('log10 GDP per capita (US$, latest available)')
ax.set_ylabel('Tourism SOC intensity (% of Claude usage)')
ax.set_title('Tourism-occupation AI usage vs economic development', fontsize=11)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(f'{F}/fig2_gdp_scatter.png', dpi=300)
plt.close()

# ---------------- Figure 3: correlation forest plot ----------------
t2s = t2.dropna().sort_values('r')
fig, ax = plt.subplots(figsize=(7.5, 5))
ypos = range(len(t2s))
ax.errorbar(t2s['r'], ypos, xerr=[t2s['r']-t2s['ci_lo'], t2s['ci_hi']-t2s['r']], fmt='o', color='#2c3e50', ecolor='#7f8c8d', capsize=3)
ax.axvline(0, color='#c0392b', ls='--', lw=1)
ax.set_yticks(list(ypos)); ax.set_yticklabels(t2s['variable'], fontsize=9)
ax.set_xlabel('Pearson correlation with tourism SOC intensity (95% bootstrap CI)')
ax.set_title('Economic correlates of tourism-occupation AI usage', fontsize=11)
plt.tight_layout()
plt.savefig(f'{F}/fig3_forest.png', dpi=300)
plt.close()

# ---------------- Figure 4: augmentation vs automation, tourism vs non-tourism ----------------
fig, ax = plt.subplots(figsize=(7.5, 5))
for flag, color, label in [(True, '#c0392b', 'Tourism-relevant groups'), (False, '#7f8c8d', 'Other groups')]:
    dd = aug[aug.tourism_flag==flag]
    ax.scatter(dd['collaboration_bucket_augmentation_pct'], dd['collaboration_bucket_automation_pct'],
               s=60, alpha=0.8, color=color, label=label)
    for _, row in dd.iterrows():
        if flag:
            ax.annotate(row['node_name'].replace(' and ',' & ').replace(' Related',''),
                        (row['collaboration_bucket_augmentation_pct'], row['collaboration_bucket_automation_pct']),
                        fontsize=7, color=color, xytext=(4,3), textcoords='offset points')
lim = [min(aug['collaboration_bucket_augmentation_pct'].min(), aug['collaboration_bucket_automation_pct'].min())-3,
       max(aug['collaboration_bucket_augmentation_pct'].max(), aug['collaboration_bucket_automation_pct'].max())+3]
ax.plot(lim, lim, 'k--', lw=0.8, alpha=0.5)
ax.set_xlabel('Augmentation (%)'); ax.set_ylabel('Automation (%)')
ax.set_title('Automation vs augmentation by SOC major group, May 2026', fontsize=11)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig(f'{F}/fig4_automation.png', dpi=300)
plt.close()

# country list
panel[['iso3','tour_soc_mean','usage_per_capita_index','gdp_pc','arrivals_pc']].to_csv(f'{R}/country_panel_clean.csv', index=False)
print("\nDONE. Files:", __import__('os').listdir(R))
