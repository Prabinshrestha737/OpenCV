import cv2 as cv 
import numpy as np


img = cv.imread('red.jpg')
cv.imshow('Red sandal', img) 

blank = np.zeros(img.shape[:2])
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, mask)
cv.imshow('Masked Image', masked)



cv.waitKey(0)