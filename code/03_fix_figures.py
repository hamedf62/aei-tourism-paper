"""Fix label truncation ('Sales & Related' -> replace ' & ' AFTER length-safety) and re-render figs 1 & 4."""
import pandas as pd, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

P = 'data/processed'; F = 'figures'
df = pd.read_pickle('data/raw/aei.pkl')

def short(g):
    return (g.replace(' and ', ' & ').replace(' Related', ' Rel.')
             .replace('Sports', '/Sports').replace('Entertainment, Design', 'Ent./Design'))

# --- Fig 1 ---
soc = df[(df.category_name=='soc_occupation') & (df.geo_level=='global') & (df.hierarchy_level==1) & (df.metric_id=='pct') & (df.date_start=='2026-05-01')]
mg = soc.groupby('node_name')['value'].mean().sort_values(ascending=False)
tour_groups = {'Food Preparation and Serving Related','Personal Care and Service','Arts, Design, Entertainment, Sports, and Media','Sales and Related','Transportation and Material Moving'}
colors = ['#c0392b' if g in tour_groups else '#7f8c8d' for g in mg.index]
fig, ax = plt.subplots(figsize=(8.5, 5.5))
ax.barh(range(len(mg)), mg.values, color=colors)
ax.set_yticks(range(len(mg)))
ax.set_yticklabels([short(g) for g in mg.index], fontsize=8)
ax.invert_yaxis()
ax.set_xlabel('Share of Claude work-related conversations (%)')
ax.set_title('Claude usage by SOC major group, May 2026\n(tourism-relevant groups in red)', fontsize=11)
plt.tight_layout()
plt.savefig(f'{F}/fig1_major_groups.png', dpi=300)
plt.close()

# --- Fig 4 ---
aug = pd.read_csv(f'{P}/augmentation_by_major_group.csv')
aug['tourism_flag'] = aug['node_name'].isin(['Food Preparation and Serving Related','Personal Care and Service','Arts, Design, Entertainment, Sports, and Media','Sales and Related'])
fig, ax = plt.subplots(figsize=(7.5, 5))
for flag, color, label in [(True, '#c0392b', 'Tourism-relevant groups'), (False, '#7f8c8d', 'Other groups')]:
    dd = aug[aug.tourism_flag==flag]
    ax.scatter(dd['collaboration_bucket_augmentation_pct'], dd['collaboration_bucket_automation_pct'],
               s=60, alpha=0.8, color=color, label=label)
    for _, row in dd.iterrows():
        if flag:
            ax.annotate(short(row['node_name']),
                        (row['collaboration_bucket_augmentation_pct'], row['collaboration_bucket_automation_pct']),
                        fontsize=7, color=color, xytext=(4,3), textcoords='offset points')
lim = [min(aug['collaboration_bucket_augmentation_pct'].min(), aug['collaboration_bucket_automation_pct'].min())-3,
       max(aug['collaboration_bucket_augmentation_pct'].max(), aug['collaboration_bucket_automation_pct'].max())+3]
ax.plot(lim, lim, 'k--', lw=0.8, alpha=0.5)
ax.set_xlim(lim); ax.set_ylim(lim)
ax.set_xlabel('Augmentation (%)'); ax.set_ylabel('Automation (%)')
ax.set_title('Automation vs augmentation by SOC major group, May 2026', fontsize=11)
ax.legend(fontsize=9, loc='upper right')
plt.tight_layout()
plt.savefig(f'{F}/fig4_automation.png', dpi=300)
plt.close()
print("figs regenerated")
