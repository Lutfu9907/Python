import numpy as np
import matplotlib.pyplot as plt
import cv2
import pylab as pl

I=cv2.imread('blobs.jpg',0)
I2=cv2.bitwise_or(I)
print(I2.dtype)

tt,I2 =cv2.threshold(I2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
I5 =cv2.warpAffine(I2,np.array([-1,0,1],[-1,0,0]),-1)

I3=cv2.Sobel(I2,ddepth=cv2.CV_64F,dx=-1,dy=0,ksize=5)
I4=cv2.Sobel(I2,ddepth=cv2.CV_64F,dx=-1,dy=1,ksize=5) #-1 orjinaline dokunma anlamında kullanıldı
I5=cv2.Sobel(I2,ddepth=cv2.CV_64F,dx=-1,dy=1,ksize=5)

cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('I3',I3)
cv2.imshow('I4',I4)

cv2.waitKey(0)
cv2.destroyAllWindows()
