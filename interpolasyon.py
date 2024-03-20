import cv2
import numpy as np

I=cv2.imread('peppers.png',1)
print(I.shape)
I2=cv2.resize(I,(3840,2160),interpolation=cv2.INTER_CUBIC)
I2=cv2.resize(I2,(512,384))
print(I2.shape)

I3=cv2.resize(I,None,fx=0.5,fy=1.5)
print(I3.shape)

I4=I[50:100,370:430]
I5=I[280:330,400:500]
print(I4.shape)
print(I5.shape)

cv2.imshow('orijinal',I)
#cv2.imshow('I2',I2)
#cv2.imshow('I3',I3)
#cv2.imshow('I4',I4)
cv2.imshow('I5',I5)
cv2.waitKey(0)
cv2.destroyAllWindows()
