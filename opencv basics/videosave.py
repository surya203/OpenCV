import numpy as np
import cv2

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc, 24.0, (716,428))
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()
	if ret ==True:
		frame=cv2.flip(frame,0)
		out.write(frame)
		cv2.imshow('ai',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()
