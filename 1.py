import numpy
import cv2
import matplotlib
image=cv2.imread('1.jpg',0);


cv2.imshow('image',image)
image=cv2.imwrite('2.jpg',image);

cv2.waitKey(0)
cv2.destroyAllWindows()

