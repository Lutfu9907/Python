import cv2

I=cv2.imread('fig1.jpg',-1)
print(I.shape)

se=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(35,35))
I2=cv2.erode(I,se)
I3=cv2.dilate(I,se)
I4=cv2.morphologyEx(I,cv2.MORPH_OPEN,se)

cv2.imshow('Orj',I)
cv2.imshow('opening',I4)
cv2.waitKey(0)
cv2.destroyAllWindows()