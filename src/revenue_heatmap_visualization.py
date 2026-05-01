import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('datathon-2026/data/sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Week'] = df['Date'].dt.isocalendar().week

pivot_data = df.groupby(['Year', 'Week'])['Revenue'].sum().reset_index()
pivot_table = pivot_data.pivot(index='Year', columns='Week', values='Revenue') / 1e9

fig, ax = plt.subplots(figsize=(24, 8))

median_val = pivot_table.median().median()

sns.heatmap(pivot_table, 
            annot=False, 
            cmap='RdYlGn',
            cbar_kws={'label': 'Doanh thu (Tỉ VNĐ)'},
            linewidths=0.1,
            linecolor='gray',
            ax=ax,
            robust=True,
            center=median_val)

ax.set_xlabel('Tuần trong năm', fontsize=13, fontweight='bold')
ax.set_ylabel('Năm', fontsize=13, fontweight='bold')
ax.set_title('Heatmap Doanh thu theo Tuần', fontsize=15, fontweight='bold', pad=30)

weeks = list(pivot_table.columns)

def get_index(week_num):
    if week_num in weeks:
        return weeks.index(week_num)
    return -1

idx_13 = get_index(13)
idx_26 = get_index(26)
idx_39 = get_index(39)
idx_52 = get_index(52)

boundaries = [idx_13, idx_26, idx_39, idx_52]
for idx in boundaries:
    if idx != -1:
        ax.axvline(x=idx, color='blue', linewidth=3, linestyle='--')

stages = [
    ("Giai đoạn 1", 0, idx_13 if idx_13 != -1 else 13),
    ("Giai đoạn 2", idx_13 if idx_13 != -1 else 13, idx_26 if idx_26 != -1 else 26),
    ("Giai đoạn 3", idx_26 if idx_26 != -1 else 26, idx_39 if idx_39 != -1 else 39),
    ("Giai đoạn 4", idx_39 if idx_39 != -1 else 39, len(weeks))
]

for name, start, end in stages:
    if start != -1 and end != -1 and end > start:
        mid_point = (start + end) / 2
        ax.text(mid_point, -0.3, name, color='blue', fontweight='bold', ha='center', va='center', fontsize=12)

plt.tight_layout()
plt.savefig('weekly_revenue_heatmap_vi.png', dpi=300, bbox_inches='tight')
print("Đã lưu Heatmap vào: weekly_revenue_heatmap_vi.png")
