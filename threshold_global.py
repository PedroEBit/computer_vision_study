import cv2 
import os

img_path = os.path.join("data", "bear.png")

img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img_thresh = cv2.threshold(img_gray, 90, 255, cv2.THRESH_BINARY)

img_thresh = cv2.blur(img_thresh, (5,5))
ret, img_thresh = cv2.threshold(img_thresh, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("imgGray", img)
cv2.imshow("imgThresh", img_thresh)
cv2.waitKey(0)