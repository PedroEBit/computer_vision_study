import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

VideoCapture = cv2.VideoCapture(0)
while True:
    ret, frame = VideoCapture.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)

    cv2.imshow("Frame", frame)
    cv2.imshow("Edges", thresh)

    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
        break

VideoCapture.release()
cv2.destroyAllWindows()