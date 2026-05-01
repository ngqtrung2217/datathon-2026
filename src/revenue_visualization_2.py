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

# 3. Khởi tạo biểu đồ
fig, ax = plt.subplots(figsize=(24, 8), facecolor='white')

# 4. Vẽ Heatmap
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

# 6. Thêm vạch phân chia và CĂN GIỮA tên Giai đoạn
weeks = list(pivot_table.columns)

def get_right_edge(week_num, default_idx):
    # Lấy tọa độ mép phải của tuần đó (index + 1) để cắt cho chuẩn
    return weeks.index(week_num) + 1 if week_num in weeks else default_idx

# Lấy các mốc cắt: Cuối tuần 13, 26, 39 và tuần cuối cùng của dữ liệu
b1 = get_right_edge(13, 13)
b2 = get_right_edge(26, 26)
b3 = get_right_edge(39, 39)
b4 = len(weeks) # Vạch chốt hạ: Hết tuần luôn (sát mép phải biểu đồ)

# Kẻ vạch
boundaries = [b1, b2, b3, b4]
for x_pos in boundaries:
    ax.axvline(x=x_pos, color='blue', linewidth=3, linestyle='--')

# Định nghĩa các Giai đoạn (Từ mốc này đến mốc kia)
periods_intervals = [
    (0, b1, 'Giai đoạn 1'),
    (b1, b2, 'Giai đoạn 2'),
    (b2, b3, 'Giai đoạn 3'),
    (b3, b4, 'Giai đoạn 4')
]

# Tính điểm giữa và điền chữ
for start_idx, end_idx, name in periods_intervals:
    if end_idx > start_idx:
        # Tính điểm chính giữa của khoảng
        mid_point = (start_idx + end_idx) / 2
        # ha='center' giúp text nằm cân đối ngay tại điểm giữa
        ax.text(mid_point, -0.2, name, color='blue', fontweight='bold', ha='center', va='center', fontsize=13)

# 7. Lưu file
plt.tight_layout()
plt.savefig('heatmap_percent_phases.png', dpi=300, bbox_inches='tight')
print("Đã lưu biểu đồ thành công vào file 'heatmap_percent_phases.png'")
