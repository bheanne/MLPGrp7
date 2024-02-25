import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Photos/image1.jpg', cv.IMREAD_GRAYSCALE)  # Read the image in grayscale mode

# Apply Canny edge detector
edges = cv.Canny(img, 100, 200)  # Parameters: (input image, minVal, maxVal)

# Displays the original and edge-detected image
plt.subplot(121), plt.imshow(img, cmap = 'gray'), plt.title('Original Image')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap = 'gray'), plt.title('Edge Image')
plt.xticks([]), plt.yticks([])
plt.show()


