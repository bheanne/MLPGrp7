import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Photos/image1.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # Convert color space to RGB
median = cv.medianBlur(img, 15)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(median), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

