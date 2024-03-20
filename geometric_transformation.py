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

aff=cv2.getRotationMatrix2D((I.shape[1]//2,I.shape[0]//2),45,1)
print(aff)
print(np.array([[np.cos(np.pi/4),np.sin(np.pi/4)],[-np.sin(np.pi/4),np.cos(np.pi/4)]]))

I6=cv2.warpAffine(I,aff,None)

height,width=I4.shape[:2]
input_pts = np.float32([[0,0], [width-1,0], [0,height-1]])
output_pts = np.float32([[width-1,0], [0,0], [width-1,height-1]])
M=cv2.getAffineTransform(input_pts,output_pts)
print(M)
I7=cv2.warpAffine(I,M,None)


cv2.imshow('orijinal',I)
#cv2.imshow('I2',I2)
#cv2.imshow('I3',I3)
#cv2.imshow('I4',I4)
#cv2.imshow('I5',I5)
#cv2.imshow('I6',I6)
cv2.imshow('I7',I7)
cv2.waitKey(0)
cv2.destroyAllWindows()

