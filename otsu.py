import numpy as np
import cv2
import pylab as pl
import matplotlib.pyplot as plt

I=cv2.imread('coins.png',0)
th,I2=cv2.threshold(I,127,255,cv2.THRESH_BINARY)
mask=np.zeros((I.shape[0]+2,I.shape[1]+2),np.uint8)
I3=I2.copy()
cv2.floodFill(I3,mask,(0,0),255)
I4=cv2.bitwise_not(I3)
I5=I2|I4
I6=cv2.bitwise_or(I2,I4)

cv2.imshow('I',I)
cv2.imshow('I2',I2)
cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.imshow('I5',I5)
cv2.imshow('I6',I6)
cv2.waitKey(0)
cv2.destroyAllWindows()

aaa=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(aaa)
bbb=aaa>5
print(bbb)
print(type(bbb))
print(bbb.dtype)
aaa[bbb]=88
print(aaa)

I7=np.bool_(I6)
I6[I7]=127
cv2.imshow('I6',I6)
cv2.waitKey(0)
cv2.destroyAllWindows()

kkk=np.array([[0,1,2],[4,0,8],[1,0,0]])
print(kkk)
print(np.bool_(kkk))

I5=cv2.morphologyEx(I4,cv2.MORPH_CLOSE,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(15,15)))
I6=cv2.morphologyEx(I4,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))

xy=np.column_stack(np.where(I6>0))
I7=I6[np.min(xy[:,0]):np.max(xy[:,0]+1),np.min(xy[:,1]):np.max(xy[:,1]+1)]


cv2.imshow('I4',I4)
cv2.imshow('I5',I5)
cv2.imshow('I6',I6)
cv2.waitKey(0)
cv2.destroyAllWindows()