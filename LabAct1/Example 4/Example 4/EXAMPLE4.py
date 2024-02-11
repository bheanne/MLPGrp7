import cv2 as cv

# define a video capture object
vid = cv.VideoCapture(0)

while True:

    ret, frame = vid.read()
    cv.imshow('camera', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()