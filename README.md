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

Bài 5: Trích Xuất Đặc Trưng HOG và Phân Loại Ảnh

	Mô tả
		Chương trình thực hiện trích xuất đặc trưng HOG (Histogram of Oriented Gradients) để phân loại ảnh trong một tập dữ liệu. Sau đó, sử dụng hai mô hình cây quyết định:
		1. CART (Gini Index): Sử dụng gini để chia nhánh.
		2. ID3 (Information Gain): Sử dụng entropy để chia nhánh.
	Quy trình
		1. Trích xuất đặc trưng HOG: Đọc ảnh từ thư mục, chuyển đổi kích thước và trích xuất đặc trưng HOG.
		2. Chia dữ liệu: Phân chia thành tập huấn luyện và kiểm tra với train_test_split.
		3. Huấn luyện mô hình: Sử dụng các mô hình CART và ID3 để huấn luyện trên tập train và dự đoán trên tập test.
		4. Đánh giá mô hình: Sử dụng accuracy_score và confusion_matrix để đánh giá kết quả.
	Yêu cầu
		Python 3.x
		Thư viện: skimage, numpy, scikit-learn
	Hướng dẫn sử dụng
		Đặt thư mục chứa ảnh cần phân loại vào đường dẫn được chỉ định.
		Chạy chương trình để trích xuất đặc trưng và đánh giá mô hình.

Bài 6: Phân Cụm Ảnh Vệ Tinh Bằng KMeans và Fuzzy C-Means (FCM)

	Mô tả
		Phân cụm ảnh vệ tinh để nhận diện các khu vực có nhà ở:
		1. KMeans Clustering: Sử dụng thuật toán KMeans để phân cụm ảnh thành hai khu vực (nhà và nền).
		2. Fuzzy C-Means (FCM): Sử dụng thuật toán FCM để phân cụm ảnh thành hai khu vực với cách tiếp cận mềm dẻo hơn (fuzzy).
	Quy trình
		1. Tiền xử lý ảnh: Đọc ảnh vệ tinh, chuyển đổi sang RGB, thay đổi kích thước và chuyển thành dạng mảng 2D.
		2. Phân cụm:
			a) KMeans: Phân cụm và xác định cụm nào là nhà dựa trên giá trị trung bình màu.
			b) FCM: Tương tự như KMeans, nhưng áp dụng phương pháp phân cụm mờ.
		3. Hiển thị kết quả: So sánh kết quả phân cụm của KMeans và FCM.
	Yêu cầu
		Python 3.x
		Thư viện: opencv-python, numpy, matplotlib, skfuzzy, scikit-learn
