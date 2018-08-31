import cv2 
import sys

img_1 = cv2.imread('moon.tif',0)
img_2 = 255 - img_1

cv2.imshow('Input Image', img_1)
cv2.imshow('Negative Of Image', img_2)
cv2.waitKey(100000)
