import cv2
import numpy as np

I=cv2.imread('circles.png',-1)
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))
I2=cv2.erode(I,se)
I3=cv2.dilate(I,se)
I4=cv2.morphologyEx(I,cv2.MORPH_OPEN,se)
I5=cv2.morphologyEx(I,cv2.MORPH_CLOSE,se)
I5_test1=cv2.morphologyEx(I,cv2.MORPH_DILATE,se)
I5_test2=cv2.morphologyEx(I5_test1,cv2.MORPH_ERODE,se)

print(np.sum(np.sum(I5-I5_test2)))
print(se.shape)
print(se.dtype)
print(se)
cv2.imshow('Kernel',se*255)

cv2.imshow('Orj',I)
cv2.imshow('closing',I5)
cv2.imshow('closing 2',I5_test2)
cv2.waitKey(0)
cv2.destroyAllWindows()