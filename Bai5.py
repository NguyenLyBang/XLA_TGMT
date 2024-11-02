import os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Định nghĩa hàm trích xuất đặc trưng HOG
def extract_hog_features(image_path):
    image = imread(image_path, as_gray=True)  # Đọc ảnh dưới dạng grayscale
    image = resize(image, (128, 128))  # Chuyển đổi kích thước về 128x128
    features = hog(image, orientations=9, pixels_per_cell=(8, 8),
                   cells_per_block=(2, 2), block_norm='L2-Hys')
    return features

# Đọc toàn bộ ảnh từ thư mục và trích xuất đặc trưng
def load_dataset(directory):
    data = []
    labels = []
    for label_folder in os.listdir(directory):
        label_path = os.path.join(directory, label_folder)
        if os.path.isdir(label_path):
            for image_file in os.listdir(label_path):
                image_path = os.path.join(label_path, image_file)
                features = extract_hog_features(image_path)  # Trích xuất đặc trưng HOG
                data.append(features)
                labels.append(label_folder)  # Sử dụng tên thư mục làm nhãn
    return np.array(data), np.array(labels)

# Đường dẫn tới thư mục chứa ảnh
dataset_directory = 'data/'
X, y = load_dataset(dataset_directory)

# Chia tập dữ liệu thành tập train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Khởi tạo và huấn luyện mô hình CART
cart_model = DecisionTreeClassifier(criterion='gini', random_state=42)
cart_model.fit(X_train, y_train)
y_pred_cart = cart_model.predict(X_test)

# Khởi tạo và huấn luyện mô hình ID3
id3_model = DecisionTreeClassifier(criterion='entropy', random_state=42)
id3_model.fit(X_train, y_train)
y_pred_id3 = id3_model.predict(X_test)

# Đánh giá mô hình
print("CART - Gini Index Accuracy:", accuracy_score(y_test, y_pred_cart))
print("Confusion Matrix (CART):\n", confusion_matrix(y_test, y_pred_cart))
print("\nID3 - Information Gain Accuracy:", accuracy_score(y_test, y_pred_id3))
print("Confusion Matrix (ID3):\n", confusion_matrix(y_test, y_pred_id3))