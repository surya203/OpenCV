import cv2
import numpy as np

img=cv2.imread("mylogo.png",1)
#To show img
cv2.namedWindow('logo', cv2.WINDOW_NORMAL)
cv2.imshow('logo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
