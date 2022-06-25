import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('red.jpg')
cv.imshow('RedSandal', img)

# plt.imshow(img)
# plt.show()


#BGR TO Gray Scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#BGR TO HSV(high saturation value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR To LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


#BGR TO RGB 

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


#HSV TO BGR 

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)