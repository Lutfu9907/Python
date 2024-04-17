import numpy as np
import matplotlib.pyplot as plt
import cv2
import pylab as pl

I = cv2.imread('peppers.png', -1)
I2 = (I[:,:,0]>220)&(I[:,:,1]>220)&(I[:,:,2]>220)
print(I2.dtype)
I3= np.uint8(I2)*255
I4=cv2.morphologyEx(I3,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10)))
print(I4.dtype)
indis=np.bool_(I4)
Inew=I.copy()
Inew[indis,0]=200
Inew[indis,1]=214
Inew[indis,2]=48

cv2.imshow('I',I)
cv2.imshow('I3',I3)
cv2.imshow('I4',I4)
cv2.imshow('I new',Inew)
cv2.waitKey(0)
cv2.destroyAllWindows()

