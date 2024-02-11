import cv2 as cv

x = cv.VideoCapture(0)

while True:

    isTrue, frame = x.read()
    cv.imshow('camera', frame)

    if cv.waitKey(1) & 0xFF == ord('w'):
        break

x.release()
cv.destroyAllWindows()