import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load và xử lý dữ liệu
df = pd.read_csv('datathon-2026/data/sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Week'] = df['Date'].dt.isocalendar().week

# 2. Tính Tỷ trọng % Doanh thu
weekly_rev = df.groupby(['Year', 'Week'])['Revenue'].sum().reset_index()
annual_rev = weekly_rev.groupby('Year')['Revenue'].transform('sum')
weekly_rev['Rev_Share'] = (weekly_rev['Revenue'] / annual_rev) * 100
pivot_table = weekly_rev.pivot(index='Year', columns='Week', values='Rev_Share')

# 3. Khởi tạo biểu đồ (Kích thước lớn 24x8 để chữ không đè nhau)
fig, ax = plt.subplots(figsize=(24, 8), facecolor='white')

# 4. Vẽ Heatmap (Bảng màu YlOrRd - Vàng/Đỏ như ảnh 1)
sns.heatmap(pivot_table, 
            cmap='YlOrRd', 
            cbar_kws={'label': '% of annual rev'},
            linewidths=0.05, 
            linecolor='lightgray',
            ax=ax)

# 5. Tùy chỉnh Nhãn & Tiêu đề
ax.set_title('Heatmap: Tuần × Năm — Revenue share (% năm)\nCác cột dọc = PATTERN GIỐNG HỆT nhau qua mọi năm', 
             fontsize=15, fontweight='bold', pad=25)
ax.set_xlabel('Tuần trong năm', fontsize=13, fontweight='bold')
ax.set_ylabel('Năm', fontsize=13, fontweight='bold')
plt.setp(ax.get_yticklabels(), rotation=90, va='center') 

# 6. Thêm vạch phân chia các mùa
weeks = list(pivot_table.columns)

def get_index(week_num):
    return weeks.index(week_num) if week_num in weeks else -1

seasons = {
    13: 'Bắt đầu Mùa Xuân',
    26: 'Bắt đầu Mùa Hè',
    39: 'Bắt đầu Mùa Thu',
    52: 'Bắt đầu Mùa Đông'
}

for week, name in seasons.items():
    idx = get_index(week)
    if idx != -1:
        ax.axvline(x=idx, color='blue', linewidth=3, linestyle='--')
        ax.text(idx + 0.5, -0.2, name, color='blue', fontweight='bold', ha='left', va='center', fontsize=11)

# 7. Lưu file
plt.tight_layout()
plt.savefig('heatmap_percent_with_seasons.png', dpi=300, bbox_inches='tight')
print("Đã lưu biểu đồ thành công vào file 'heatmap_percent_with_seasons.png'")
