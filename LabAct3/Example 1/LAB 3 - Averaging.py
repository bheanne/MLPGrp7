import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('Photos/image1.png')
cvrimg = cv.cvtColor(image, cv.COLOR_BGR2RGB) # This converts the color from BGR to RGB
img = cvrimg

blur = cv.blur(img,(5,5)) #Reads x and y values of blurring

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()