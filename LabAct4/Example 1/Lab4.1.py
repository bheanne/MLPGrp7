import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('flower.jpg')
cvromg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
omz = cvromg
zobel = cv.blur(omz, (3, 3))

# zobel x
zobelx = cv.Sobel(src=zobel, ddepth=cv.CV_64F, dx=1, dy=0, ksize=3)
fltrd_zx = cv.convertScaleAbs(zobelx)

# zobel y
zobely = cv.Sobel(src=zobel, ddepth=cv.CV_64F, dx=0, dy=1, ksize=3)
fltrd_zy = cv.convertScaleAbs(zobely)

# zsobel xy
zobelxy = cv.Sobel(src=zobel, ddepth=cv.CV_64F, dx=1, dy=1, ksize=3)
fltrd_zxy = cv.convertScaleAbs(zobelxy)

# set figure size
plt.figure(figsize=(10, 5))

# show 1st image - sobel x
plt.subplot(221), plt.imshow(omz, cmap='gray'), plt.title('Original Image')
plt.axis('off')

# show 2nd image - sobel y
plt.subplot(222), plt.imshow(zobelx, cmap='gray'), plt.title('Sobel X Image')
plt.axis('off')

# show 3rd image
plt.subplot(223), plt.imshow(zobely, cmap='gray'), plt.title('Sobel Y Image')
plt.axis('off')

# show 4th image - sobel xy
plt.subplot(224), plt.imshow(zobelxy, cmap='gray'), plt.title('Sobel XY Image')
plt.axis('off')

#show the frame
plt.show()
