import cv2
from time import sleep

while True:
	cam = cv2.VideoCapture(0)
	ret_val, img = cam.read()
	cv2.waitKey(10)
	cv2.imwrite('img/cam.jpg',img)
	sleep(4.83)
	cam.release()
