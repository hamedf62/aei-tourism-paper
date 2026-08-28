"""Panel v3: 2025-08 gradient (17 countries, restricted schema) + within-country component analysis.
Also examine WHO entered later: are 2026-only countries richer/poorer than 2025-08 adopters?
"""
import pandas as pd, numpy as np

P='data/processed'; R='results'
panel = pd.read_csv(f'{P}/tour_period_panel.csv')
wb = pd.read_csv(f'{P}/wb_only.csv')
panel = panel.merge(wb[['iso3','gdp_pc','population']], on='iso3', how='left')
panel['log_gdp_pc'] = np.log(panel['gdp_pc'])

# 1. gradient in 2025-08 (n=17)
d = panel[panel.period=='2025-08'].dropna(subset=['log_gdp_pc','tour_soc_mean'])
X = np.column_stack([np.ones(len(d)), d['log_gdp_pc'].values]); yv=d['tour_soc_mean'].values
b,*_ = np.linalg.lstsq(X,yv,rcond=None)
res = yv-X@b
se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(res@res/(len(d)-2)))
r1 = {'period':'2025-08','beta':round(b[1],4),'se':round(se[1],4),'t':round(b[1]/se[1],2),'n':len(d)}
print("2025-08 gradient:", r1)
pd.DataFrame([r1]).to_csv(f'{R}/panel2_gradient_2025_08.csv', index=False)

# 2. early vs late adopters: is 2025-08 presence related to income/usage?
panel['early'] = panel.iso3.isin(panel[panel.period=='2025-08'].iso3)
info = panel[panel.period=='2026-05'].dropna(subset=['log_gdp_pc']).copy()
info = info.drop_duplicates('iso3')
# usage index (May) from panel.csv
pmain = pd.read_csv(f'{P}/panel.csv')[['iso3','usage_per_capita_index']]
info = info.merge(pmain, on='iso3', how='left')
early = info[info.early]; late = info[~info.early]
comp = pd.DataFrame({
 'group':['early (2025-08)','late (2026 only)'],
 'n':[len(early), len(late)],
 'mean_log_gdp':[round(early['log_gdp_pc'].mean(),3), round(late['log_gdp_pc'].mean(),3)],
 'mean_usage_index':[round(early['usage_per_capita_index'].mean(),3), round(late['usage_per_capita_index'].mean(),3)],
 'mean_tour_share':[round(early['tour_soc_mean'].mean(),3), round(late['tour_soc_mean'].mean(),3)],
})
print("\n", comp.to_string(index=False))
comp.to_csv(f'{R}/panel2_early_vs_late.csv', index=False)

# 3. mean-level shift decomposition: within vs entry
w = panel.pivot_table(index='iso3', columns='period', values='tour_soc_mean')
stayers = w.dropna()
overall = {
 'mean_2025_08_stayers': round(stayers['2025-08'].mean(),3),
 'mean_2026_05_stayers': round(stayers['2026-05'].mean(),3),
 'within_growth_pp': round((stayers['2026-05']-stayers['2025-08']).mean(),3),
 'entry_effect_pp': round((w['2026-05'] - w['2025-08']).reindex(w.index).mean(),3),
}
print("\nDecomposition:", overall)
pd.DataFrame([overall]).to_csv(f'{R}/panel2_decomposition.csv', index=False)
