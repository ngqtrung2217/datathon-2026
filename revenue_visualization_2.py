import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------
# 1. ĐỌC VÀ XỬ LÝ DỮ LIỆU TỪ FILE CSV
# ---------------------------------------------------------
df = pd.read_csv('datathon-2026/data/sales.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Trích xuất Năm và Tuần (ISO week)
df['Year'] = df['Date'].dt.year
df['Week'] = df['Date'].dt.isocalendar().week

# Nhóm dữ liệu để tính tổng doanh thu theo từng Tuần của mỗi Năm
weekly_rev = df.groupby(['Year', 'Week'])['Revenue'].sum().reset_index()

# Tính tổng doanh thu của cả Năm
annual_rev = weekly_rev.groupby('Year')['Revenue'].transform('sum')

# Tính tỷ trọng doanh thu tuần (% of annual rev)
weekly_rev['Rev_Share'] = (weekly_rev['Revenue'] / annual_rev) * 100

# Xoay dữ liệu (Pivot) thành ma trận: Hàng là Năm, Cột là Tuần
heatmap_data = weekly_rev.pivot(index='Year', columns='Week', values='Rev_Share')


# ---------------------------------------------------------
# 2. THIẾT LẬP STYLE BIỂU ĐỒ (LIGHT THEME)
# ---------------------------------------------------------
bg_color = 'white'  
text_color = 'black' 

# Mở rộng kích thước (24x8) để chữ chia mùa hiển thị rõ, giống kích thước ảnh số 2
fig, ax = plt.subplots(figsize=(24, 8), facecolor=bg_color)
ax.set_facecolor(bg_color)


# ---------------------------------------------------------
# 3. VẼ HEATMAP (TỶ TRỌNG % - BẢNG MÀU VÀNG/ĐỎ)
# ---------------------------------------------------------
# Bỏ xticklabels=5 để hiển thị toàn bộ số tuần giống ảnh số 2, giúp dễ dóng hàng
sns.heatmap(heatmap_data, 
            cmap='YlOrRd', 
            cbar_kws={'label': '% of annual rev', 'shrink': 0.6},
            linewidths=0.05, 
            linecolor='lightgray',
            ax=ax)


# ---------------------------------------------------------
# 4. TÙY CHỈNH LABELS, TITLE & COLORBAR
# ---------------------------------------------------------
plt.title('Heatmap: Tuần × Năm — Revenue share (% năm)\nCác cột dọc = PATTERN GIỐNG HỆT nhau qua mọi năm', 
          color=text_color, fontsize=15, fontweight='bold', pad=25)

plt.xlabel('Tuần trong năm', color=text_color, fontsize=13, fontweight='bold')
plt.ylabel('Năm', color=text_color, fontsize=13, fontweight='bold')

ax.tick_params(colors=text_color)
plt.setp(ax.get_xticklabels(), rotation=0) 
plt.setp(ax.get_yticklabels(), rotation=90, va='center') 

cbar = ax.collections[0].colorbar
cbar.ax.yaxis.set_tick_params(color=text_color, labelcolor=text_color)
cbar.set_label('% of annual rev', color=text_color, fontweight='bold', fontsize=12)


# ---------------------------------------------------------
# 5. THÊM VẠCH PHÂN CHIA CÁC MÙA (Y HỆT ẢNH SỐ 2)
# ---------------------------------------------------------
weeks = list(heatmap_data.columns)

def get_index(week_num):
    """Hàm phụ trợ để lấy chính xác index cột của tuần cần vẽ"""
    if week_num in weeks:
        return weeks.index(week_num)
    return -1

# Xác định index cho 4 mùa
spring_idx = get_index(13)
summer_idx = get_index(26)
fall_idx = get_index(39)
winter_idx = get_index(52)

season_indices = [spring_idx, summer_idx, fall_idx, winter_idx]
season_names = ['Bắt đầu Mùa Xuân', 'Bắt đầu Mùa Hè', 'Bắt đầu Mùa Thu', 'Bắt đầu Mùa Đông']

for idx, name in zip(season_indices, season_names):
    if idx != -1:
        # Kẻ vạch xanh dương đậm, nét đứt
        ax.axvline(x=idx, color='blue', linewidth=3, linestyle='--')
        # Điền chữ tên mùa
        ax.text(idx + 0.5, -0.2, name, color='blue', fontweight='bold', ha='left', va='center', fontsize=11)


# ---------------------------------------------------------
# 6. LƯU VÀ HIỂN THỊ
# ---------------------------------------------------------
plt.tight_layout()
plt.savefig('heatmap_light_theme_with_seasons.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), transparent=False)
print("Đã lưu biểu đồ thành công vào file 'heatmap_light_theme_with_seasons.png'")