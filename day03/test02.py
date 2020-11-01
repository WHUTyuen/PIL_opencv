import cv2 as cv

img = cv.imread("11.jpg", 0)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.erode(img, kernel)

cv.imshow('src', img)
cv.imshow('dst', dst)
cv.waitKey(0)
