import cv2
import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
from time import time

# Khởi tạo bộ trích xuất HOG của OpenCV
hog_descriptor = cv2.HOGDescriptor(
    _winSize=(64, 128),
    _blockSize=(16, 16),
    _blockStride=(8, 8),
    _cellSize=(8, 8),
    _nbins=9
)

# Hàm này trích xuất đặc trưng HOG từ một ảnh
def extract_hog_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (64, 128))  # Kích thước chuẩn cho bộ HOG
    features = hog_descriptor.compute(image).flatten()  # Tính HOG và chuyển về mảng 1D
    return features

# Hàm tải dữ liệu huấn luyện từ file và tính đặc trưng HOG cho từng ảnh
def load_training_data(file_path='train_data.txt'):
    features = []
    labels = []
    with open(file_path, 'r') as f:
        for line in f:
            *feature_values, label = line.strip().split(',')
            features.append(list(map(float, feature_values)))  # Chuyển đổi các giá trị đặc trưng sang float
            labels.append(label)
    return np.array(features), np.array(labels)

# Hàm huấn luyện và đánh giá mô hình
def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    start_time = time()
    model.fit(X_train, y_train)
    training_time = time() - start_time

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Tính toán precision và recall với zero_division để tránh cảnh báo
    precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)

    # In báo cáo phân loại để xem các chỉ số cho từng nhãn
    report = classification_report(y_test, y_pred, zero_division=0)
    print(report)

    return training_time, accuracy, precision, recall

# Hàm chính
def main():
    # Bước 1: Tải dữ liệu huấn luyện với đặc trưng HOG
    features, labels = load_training_data('train_data.txt')

    # Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
    split_ratio = 0.8
    split_index = int(len(features) * split_ratio)
    X_train, X_test = features[:split_index], features[split_index:]
    y_train, y_test = labels[:split_index], labels[split_index:]

    # Khởi tạo các mô hình
    models = {
        "SVM": SVC(),
        "KNN": KNeighborsClassifier(n_neighbors=15),
        "Decision Tree": DecisionTreeClassifier()
    }

    # Huấn luyện và đánh giá từng mô hình
    for model_name, model in models.items():
        training_time, accuracy, precision, recall = train_and_evaluate_model(model, X_train, y_train, X_test, y_test)
        print(f"\nModel: {model_name}")
        print(f"Training Time: {training_time:.4f} seconds")
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print(f"Precision: {precision * 100:.2f}%")
        print(f"Recall: {recall * 100:.2f}%")

    # Dự đoán nhãn cho một ảnh đầu vào với từng mô hình
    input_image_path = '/XLA/New2/input3.jpg'
    input_features = extract_hog_features(input_image_path).reshape(1, -1)
    for model_name, model in models.items():
        predicted_label = model.predict(input_features)[0]
        print(f"Predicted Label by {model_name}: {predicted_label}")

# Chạy hàm main
if __name__ == "__main__":
    main()
