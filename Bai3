import tensorflow_datasets as tfds
import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
import time

# 1. Tải và chuẩn bị dữ liệu ảnh chó mèo
DATASET_DIR = "animal_dataset"
os.makedirs(DATASET_DIR, exist_ok=True)

dataset, info = tfds.load("cats_vs_dogs", split="train", with_info=True)
images = []
labels = []

# Tạo dữ liệu và lưu về thư mục local
for i, example in enumerate(dataset.take(50)):  # Tải 500 ảnh mẫu
    label = example['label'].numpy()
    img = example['image'].numpy()
    img = cv2.resize(img, (64, 64))  # resize ảnh về 64x64
    
    images.append(img.flatten())
    labels.append(label)

# 2. Chia tập train và test
X_train, X_test, y_train, y_test = train_test_split(np.array(images), np.array(labels), test_size=0.2, random_state=42)

# 3. Định nghĩa mô hình
models = {
    "SVM": SVC(),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier()
}

# 4. Hàm đánh giá mô hình
def evaluate_model(model, X_train, X_test, y_train, y_test):
    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    
    return training_time, accuracy, precision, recall

# 5. Huấn luyện và đánh giá các mô hình
results = {}
for model_name, model in models.items():
    training_time, accuracy, precision, recall = evaluate_model(model, X_train, X_test, y_train, y_test)
    results[model_name] = {
        "Time": training_time,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall
    }

# 6. In kết quả
print("Kết quả đánh giá cho dataset con vật (chó, mèo):")
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    print(f"Time: {metrics['Time']:.4f} seconds")
    print(f"Accuracy: {metrics['Accuracy']:.4f}")
    print(f"Precision: {metrics['Precision']:.4f}")
    print(f"Recall: {metrics['Recall']:.4f}")
    print("-" * 30)
