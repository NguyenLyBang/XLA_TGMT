import cv2
import numpy as np
from matplotlib import pyplot as plt

# Đọc ảnh đầu vào
img = cv2.imread('input_image.jpg', 0)  # Đọc ảnh ở dạng grayscale (ảnh xám)

# ------------------- Toán tử Sobel -------------------
# Dò biên Sobel theo trục X và Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Gradient theo X
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Gradient theo Y

# Tổng hợp kết quả bằng cách tính độ lớn của gradient
sobel_combined = cv2.magnitude(sobelx, sobely)

# ------------------- Toán tử Laplace of Gaussian (LoG) -------------------
# Áp dụng làm mịn Gaussian để giảm nhiễu trước khi dùng Laplace
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Sử dụng toán tử Laplace để dò biên
laplacian = cv2.Laplacian(gaussian_blur, cv2.CV_64F, ksize=5)

# ------------------- Hiển thị kết quả -------------------
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Ảnh gốc'), plt.axis('off')

plt.subplot(2, 2, 2), plt.imshow(sobel_combined, cmap='gray')
plt.title('Dò biên Sobel'), plt.axis('off')

plt.subplot(2, 2, 3), plt.imshow(laplacian, cmap='gray')
plt.title('Dò biên Laplace of Gaussian'), plt.axis('off')

plt.show()
