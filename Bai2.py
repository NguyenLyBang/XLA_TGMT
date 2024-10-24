import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
image = cv2.imread('c:/Users/nguye/OneDrive/Pictures/HA/020.jpg', cv2.IMREAD_GRAYSCALE)

# 1. Dò biên với toán tử Sobel
# Áp dụng toán tử Sobel theo hướng x và y
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel theo hướng x
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel theo hướng y

# Tổng hợp biên bằng cách kết hợp kết quả của Sobel X và Y
sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)

# 2. Dò biên với toán tử Laplacian of Gaussian (LoG)
# Lọc Gaussian để làm mượt ảnh trước khi áp dụng Laplacian
blurred_image = cv2.GaussianBlur(image, (3, 3), 0)
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F, ksize=3)

# 3. Hiển thị kết quả
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
plt.title('Original Image'), plt.axis('off')

plt.subplot(2, 2, 2), plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Edge Detection'), plt.axis('off')

plt.subplot(2, 2, 3), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian of Gaussian'), plt.axis('off')

plt.show()
