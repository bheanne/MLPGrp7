#Python code to read image
import cv2
img = cv2.imread(r"C:\Users\msi\Downloads\image.jpg", cv2.IMREAD_COLOR)

#Creating GUI window to display an image on screen
cv2.imshow("image", img)
cv2.waitKey(0)
cv2. destroyAllWindows()