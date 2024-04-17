import numpy as np
import cv2
import pylab as pl
import matplotlib.pyplot as plt

I=cv2.imread('threshold.jpg',0)
print(I.shape)

tvalue,I_tresh1=cv2.threshold(I,127,255,cv2.THRESH_BINARY)
tvalue2,I_tresh2=cv2.threshold(I,190,255,cv2.THRESH_BINARY)
tvalue3,I_tresh3=cv2.threshold(I,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(tvalue3)

cv2.imshow('I',I)
cv2.imshow('thresh',I_tresh1)
cv2.imshow('thresh',I_tresh2)
cv2.imshow('thresh otsu',I_tresh3)

cv2.waitKey(0)
cv2.destroyAllWindows()