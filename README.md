# Datathon 2026 - Phân Tích & Dự Báo Thị Trường TMĐT

Dự án phân tích và dự báo thị trường cho nền tảng thương mại điện tử Việt Nam, sử dụng các kỹ thuật học máy và phân tích dữ liệu nâng cao.

## 📁 Cấu Trúc Thư Mục

```
datathon-2026/
├── src/                          # Source code for analysis and modeling
│   ├── part1.ipynb              # Data Cleaning & Exploratory Data Analysis
│   ├── part3.ipynb              # Advanced Analysis
│   └── part 2/                  # Feature Engineering & Modeling
│       ├── gross_margin_insights.ipynb     # Gross Margin Analysis
│       ├── macro_insight.ipynb              # Macro Market Insights
│       ├── macro_visualization.png          # Macro Visualization
│       ├── revenue_heatmap_visualization.py # Revenue Heatmap
│       └── revenue_visualization_2.py       # Revenue Visualization
├── data/                        # Input Data (CSV files)
│   ├── products.csv            # Product Information
│   ├── customers.csv           # Customer Information
│   ├── orders.csv              # Order Data
│   ├── order_items.csv         # Order Item Details
│   ├── sales.csv               # Daily Sales Data
│   ├── inventory.csv           # Inventory Data
│   ├── payments.csv            # Payment Information
│   ├── returns.csv             # Return Data
│   ├── reviews.csv             # Customer Reviews
│   ├── promotions.csv          # Promotion Information
│   ├── geography.csv           # Geography Data
│   ├── shipments.csv           # Shipping Information
│   ├── web_traffic.csv         # Web Traffic Data
│   └── sample_submission.csv   # Sample Submission File
├── docs/                        # Documentation & Reports
│   ├── report.md               # Detailed Results Report
│   └── deleteme.txt            # Temporary File
├── output/                      # Output Results & Visualizations
└── README.md                    # This Documentation
```

## 🎯 Mục Tiêu Dự Án

1. **Phân tích dữ liệu (EDA):** Khám phá xu hướng, mô hình và bất thường trong dữ liệu
2. **Kỹ thuật đặc trưng (Feature Engineering):** Tạo biến phái sinh để cải thiện hiệu suất
3. **Mô hình hóa (Modeling):** Xây dựng mô hình dự báo doanh thu và bán hàng
4. **Trực quan hóa (Visualization):** Tạo biểu đồ để giải thích kết quả
5. **Giải thích mô hình (Explainability):** Sử dụng SHAP để diễn giải quyết định

## 📊 Các Phần Chính

### Phần 1: Làm sạch dữ liệu & EDA
- Kiểm tra tính toàn vẹn dữ liệu
- Xử lý giá trị khuyết thiếu
- Khám phá mô hình và bất thường
- Tạo thống kê mô tả

### Phần 2: Kỹ thuật đặc trưng & Mô hình hóa
- **Phân tích lợi nhuận gộp:** Insight về gross margin
- **Phân tích vĩ mô:** Chỉ số thị trường chính
- **Trực quan hóa:** Heatmap doanh thu và insights

### Phần 3: Phân tích nâng cao
- Phân tích sâu và dự báo tương lai

## 🔧 Hướng Dẫn Chạy

### Yêu Cầu Hệ Thống
- Python 3.8 trở lên
- pandas, numpy, matplotlib, seaborn
- scikit-learn, xgboost, lightgbm (cho mô hình)
- SHAP (cho giải thích mô hình)

### Cài Đặt Gói Thư Viện
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm shap jupyter
```

### Chạy Notebooks
```bash
# Chạy Phần 1
jupyter notebook src/part1.ipynb

# Chạy Phần 2
jupyter notebook src/part\ 2/macro_insight.ipynb

# Chạy Phần 3
jupyter notebook src/part3.ipynb
```

## 📈 Các Insight Chính

Dự án tập trung vào phân tích:
- **Doanh thu theo thời gian:** Xu hướng năm, tháng
- **Tồn kho:** Phân tích vấn đề về tồn kho
- **Giá trị đơn hàng (AOV):** Average Order Value phân tích
- **Lợi nhuận gộp:** Phân tích theo danh mục
- **Dự báo:** Dự đoán bán hàng tương lai

## 📝 Lưu Ý

- Tất cả file dữ liệu CSV nằm trong thư mục `data/`
- Notebooks sử dụng đường dẫn tương đối `../data/` để tải dữ liệu
- Output visualization lưu trong thư mục `output/`
- Báo cáo chi tiết xem tại `docs/report.md`

## 👤 Tác Giả

Datathon 2026 Project

## 📄 Giấy Phép

Dự án này được tạo cho mục đích phân tích dữ liệu và học tập.