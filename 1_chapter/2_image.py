import cv2 as cv
import numpy as np

img = cv.imread(r"images\i1.jpg")

img1 = cv.resize(img, (400,500))

cv.imshow('image', img1)
cv.waitKey(0)
cv.destroyAllWindows()
