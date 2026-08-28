"""Panel v4: robustness of convergence (leave-one-out), within-country correlation of food/personal changes,
and the gradient-by-period synthesis figure (fig7)."""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P='data/processed'; R='results'; F='figures'
panel = pd.read_csv(f'{P}/tour_period_panel.csv')
wb = pd.read_csv(f'{P}/wb_only.csv')
panel = panel.merge(wb[['iso3','gdp_pc']], on='iso3', how='left')
panel['log_gdp_pc'] = np.log(panel['gdp_pc'])
w = panel.pivot_table(index='iso3', columns='period', values='tour_soc_mean')
conv = w.dropna(subset=['2025-08']).copy()
conv['growth'] = w['2026-05'] - conv['2025-08']
conv = conv.dropna(subset=['growth']).reset_index()

# 1. leave-one-out convergence
loo=[]
for i in range(len(conv)):
    d = conv.drop(conv.index[i])
    X = np.column_stack([np.ones(len(d)), d['2025-08'].values]); yv=d['growth'].values
    b,*_ = np.linalg.lstsq(X,yv,rcond=None)
    res = yv-X@b
    se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(res@res/(len(d)-2)))
    loo.append({'excluded':conv.loc[conv.index[i],'iso3'],'beta':round(b[1],3),'t':round(b[1]/se[1],2)})
loo_df = pd.DataFrame(loo)
loo_df.to_csv(f'{R}/panel2_convergence_loo.csv', index=False)
print("Leave-one-out convergence: beta range", loo_df['beta'].min(), "to", loo_df['beta'].max(),
      "| t range", loo_df['t'].min(), "to", loo_df['t'].max())
print(loo_df.to_string(index=False))

# 2. component-wise growth: food vs personal
pf = panel.pivot_table(index='iso3', columns='period', values=panel.columns.intersection(['food','personal']).tolist() or None) if False else None
pfood = panel.pivot_table(index='iso3', columns='period', values='food')
ppers = panel.pivot_table(index='iso3', columns='period', values='personal')
comp = pd.DataFrame({
 'food_growth': (pfood['2026-05']-pfood['2025-08']),
 'personal_growth': (ppers['2026-05']-ppers['2025-08']),
 'food_initial': pfood['2025-08'],
 'personal_initial': ppers['2025-08'],
}).dropna()
# convergence within each component
for col, g0 in [('food_growth','food_initial'), ('personal_growth','personal_initial')]:
    X = np.column_stack([np.ones(len(comp)), comp[g0].values]); yv=comp[col].values
    b,*_ = np.linalg.lstsq(X,yv,rcond=None)
    res = yv-X@b
    se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(res@res/(len(comp)-2)))
    print(f"\nConvergence in {g0}: beta={b[1]:.3f} (t={b[1]/se[1]:.1f}, n={len(comp)})")

# 3. fig7: gradient by period bar chart
grad = pd.concat([
 pd.read_csv(f'{R}/panel2_gradient_2025_08.csv'),
 pd.read_csv(f'{R}/panel2_gradient_by_period.csv')])
grad = grad.drop_duplicates('period')
fig, ax = plt.subplots(figsize=(7.5,5))
colors = ['#8e44ad','#2980b9','#27ae60']
for i,(_,row) in enumerate(grad.iterrows()):
    ax.bar(i, row['beta'], yerr=1.96*row['se'], capsize=4, color=colors[i%3], alpha=0.85)
    ax.annotate(f"n={row['n']}", (i, row['beta']+ (0.02 if row['beta']>=0 else -0.04)), ha='center', fontsize=9)
ax.axhline(0, color='k', lw=0.8)
ax.set_xticks(range(len(grad)))
ax.set_xticklabels([f"{p}\n({n} countries)" for p,n in zip(grad.period, grad.n)])
ax.set_ylabel('OLS coefficient on log GDP per capita (95% CI)')
ax.set_title('The cross-country income gradient reverses as the platform broadens', fontsize=11)
plt.tight_layout(); plt.savefig(f'{F}/fig7_gradient_by_period.png', dpi=300); plt.close()
print("\nfig7 written")
print(grad.to_string(index=False))
