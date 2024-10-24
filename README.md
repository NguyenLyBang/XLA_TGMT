Bài tập 1: Dò biên ảnh bằng Sobel và Laplace of Gaussian (LoG)
Mục tiêu:
Thực hiện dò biên của ảnh sử dụng toán tử Sobel và Laplace Gaussian (LoG).
Phương pháp:
Toán tử Sobel: Tính gradient cường độ ảnh theo hai trục x và y để phát hiện biên.
Laplace of Gaussian (LoG): Kết hợp Gaussian để làm mịn và Laplace để dò biên chính xác hơn trong ảnh có nhiễu.
Kết quả:
Ảnh sau khi được áp dụng Sobel và LoG để tìm biên.
Bài tập 2: Tăng cường ảnh
Mục tiêu:
Thực hiện các thao tác tăng cường ảnh bao gồm:
Ảnh âm tính
Tăng độ tương phản
Biến đổi log
Cân bằng Histogram
Phương pháp:
Ảnh âm tính: Lật ngược mức cường độ pixel.
Tăng độ tương phản: Sử dụng phương pháp CLAHE để cải thiện độ tương phản.
Biến đổi log: Mở rộng giá trị cường độ ở vùng tối.
Cân bằng Histogram: Phân phối lại các giá trị cường độ của ảnh để cân bằng sáng.
Kết quả:
Hiển thị ảnh sau khi áp dụng từng kỹ thuật tăng cường.
Yêu cầu thư viện:
OpenCV
NumPy
Matplotlib
Hướng dẫn chạy:
Chọn ảnh đầu vào thông qua hộp thoại.
Chương trình sẽ thực hiện các thao tác và hiển thị kết quả.
