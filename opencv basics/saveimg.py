import cv2
import numpy as np

img=cv2.imread("mylogo.png",1)
#To show img
cv2.namedWindow('logo', cv2.WINDOW_NORMAL)
cv2.imshow('logo',img)
cv2.imwrite("mylogo1.jpg",img)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
if k== ord("s"):
	cv2.imwrite("mylogo2.png",img)
	cv2.destroyAllWindows()
else:
	print("error")
	
