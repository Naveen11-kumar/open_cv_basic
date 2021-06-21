import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("nav.jpg")




# draw green text on the image
output = img.copy()
cv2.putText(output, "Naveen", (400, 800),cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 250, 0), 3)
cv2.imshow("Text", output)
cv2.waitKey()


