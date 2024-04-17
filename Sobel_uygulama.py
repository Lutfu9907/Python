import numpy as np
import matplotlib.pyplot as plt
import cv2

# 'blobs.jpg' adlı siyah beyaz bir resim dosyası 'I' değişkenine okunur.
I = cv2.imread('blobs.jpg', 0)

# Otsu'nun ikili segmentasyon yöntemi kullanılarak eşik değeri hesaplanır ve resim ikili hale getirilir.
_, I2 = cv2.threshold(I, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Sobel kenar tespiti uygulanır.
I3 = cv2.Sobel(I2, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
I4 = cv2.Sobel(I2, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

# Orijinal resim ve işlenmiş resimlerin gösterilmesi.
cv2.imshow('Original', I)
cv2.imshow('Thresholded', I2)
cv2.imshow('Sobel X', I3)
cv2.imshow('Sobel Y', I4)

# Pencere kapatma işlemleri yapılır.
cv2.waitKey(0)
cv2.destroyAllWindows()
