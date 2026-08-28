"""Panel analysis v2 — richer design given T=3 (Aug 2025, Apr 2026, May 2026):

A. Growth/level dynamics: within-country changes 2025-08 -> 2026-04/05.
B. Convergence: beta-convergence (initial level vs growth) + sigma check.
C. Composition stability: is the CROSS-COUNTRY RANKING stable? (rank correlations per pair)
D. Interaction: does the cross-sectional income gradient fade as platform matures?
   (compare gradient beta in 2025-08 vs 2026-04 vs 2026-05)
E. Usage-growth decomposition: usage_per_capita growth vs tourism-share change.
Outputs: results/panel2_*.csv + figures/fig5, fig6.
"""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P='data/processed'; R='results'; F='figures'
panel = pd.read_csv(f'{P}/tour_period_panel.csv')
wb = pd.read_csv(f'{P}/wb_only.csv')
panel = panel.merge(wb[['iso3','gdp_pc','population']], on='iso3', how='left')
panel['log_gdp_pc'] = np.log(panel['gdp_pc'])
w = panel.pivot_table(index='iso3', columns='period', values='tour_soc_mean')
g = panel.pivot_table(index='iso3', columns='period', values='log_gdp_pc')

# ---------- C. rank stability ----------
def spearman(a, b):
    da = pd.DataFrame({'a':a,'b':b}).dropna()
    ra = da['a'].rank(); rb = da['b'].rank()
    return round(np.corrcoef(ra, rb)[0,1], 3)

pairs = [('2025-08','2026-04'), ('2025-08','2026-05'), ('2026-04','2026-05')]
rank_rows = []
for p1, p2 in pairs:
    both = w[[p1,p2]].dropna()
    rank_rows.append({'pair':f'{p1} vs {p2}', 'n':len(both),
                      'pearson':round(both[p1].corr(both[p2]),3),
                      'spearman':spearman(both[p1], both[p2])})
rank_df = pd.DataFrame(rank_rows)
rank_df.to_csv(f'{R}/panel2_rank_stability.csv', index=False)
print("Rank stability:"); print(rank_df.to_string(index=False))

# ---------- D. gradient by period ----------
grad_rows = []
for per in ['2025-08','2026-04','2026-05']:
    d = panel[panel.period==per].dropna(subset=['log_gdp_pc','tour_soc_mean'])
    if len(d) < 15: continue
    X = np.column_stack([np.ones(len(d)), d['log_gdp_pc'].values])
    yv = d['tour_soc_mean'].values
    beta,*_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X@beta
    se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(resid@resid/(len(d)-2)))
    grad_rows.append({'period':per,'beta':round(beta[1],4),'se':round(se[1],4),'t':round(beta[1]/se[1],2),'n':len(d)})
grad_df = pd.DataFrame(grad_rows)
grad_df.to_csv(f'{R}/panel2_gradient_by_period.csv', index=False)
print("\nIncome gradient by period:"); print(grad_df.to_string(index=False))

# ---------- B. convergence (growth vs initial level) ----------
conv = w.dropna(subset=['2025-08']).copy()
conv['growth'] = w['2026-05'] - w['2025-08']
conv = conv.dropna(subset=['growth']).reset_index().merge(wb[['iso3','population']], on='iso3', how='left')
X = np.column_stack([np.ones(len(conv)), conv['2025-08'].values])
yv = conv['growth'].values
beta,*_ = np.linalg.lstsq(X, yv, rcond=None)
resid = yv - X@beta
se = np.sqrt(np.diag(np.linalg.pinv(X.T@X))*(resid@resid/(len(conv)-2)))
conv_row = {'beta_initial':round(beta[1],4),'se':round(se[1],4),'t':round(beta[1]/se[1],2),'n':len(conv)}
pd.DataFrame([conv_row]).to_csv(f'{R}/panel2_convergence.csv', index=False)
print("\nBeta-convergence (growth on initial level):", conv_row)

# ---------- figures ----------
# Fig 5: trajectory plot (countries in all 3 periods)
both3 = w.dropna()
fig, ax = plt.subplots(figsize=(7.5,5))
for iso, row in both3.iterrows():
    ax.plot([0,1,2], [row['2025-08'], row['2026-04'], row['2026-05']], color='gray', alpha=0.35, lw=0.8)
mean_traj = [both3['2025-08'].mean(), both3['2026-04'].mean(), both3['2026-05'].mean()]
ax.plot([0,1,2], mean_traj, color='#c0392b', lw=3, marker='o', label=f'Mean trajectory (n={len(both3)})')
ax.set_xticks([0,1,2]); ax.set_xticklabels(['Aug 2025','Apr 2026','May 2026'])
ax.set_ylabel('Tourism SOC intensity (%)')
ax.set_title('Within-country trajectories of tourism-occupation AI usage', fontsize=11)
ax.legend()
plt.tight_layout(); plt.savefig(f'{F}/fig5_trajectories.png', dpi=300); plt.close()

# Fig 6: convergence scatter (initial level vs growth)
fig, ax = plt.subplots(figsize=(7.5,5))
ax.scatter(conv['2025-08'], conv['growth'], s=30, alpha=0.7, color='#2c3e50')
xs = np.linspace(conv['2025-08'].min(), conv['2025-08'].max(), 50)
ax.plot(xs, beta[0]+beta[1]*xs, color='#c0392b', lw=2,
        label=f"β-convergence (slope={beta[1]:.2f}, t={conv_row['t']:.1f})")
ax.set_xlabel('Initial level (Aug 2025, %)'); ax.set_ylabel('Growth (Aug 2025 → May 2026, pp)')
ax.set_title('Convergence: countries with high initial tourism share grew less', fontsize=11)
ax.legend(fontsize=9)
plt.tight_layout(); plt.savefig(f'{F}/fig6_convergence.png', dpi=300); plt.close()

print("\nfigures written: fig5_trajectories.png, fig6_convergence.png")
print("\ncountries in all 3 periods:", len(both3))
