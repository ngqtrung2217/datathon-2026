# Datathon 2026: Retail Data Analytics & Financial Forecasting

## Tác giả - Team Chobua

- **Nguyễn Chu Hùng Anh** - [Leader]
- **Phạm Đức Tuấn** - [Member]
- **Nguyễn Kim Hải Đăng** - [Member]
- **Nguyễn Quang Trung** - [Member]

---

## Mục lục

1. [Tổng quan dự án](#tổng-quan-dự-án)
2. [Mục tiêu chính](#mục-tiêu-chính)
3. [Cấu trúc thư mục](#cấu-trúc-thư-mục)
4. [Phương pháp tiếp cận](#phương-pháp-tiếp-cận)
5. [Hướng dẫn khởi động](#hướng-dẫn-khởi-động)
6. [Kết quả đạt được](#kết-quả-đạt-được)

---

## Tổng quan dự án

Dự án phân tích dữ liệu bán lẻ đa kênh và xây dựng hệ thống dự báo tài chính (Revenue & COGS) nhằm tối ưu hóa quyết định kinh doanh dựa trên dữ liệu.

Dự án tập trung vào việc khai thác kho dữ liệu bán lẻ đa dạng để trích xuất các thông tin giá trị về hành vi khách hàng, tối ưu hóa danh mục sản phẩm và dự báo các chỉ số tài chính cốt lõi. Chúng tôi kết hợp các phương pháp phân tích thống kê truyền thống với các mô hình học máy hiện đại (LightGBM) để đưa ra các dự báo có độ chính xác cao.

## Mục tiêu chính

1.  **Phân tích Hiệu suất Kinh doanh:**
    - Đo lường hành vi khách hàng (chu kỳ mua hàng, khoảng cách giữa các đơn hàng).
    - Phân tích biên lợi nhuận (Gross Margin) theo phân khúc sản phẩm.
    - Đánh giá hiệu quả của các chiến dịch khuyến mãi.
2.  **Dự báo Tài chính (Forecasting):**
    - Dự báo Doanh thu (Revenue) sử dụng phương pháp **Mathematical Median with Shrinkage**.
    - Dự báo Giá vốn hàng bán (COGS) thông qua mô hình dự đoán tỷ lệ (Ratio) để đảm bảo tính ổn định.

## Cấu trúc thư mục

```text
datathon/
├── data/               # Dữ liệu thô (14+ file CSV: Sales, Products, Customers, etc.)
├── output/             # Kết quả dự báo (submission.csv) và biểu đồ phân tích (SHAP)
├── src/
│   ├── part1.ipynb     # EDA & Giải quyết các bài toán Business Intelligence
│   ├── part 2/         # Visualization chuyên sâu về Gross Margin & Macro Insights
│   └── part3.ipynb     # Pipeline huấn luyện mô hình & Forecasting chuyên sâu
└── requirements.txt    # Danh sách các thư viện cần thiết
```

## Phương pháp tiếp cận

### 1. Kỹ thuật tính năng (Feature Engineering)

- **Tích hợp dữ liệu:** Kết nối dữ liệu từ nhiều nguồn khác nhau để xây dựng bức tranh toàn cảnh về hoạt động kinh doanh.
- **Time-series Engineering:** Trích xuất các đặc trưng thời gian như Seasonality, Holidays, Weekends và các sự kiện đặc thù (ví dụ: `urban_blowout_odd`).

### 2. Mô hình hóa (Modeling Strategy)

- **Revenue Forecasting:** Áp dụng kỹ thuật **Shrinkage 7%** trên nền tảng trung vị (Median) để giảm thiểu tác động của nhiễu và các giá trị ngoại lai, giúp dự báo xu hướng bền vững hơn.
- **COGS Forecasting:** Sử dụng mô hình **LightGBM Ensemble** với kỹ thuật **Bagging** qua nhiều `seeds` (42, 7, 123). Mô hình tập trung dự đoán _tỷ lệ COGS/Revenue_ để giữ được tính tương quan logic giữa hai đại lượng này.

### 3. Giải thích mô hình (Model Interpretability)

- Tích hợp **SHAP (SHapley Additive exPlanations)** để minh bạch hóa các yếu tố ảnh hưởng đến dự báo. Điều này giúp bộ phận kinh doanh hiểu rõ tại sao mô hình đưa ra kết quả đó (ví dụ: yếu tố ngày trong tuần hay sự kiện đặc biệt tác động thế nào đến biên lợi nhuận).

## Hướng dẫn khởi động

1.  **Cài đặt thư viện:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Thực thi pipeline:**
    - Khám phá dữ liệu và giải quyết câu hỏi nghiệp vụ tại [src/part1.ipynb](src/part1.ipynb).
    - Huấn luyện mô hình và xuất kết quả tại [src/part3.ipynb](src/part3.ipynb).
    - Kết quả cuối cùng sẽ được lưu tại `output/submission.csv`.

## Kết quả đầu ra

- Hệ thống dự báo có khả năng thích ứng linh hoạt với các biến động thị trường theo mùa.
- Insights về biên lợi nhuận giúp doanh nghiệp định vị lại các nhóm sản phẩm chiến lược.
- Cung cấp file kết quả đạt chuẩn yêu cầu cho bài toán Datathon.

---

_Dự án được thực hiện bởi đội ngũ phân tích dữ liệu chuyên nghiệp tại Datathon 2026._

- Notebooks sử dụng đường dẫn tương đối `../data/` để tải dữ liệu
- Output visualization lưu trong thư mục `output/`
