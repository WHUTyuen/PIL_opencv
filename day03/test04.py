import cv2 as cv

img = cv.imread("10.jpg", 0)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel, iterations=1)

cv.imwrite("21.jpg", dst)

cv.imshow('src', img)
cv.imshow('dst', dst)
cv.waitKey(0)
