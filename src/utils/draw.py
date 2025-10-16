import cv2
import os
import numpy as np

img = cv2.imread(os.path.join("data", "whiteboard.png"))

#line
cv2.line(img, (61,31), (918,631), (0,0,0), 2)

#rectangle
cv2.rectangle(img, (100,100), (200,400), (255,0,0), 7)

#circle
cv2.circle(img, (300,300), 50, (0,0,255), -1)

#text
cv2.putText(img, "Hello, OpenCV!", (300, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,70,155), 1)

img = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("Image", img)
waitKey = cv2.waitKey(0)