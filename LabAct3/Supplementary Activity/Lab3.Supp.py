import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('Photos/image1.png')
cvrimg = cv.cvtColor(image, cv.COLOR_BGR2RGB) # This converts the color from RGB to BGR
img = cvrimg

x_axis = 135
y_axis = 25
ave = cv.blur(img,(5,5)) # Reads x and y values of blurring
gaus = cv.GaussianBlur(img,(5,5),0)
medi = cv.medianBlur(img,5)
bilat = cv.bilateralFilter(img, 9, 75,75)

plt.subplot(3,3,1), plt.imshow(ave), plt.text(x_axis, y_axis, 'Averaging' ,fontdict={'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'style': 'normal', 'color': 'blue'})
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,3), plt.imshow(gaus), plt.text(x_axis, y_axis, 'Gaussian',fontdict={'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'style': 'normal', 'color': 'blue'})
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,7), plt.imshow(medi), plt.text(x_axis, y_axis, 'Median',fontdict={'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'style': 'normal', 'color': 'blue'})
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,9), plt.imshow(bilat), plt.text(x_axis, y_axis, 'Bilateral',fontdict={'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'style': 'normal', 'color': 'blue'})
plt.xticks([]), plt.yticks([])

plt.subplot(3,3,5), plt.imshow(img), plt.text(x_axis, y_axis, 'Original',fontdict={'family': 'Times New Roman', 'size': 12, 'weight': 'bold', 'style': 'normal', 'color': 'blue'})
plt.xticks([]), plt.yticks([])

plt.show()
