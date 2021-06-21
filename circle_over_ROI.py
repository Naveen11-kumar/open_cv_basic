import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("nav.jpg")

output = img.copy()
circle_img = cv2.circle(img,(335,480), 330, (0,250,0), 3)
cv2.imshow ("circle", circle_img )
cv2.waitKey()


