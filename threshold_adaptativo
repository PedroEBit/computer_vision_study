import cv2 
import os

img_path = os.path.join("data", "handwritten.png")

img = cv2.imread(img_path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
img_thresh_mean = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow("img", img_thresh)
cv2.imshow("img_mean", img_thresh_mean)
cv2.waitKey(0)
