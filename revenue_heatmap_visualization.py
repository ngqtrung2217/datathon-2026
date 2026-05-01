import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# ---------------------------------------------------------
# 1. ĐỌC VÀ XỬ LÝ DỮ LIỆU
# ---------------------------------------------------------
df = pd.read_csv('datathon-2026/data/sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Week'] = df['Date'].dt.isocalendar().week

# Nhóm dữ liệu theo năm và tuần
pivot_data = df.groupby(['Year', 'Week'])['Revenue'].sum().reset_index()

# Chuyển đổi dữ liệu thành ma trận pivot và chia cho 1 tỷ để hiển thị Tỷ USD
pivot_table = pivot_data.pivot(index='Year', columns='Week', values='Revenue') / 1e9

# ---------------------------------------------------------
# 2. THIẾT LẬP VÀ VẼ HEATMAP
# ---------------------------------------------------------
# Tạo biểu đồ (Mở rộng kích thước 24x8 để chứa đủ hơn 52 cột)
fig, ax = plt.subplots(figsize=(24, 8))

# Vẽ heatmap (tắt annot để tránh chữ đè lên nhau)
sns.heatmap(pivot_table, 
            annot=False, 
            cmap='RdYlGn',
            cbar_kws={'label': 'Doanh thu (Tỷ USD)'},
            linewidths=0.1,
            linecolor='gray',
            ax=ax,
            vmin=pivot_table.min().min(),
            vmax=pivot_table.max().max())

# Tùy chỉnh Nhãn và Tiêu đề
ax.set_xlabel('Tuần trong năm', fontsize=13, fontweight='bold')
ax.set_ylabel('Năm', fontsize=13, fontweight='bold')
ax.set_title('Heatmap Doanh thu theo Tuần cùng Ranh giới các Mùa\nCường độ màu = Mức Doanh thu', 
             fontsize=15, fontweight='bold', pad=20)

# ---------------------------------------------------------
# 3. THÊM VẠCH PHÂN CHIA CÁC MÙA
# Ước tính dựa trên 52 tuần:
# Mùa Xuân bắt đầu ~Tuần 13 | Mùa Hè bắt đầu ~Tuần 26
# Mùa Thu bắt đầu ~Tuần 39  | Mùa Đông bắt đầu ~Tuần 52
# ---------------------------------------------------------
weeks = list(pivot_table.columns)

def get_index(week_num):
    """Hàm phụ trợ để tìm chính xác chỉ số cột cho các đường phân chia"""
    if week_num in weeks:
        return weeks.index(week_num)
    return -1

# Xác định chỉ số (index) bắt đầu của từng mùa
spring_idx = get_index(13)
summer_idx = get_index(26)
fall_idx = get_index(39)
winter_idx = get_index(52)

# Vẽ đường phân chia và thêm nhãn
season_indices = [spring_idx, summer_idx, fall_idx, winter_idx]
season_names = ['Bắt đầu Mùa Xuân', 'Bắt đầu Mùa Hè', 'Bắt đầu Mùa Thu', 'Bắt đầu Mùa Đông']

for idx, name in zip(season_indices, season_names):
    if idx != -1:
        # Vẽ một đường dọc nét đứt
        ax.axvline(x=idx, color='blue', linewidth=3, linestyle='--')
        # Thêm tên mùa ngay trên vạch kẻ
        ax.text(idx + 0.5, -0.2, name, color='blue', fontweight='bold', ha='left', va='center')

# ---------------------------------------------------------
# 4. HOÀN THIỆN VÀ LƯU BIỂU ĐỒ
# ---------------------------------------------------------
plt.tight_layout()
plt.savefig('weekly_revenue_heatmap_vi.png', dpi=300, bbox_inches='tight')
print("Đã lưu Heatmap vào: weekly_revenue_heatmap_vi.png")

# In ra tóm tắt dữ liệu
print("\n" + "="*80)
print("DOANH THU THEO TUẦN - BẢNG DỮ LIỆU HEATMAP XEM TRƯỚC")
print("="*80)
# Chỉ in 10 tuần đầu tiên để giữ cho console gọn gàng
print(pivot_table.iloc[:, :10].round(2))