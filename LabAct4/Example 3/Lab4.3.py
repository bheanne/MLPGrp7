import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread('images\\image1.jpg')
cvrimg = cv.cvtColor(image, cv.COLOR_BGR2RGB) # This converts the color from RGB to BGR

x_axis = 135
y_axis = 25
ave = cv.blur(cvrimg,(2,2)) 

laplacian = cv.Laplacian(ave, 5, cv.CV_16F)
filtered_image = cv.convertScaleAbs(laplacian)


# set figure size
plt.figure(figsize=(20,20))

# show the first image
plt.subplot(121)
plt.imshow(cvrimg, cmap='gray')
plt.title('Original Image')
plt.axis("off")

# show the second image
plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('Edged Image')
plt.axis("off")

plt.show()