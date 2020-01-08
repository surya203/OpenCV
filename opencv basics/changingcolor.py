import cv2
import numpy as np

def scroll(x):
	pass
	
img=np.zeros((428,716,3), np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar('Red' ,"image",0,225,scroll)
cv2.createTrackbar('Blue' ,"image",0,225,scroll)
cv2.createTrackbar('Green' ,"image",0,225,scroll)

switch = '0:OFF,1=ON'
cv2.createTrackbar(switch,"image",0,1,scroll)

while(1):
	cv2.imshow("image",img)
	k=cv2.waitKey(1)&0xFF
	if k==27:
		break
		
	r=cv2.getTrackbarPos('Red',"image")
	b=cv2.getTrackbarPos('Blue',"image")
	g=cv2.getTrackbarPos('Green',"image")
	s=cv2.getTrackbarPos(switch,"image")
	
	if s==0:
		img[:]=0
	else:
		img[:]=[b,g,r]
cv2.destroyAllWindows()
