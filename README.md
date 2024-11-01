Bài 1: Tăng Cường Ảnh

	Mô tả
 		Chương trình thực hiện các thao tác cơ bản để tăng cường ảnh:
		1. Ảnh âm tính: Đảo ngược giá trị pixel của ảnh.
		2. Tăng độ tương phản: Sử dụng phương pháp CLAHE để cải thiện độ tương phản.
		3. Biến đổi log: Tăng cường độ sáng ở các vùng tối.
		4. Cân bằng Histogram: Phân phối lại giá trị độ sáng để tăng cường độ tương phản.
	Yêu cầu
 		Python
	 	Thư viện: opencv-python, numpy, matplotlib, tkinter
	Hướng dẫn sử dụng
 		Chạy chương trình và chọn ảnh từ hệ thống.
	 	Kết quả bao gồm các phiên bản ảnh sau khi áp dụng các thao tác trên.

Bài 2: Dò Biên Ảnh

	Mô tả
 		Chương trình áp dụng các phương pháp dò biên trên ảnh:
		1. Dò biên Sobel: Dò biên theo các hướng x và y.
		2. Laplace Gaussian (LoG): Làm mượt ảnh bằng Gaussian trước khi áp dụng toán tử Laplacian để dò biên.
	Yêu cầu
		Python
		Thư viện: opencv-python, numpy, matplotlib
	Hướng dẫn sử dụng
		Chạy chương trình và chọn ảnh.
		Kết quả hiển thị các biên của ảnh bằng phương pháp Sobel và Laplacian.
  

Bài 3: Phân Loại Hình Ảnh Chó Mèo

	Mô tả
		Chương trình phân loại ảnh chó và mèo bằng cách sử dụng ba mô hình học máy:
		1. SVM (Support Vector Machine)
		2. K-Nearest Neighbors (KNN)
		3. Decision Tree (Cây Quyết Định)
	Quy trình
		1. Tải và chuẩn bị dữ liệu: Tải dữ liệu chó mèo từ tensorflow_datasets, sau đó resize ảnh về 64x64 và chuyển đổi sang định dạng phù hợp.
		2. Chia tập train và test: Sử dụng train_test_split để chia dữ liệu thành tập huấn luyện và kiểm tra.
		3. Huấn luyện và đánh giá mô hình: Áp dụng từng mô hình và đánh giá dựa trên các chỉ số accuracy, precision, recall, và thời gian huấn luyện.
	Yêu cầu
		Python 3.x
		Thư viện: tensorflow_datasets, opencv-python, numpy, scikit-learn
	Hướng dẫn sử dụng
		Chạy chương trình.
		Chương trình sẽ tải dữ liệu, huấn luyện và đánh giá từng mô hình, sau đó in ra kết quả.
