import cv2
import numpy as np
cap=cv2.VideoCapture(0)
print(cap)
while(1):    # get a frame
    ret,frame = cap.read()
    cv2.imshow("capture",frame)