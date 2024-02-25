import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)


def animate(i):
    # multithreading
    a = threading.Thread(target=lambda: plot1.set_data(camera(cap, "original")))
    a.start()
    b = threading.Thread(target=lambda: plot2.set_data(camera(cap, "Canny")))
    b.start()
    c = threading.Thread(target=lambda: plot3.set_data(camera(cap, "SobelXY")))
    c.start()
    d = threading.Thread(target=lambda: plot4.set_data(camera(cap, "Laplace")))
    d.start()
    if plt.waitforbuttonpress(timeout=0.00001):
        plt.close()


def camera(cam, plots):
    ret, frame = cam.read()
    smurftohuman = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    ave = cv.blur(smurftohuman, (5, 5))  # Reads x and y values of blurring
    gaus = cv.GaussianBlur(smurftohuman, (1, 1), 0)
    medi = cv.medianBlur(smurftohuman, 5)
    bilat = cv.bilateralFilter(smurftohuman, 9, 75, 75)

    if plots == "original":
        return smurftohuman
    elif plots == "Canny":
        return cv.Canny(medi, 100, 200)
    elif plots == "SobelXY":
        sobelxy = cv.Sobel(src=gaus, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
        return cv.convertScaleAbs(sobelxy)
    elif plots == "Laplace":
        laplacian = cv.Laplacian(gaus, 5, cv.CV_64F)
        filtered_image = cv.convertScaleAbs(laplacian)
        return filtered_image


x_axis = 195
y_axis = 25

plt.figure(figsize=(17, 8))

nf = plt.subplot(2, 2, 1)
plt.xticks([]), plt.yticks([]), plt.text(200, 45, 'No filter/Original',
                                         fontdict={'family': 'Arial', 'size': 12, 'weight': 'bold',
                                                   'style': 'normal', 'color': 'blue'})
cunnykiel = plt.subplot(2, 2, 2)
plt.xticks([]), plt.yticks([]), plt.text(200, 45, 'Canny Edge Detector',
                                         fontdict={'family': 'Arial', 'size': 12, 'weight': 'bold',
                                                   'style': 'normal', 'color': 'blue'})
zobelxy = plt.subplot(2, 2, 3)
plt.xticks([]), plt.yticks([]), plt.text(200, 45, 'Sobel Edge Detector',
                                         fontdict={'family': 'Arial', 'size': 12, 'weight': 'bold',
                                                   'style': 'normal', 'color': 'blue'})
laplace = plt.subplot(2, 2, 4)
plt.xticks([]), plt.yticks([]), plt.text(200, 45, 'Laplacian Edge Detector',
                                         fontdict={'family': 'Arial', 'size': 12, 'weight': 'bold',
                                                   'style': 'normal', 'color': 'blue'})

plot1 = nf.imshow(camera(cap, "original"))
plot2 = cunnykiel.imshow(camera(cap, "Canny"), cmap="gray")
plot3 = zobelxy.imshow(camera(cap, "SobelXY"), cmap="gray")
plot4 = laplace.imshow(camera(cap, "Laplace"), cmap="gray")

animation = FuncAnimation(plt.gcf(), animate, interval=1, repeat=False, cache_frame_data=False)

plt.show()
