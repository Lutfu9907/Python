import numpy as np
import cv2
from matplotlib import pyplot as plt

I=cv2.imread('peppers.png',1)
M=np.array([[2,0,0],[0,0.5,0]],dtype=np.float32)
M2=np.array([[1,0,100],[0,1,50]],dtype=np.float32)
height,width=I.shape[0:2]
I2=cv2.warpAffine(I,M,(width*2,height//2))
I3=cv2.warpAffine(I,M2,None)


# print(I.shape)
# print(I2.shape)
# cv2.imshow('I',I)
# cv2.imshow('I2',I2)
# cv2.imshow('I3',I3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

I=cv2.imread('cameraman.tif',-1)
print(I.shape)

print('min',np.min(I))
print('max',np.max(I))
print('mean',np.mean(I))
I2=I+50
I3=I-50

I2[I2>255]=255
I2[I2<0]=0
I3[I3>255]=255
I3[I3<0]=0
I2=np.uint8(I2)
I3=np.uint8(I3)

print('min2',np.min(I2))
print('max2',np.max(I2))
print('mean2',np.mean(I2))

print('min3',np.min(I3))
print('max3',np.max(I3))
print('mean3',np.mean(I3))

I4=255-I
I5=255-np.int8(I)
I5=np.int8(I5)

# I6=cv2.calcHist([I],[0],None,[256],(0,256))
# plt.plot(I6,'red')
# plt.hist(I.ravel(),256,(0,256))
# plt.waitforbuttonpress()
# plt.close()

I7_orj=cv2.imread('peppers.png',1)
colors=('b','g','r')
for i,renk in enumerate(colors):
    I7=cv2.calcHist([I7_orj],[i],None,[256],(0,256))
    plt.plot(I7,color=renk)
plt.waitforbuttonpress()
plt.close()

cv2.imshow('I',I)
# cv2.imshow('I2',I2)
# cv2.imshow('I3',I3)
#cv2.imshow('I4',I4)
#cv2.imshow('I6',I6)
cv2.waitKey(0)
cv2.destroyAllWindows()