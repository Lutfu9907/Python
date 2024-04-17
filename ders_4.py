import numpy as np
import cv2
import pylab as pl
import matplotlib.pyplot as plt

I=cv2.imread('peppers.png',0)
I_eq=cv2.equalizeHist(I)
clahe1=cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))
I_clahe=clahe1.apply(I)

cv2.imshow('I combined',np.concatenate((I,I_clahe),axis=1))
cv2.waitKey(0)
cv2.destroyAllWindows()

I_hist=cv2.calcHist([I],[0],None,[256],(0,256))
I_eq_hist=cv2.calcHist([I_clahe],[0],None,[256],(0,256))

plt.plot(I_hist,'b')
#plt.plot(I_eq,'r')
plt.plot(I_clahe,'r')
plt.waitforbuttonpress()
plt.show()
plt.close()

