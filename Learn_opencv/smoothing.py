import cv2 as cv

img = cv.imread('red.jpg')
cv.imshow('Red Sandalwood', img)



# Averaging 
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)


# Gaussian Blur 

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)



# Median Blur 
median = cv.medianBlur(img, 3)


cv.waitKey(0)