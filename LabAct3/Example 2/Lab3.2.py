import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('filename.png')
cvrimg = cv.cvtColor(image, cv.COLOR_BGR2RGB)
img = cvrimg
blur = cv.GaussianBlur(img,(5, 5),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


