import cv2 
import os
import numpy as np

img_path = os.path.join("data", "birds.png")
img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    counter = 0
    area = cv2.contourArea(cnt)
    if area > 200:
       counter += 1
       #cv2.drawContours(img, [cnt], -1, (0,255,0), 1)
       cv2.boundingRect(cnt)
       x1,y1,w,h = cv2.boundingRect(cnt)
       cv2.rectangle(img, (x1,y1), (x1+w, y1+h), (0,255,0), 1)
       cv2.putText(img, str(round(area)), (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

cv2.imshow("Image", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()