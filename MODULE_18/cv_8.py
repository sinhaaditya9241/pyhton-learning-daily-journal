import cv2 
import numpy as np

img = cv2.imread('image.jpg')

threshold_value = 200

_, binary_threshold = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', img)
cv2.imshow('Binary Threshold', binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows() 