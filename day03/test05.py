import cv2 as cv

img = cv.imread("11.jpg", 0)

kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
dst = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# cv.imwrite("21.jpg", dst)
cv.imwrite("27.jpg", dst)

cv.imshow('src', img)
cv.imshow('dst', dst)
cv.waitKey(0)