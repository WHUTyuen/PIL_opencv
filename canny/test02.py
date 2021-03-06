import cv2

img = cv2.imread("7.jpg", 0)
cv2.imshow('Canny2', img)

img = cv2.convertScaleAbs(img, alpha=6, beta=0)
cv2.imshow('Abs', img)
img = cv2.GaussianBlur(img, (5, 5), 0)
canny = cv2.Canny(img, 50, 150)
canny = cv2.resize(canny, dsize=(500, 500))
cv2.imshow('Canny', canny)
cv2.waitKey(0)
