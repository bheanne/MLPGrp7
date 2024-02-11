import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
# define the codec and create a VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
        
    cv.imshow('frame', frame)
    out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break
#release everything if job is finished
cap.release()
cv.destroyAllWindows()