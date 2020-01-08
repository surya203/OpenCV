import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)

img=cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('logo',img)

img1=cv2.rectangle(img,(384,30),(310,128),(0,255,0),2)
cv2.imshow('logo',img1)

img2=cv2.circle(img,(190,190),44,(0,0,225),-1)
cv2.imshow('logo',img2)

img3=cv2.ellipse(img,(256,256),(100,50),0,0,180,225,-1)
cv2.imshow('logo',img3)

font=cv2.FONT_HERSHEY_SIMPLEX
name=cv2.putText(img,"AiWalkers",(10,500), font,4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("logo",name)
cv2.imwrite("AiWalkers.png",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

