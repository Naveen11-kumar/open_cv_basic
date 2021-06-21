import cv2
import numpy
import imutils

#img read 
img=cv2.imread("football.jpg")



#ball_ROI
ball = img[125:165, 75:125]
img[100:140, 10:60] = ball



#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey()
