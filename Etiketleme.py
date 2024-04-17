import numpy as np
import matplotlib.pyplot as plt
import cv2
import pylab as pl
import time

I = cv2.imread('coins.png', 0)
th,I2=cv2.threshold(I,0,255,cv2.THRESH_BINARY+ cv2.THRESH_OTSU)
print(th)
count,I3,stats,xy=cv2.connectedComponentsWithStats(I2)

print('daire sayısı:',count-1)
print(I3.dtype)
print(I3.shape)
print(stats)
print(xy)



cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('1.madeni para', np.uint8(I3==1)*255)
cv2.imshow('2.madeni para', np.uint8(I3==2)*255)

cv2.waitKey(0)
cv2.destroyAllWindows()


for i in range(1,count):
     cv2.imshow('madeni para', np.uint8(I3 == i) * 255)
     cv2.waitKeyEx(1000)
