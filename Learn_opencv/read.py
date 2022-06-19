from configparser import Interpolation
import cv2 as cv


#Reading Images 


img = cv.imread('red.jpg')

cv.imshow('RedSandal', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)





#Reading Videos 

# capture = cv.VideoCapture('video.mp4')

# while True:
#     isTrue, frame = capture.read()

#     cv.imshow('Video of Dog', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

cv.waitKey(0)


