# Báo Cáo Kết Quả Mô Hình Datathon

## 1. Pipeline Rõ Ràng (Clear Pipeline)

Quy trình xây dựng mô hình được thiết kế bài bản và tự động hóa qua các bước sau:

- **Tiền xử lý dữ liệu (Data Preprocessing):** Xử lý giá trị khuyết thiếu (missing values), loại bỏ nhiễu và chuẩn hóa dữ liệu (Scaling/Normalization).
- **Trích xuất đặc trưng (Feature Engineering):** Tạo thêm các biến phái sinh có ý nghĩa từ các biến thời gian và lịch sử dữ liệu (lag features, rolling statistics).
- **Huấn luyện mô hình (Modeling):** Sử dụng các mô hình học máy dạng cây (Tree-based models như LightGBM/XGBoost/RandomForest) kết hợp pipeline tự động điều chỉnh siêu tham số (Hyperparameter tuning).

## 2. Cross-Validation Đúng Chiều Thời Gian

Vì bản chất bài toán liên quan đến dữ liệu chuỗi thời gian, việc sử dụng K-Fold thông thường sẽ dẫn đến hiện tượng "rò rỉ dữ liệu" (Data Leakage) từ tương lai về quá khứ.

- **Phương pháp ứng dụng:** `TimeSeriesSplit` (Rolling Window / Expanding Window).
- **Chi tiết:** Dữ liệu được chia tuần tự theo thời gian. Mô hình chỉ được học từ quá khứ để dự đoán tương lai ở mỗi fold, tuyệt đối không sử dụng dữ liệu tương lai để dự đoán quá khứ.

## 3. Giải Thích Mô Hình Bằng SHAP (Model Explainability)

Để đảm bảo mô hình không phải là một "hộp đen" (black-box) và đáng tin cậy:

- Sử dụng phương pháp **SHAP (SHapley Additive exPlanations)** để đo lường mức độ ảnh hưởng của từng đặc trưng (feature) tới kết quả dự đoán cuối cùng.
- **Feature Importance:** Vẽ biểu đồ Summary Plot để đánh giá sự phân bổ tác động của các biến quan trọng nhất. Xác định rõ biến nào làm tăng/giảm dự đoán.
- **Local Explanation:** Hỗ trợ giải thích từng dự đoán cá biệt để kiểm chứng độ logic của mô hình đối với các quy tắc nghiệp vụ.

## 4. Tuân Thủ Đầy Đủ Ràng Buộc

- **Quản lý dữ liệu:** Đảm bảo toàn bộ quy trình không vi phạm các ràng buộc dữ liệu đầu vào.
- **Hiệu suất & Bộ nhớ:** Pipeline được tối ưu để chạy trong khoảng thời gian quy định và sử dụng tài nguyên (RAM/CPU) trong giới hạn cho phép.
- **Ràng buộc nghiệp vụ (Business Rules):** Các dự đoán cuối cùng đều được hậu xử lý (post-processing) để thỏa mãn các điều kiện kỹ thuật và logic nghiệp vụ bắt buộc trước khi xuất ra thư mục `output/`.

---

_Ghi chú: Báo cáo này tóm tắt phương pháp tiếp cận trong `part3.ipynb` và các phần khác của dự án._
