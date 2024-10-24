import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def show_image(title, image):
    """Hiển thị ảnh với tiêu đề."""
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def negative_image(image):
    """Chuyển ảnh sang âm tính."""
    negative = 255 - image
    return negative

def contrast_enhancement(image):
    """Tăng độ tương phản của ảnh bằng phương pháp CLAHE."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)

    lab = cv2.merge((l, a, b))
    enhanced_image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    return enhanced_image

def log_transform(image):
    """Thực hiện phép biến đổi log trên ảnh."""
    c = 255 / np.log(1 + np.max(image))
    log_image = c * np.log(1 + image)
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def histogram_equalization(image):
    """Cân bằng Histogram cho ảnh."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    return equalized

# Mở hộp thoại chọn file để chọn ảnh
Tk().withdraw()  # Ẩn cửa sổ gốc của Tkinter
file_path = askopenfilename(title="Chọn một ảnh", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])

# Kiểm tra xem người dùng đã chọn file hay chưa
if not file_path:
    print("Bạn chưa chọn file ảnh.")
else:
    # Đọc ảnh đầu vào
    image = cv2.imread(file_path)

    if image is None:
        print("Không thể đọc ảnh từ đường dẫn đã cung cấp.")
    else:
        # 1. Ảnh âm tính
        negative = negative_image(image)
        show_image('Ảnh âm tính', negative)

        # 2. Tăng độ tương phản
        contrast = contrast_enhancement(image)
        show_image('Tăng độ tương phản', contrast)

        # 3. Biến đổi log
        log_transformed = log_transform(image)
        show_image('Biến đổi log', log_transformed)

        # 4. Cân bằng Histogram
        equalized = histogram_equalization(image)
        show_image('Cân bằng Histogram', equalized)