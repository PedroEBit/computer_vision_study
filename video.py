import cv2
import os
import numpy as np

video_path = os.path.join("data", "Monkeyflip.mp4")
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _ , thresh = cv2.threshold(gray, 100, 200, cv2.THRESH_BINARY)

    cv2.imshow("Frame", frame)
    cv2.imshow("Edges", thresh)

    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()