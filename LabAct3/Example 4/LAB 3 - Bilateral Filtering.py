import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread("Photos/Image3.png")
cvrimg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img1 = cvrimg
blur = cv.bilateralFilter(img1, 9, 75, 75)

plt.subplot(121), plt.imshow(img1), plt.title("Original")
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(blur), plt.title("Blurred")
plt.xticks([]), plt.yticks([])
plt.show()