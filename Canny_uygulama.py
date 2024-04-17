import numpy as np
import matplotlib.pyplot as plt
import cv2

I=cv2.imread('coins.png',0)
thresh,I2 = cv2.threshold(I,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
mask=np.zeros((I.shape[0]+2,I.shape[1]+2),dtype=np.uint8)
I3=I2.copy()
cv2.floodFill(I3,mask,(0,0),255)
I4=cv2.bitwise_not(I3)
I5=I2|I4

numLabels,labels,stats,centroids=cv2.connectedComponentsWithStats(I5)

areas=stats[1:,[4]]
big_label=np.argmax(areas)+1
print('en buyuk para etiketi=',big_label)

big_coin=np.uint8(labels==big_label)*255
big_coin_edge=cv2.Canny(big_coin,100,200)
indis=np.bool_(big_coin_edge)

I_bgr=np.zeros((I.shape[0],I.shape[1],3),dtype=np.uint8)
I_bgr[:,:,0]=I_bgr[:,:,1]=I_bgr[:,:,2]=I
I_bgr[indis]=[0,0,255]

cv2.imshow('Orj',I)
cv2.imshow('Sonuc',I_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()