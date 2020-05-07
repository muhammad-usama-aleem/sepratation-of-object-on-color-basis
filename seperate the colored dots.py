import os
import numpy as np
import cv2

os.chdir("C:/Users/abdul/OneDrive/Pictures/New folder")
img = cv2.imread("dots.jpg")
img = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
Gaussian = cv2.GaussianBlur(img, (15, 15), 0)
gray = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2HSV)

lower_blue = np.array([13,41,133])
upper_blue = np.array([35,150,255])
result = cv2.inRange(gray, lower_blue, upper_blue)
contour, _ = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

yellow = 0
for c in contour:
    if cv2.contourArea(c) > 500:
        cv2.cv2.drawContours(img, contour, -1, (255, 0, 0), 2)
        yellow = yellow + 1
print(yellow)

cv2.imshow("win", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
