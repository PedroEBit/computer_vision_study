import cv2 
import os
import numpy as np

img_path = os.path.join("data", "curry.png")
img = cv2.imread(img_path)
edges = cv2.Canny(img, 200, 260)

edges_dilated = cv2.dilate(edges, np.ones((3,3), dtype=np.int8))
edges_eroded = cv2.erode(edges_dilated, np.ones((3,3), dtype=np.int8))

cv2.imshow("Edges Dilated", edges_dilated)
cv2.imshow("Edges Eroded", edges_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()