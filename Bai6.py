import cv2
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import skfuzzy as fuzz

# Hàm đọc ảnh vệ tinh và chuyển về dạng cần thiết cho phân cụm
def load_and_preprocess_image(file_path):
    image = cv2.imread(file_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển từ BGR sang RGB
    image_resized = cv2.resize(image, (200, 200))  # Điều chỉnh kích thước
    flat_image = image_resized.reshape((-1, 3))    # Chuyển về mảng 2D
    flat_image = np.float32(flat_image)            # Chuyển sang kiểu float32
    return image_resized, flat_image

# Hàm phân cụm KMeans (2 cụm: nhà và nền)
def kmeans_clustering(image_data, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(image_data)
    
    # Xác định cụm nào là nhà dựa trên giá trị trung bình màu
    cluster_centers = kmeans.cluster_centers_
    house_label = np.argmin(cluster_centers.sum(axis=1))  # Cụm có giá trị nhỏ nhất sẽ là nhà (màu tối hơn)
    
    # Gán lại nhãn thành 0 (trắng) và 1 (đen) cho nhà
    binary_labels = (labels == house_label).astype(np.uint8)
    segmented_image = binary_labels.reshape(200, 200) * 255
    return segmented_image

# Hàm phân cụm Fuzzy C-Means (FCM) (2 cụm: nhà và nền)
def fuzzy_c_means(image_data, n_clusters=2):
    cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(image_data.T, c=n_clusters, m=2, error=0.005, maxiter=1000, init=None)
    cluster_membership = np.argmax(u, axis=0)
    
    # Xác định cụm nào là nhà dựa trên giá trị trung bình màu
    house_label = np.argmin(cntr.sum(axis=1))  # Cụm có giá trị nhỏ nhất sẽ là nhà (màu tối hơn)
    
    # Gán lại nhãn thành 0 (trắng) và 1 (đen) cho nhà
    binary_labels = (cluster_membership == house_label).astype(np.uint8)
    segmented_image = binary_labels.reshape(200, 200) * 255
    return segmented_image

# Hiển thị kết quả phân cụm
def plot_results(original, kmeans_result, fcm_result, title):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title(f'Ảnh gốc: {title}')

    plt.subplot(1, 3, 2)
    plt.imshow(kmeans_result, cmap='gray')
    plt.title('KMeans Clustering (Nhà - Đen)')

    plt.subplot(1, 3, 3)
    plt.imshow(fcm_result, cmap='gray')
    plt.title('Fuzzy C-Means Clustering (Nhà - Đen)')

    plt.show()

# Đọc và xử lý từng ảnh vệ tinh
image_paths = ["Bai6/1.jpg", "Bai6/2.jpg", "Bai6/3.jpg"]  # Thay thế bằng đường dẫn ảnh của bạn
for idx, path in enumerate(image_paths):
    original_image, flat_image = load_and_preprocess_image(path)
    
    # Phân cụm với KMeans
    kmeans_result = kmeans_clustering(flat_image)
    
    # Phân cụm với FCM
    fcm_result = fuzzy_c_means(flat_image)
    
    # Hiển thị kết quả
    plot_results(original_image, kmeans_result, fcm_result, f"Ảnh {idx + 1}")
