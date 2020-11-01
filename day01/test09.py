import cv2

img = cv2.imread(r"1.jpg")

img[..., 0] = 0
img[..., 1] = 0

cv2.imshow("dst show", img)
cv2.waitKey(0)
