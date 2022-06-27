
import cv2 as cv
import numpy as np

blank =np.zeros((400, 400))

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)


cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)



#Bitwise AND --> Intersecting Regions 

bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('BITWISE AND ', bitwise_and)


#BITWISE OR --> None interesting and intersecting regions 
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('BITWISE OR ', bitwise_or)


#BITWISE OR  ---> Non- intesecting regions 
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('BITWISE XOR ', bitwise_xor)



cv.waitKey(0)