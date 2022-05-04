import cv2
import numpy as np
from vlcs_mobile import copyVideo

video = copyVideo()
cap = cv2.VideoCapture(video)

total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
i = 0

while (cap.isOpened() and i<total):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray,None,fx=0.5,fy=0.5)
        cv2.imshow('Gray',gray)
        cv2.waitKey(60)
        i += 1

cap.release()
cv2.destroyAllWindows()
