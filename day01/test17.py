import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('9.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
# dst = cv2.add(img1,img2)

cv2.imshow('dst', dst)
cv2.waitKey(0)
