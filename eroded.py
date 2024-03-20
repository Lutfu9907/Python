import cv2

I=cv2.imread('fig1.jpg',-1)
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(20,30))
I2=cv2.erode(I,se)

cv2.imshow('Orj',I)
cv2.imshow('eroded',I2)
cv2.waitKey(0)
cv2.destroyAllWindows()
