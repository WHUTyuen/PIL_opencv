import cv2

src = cv2.imread('1.jpg')
rows, cols, channel = src.shape

dst = cv2.resize(src, (cols * 2, rows * 2), interpolation=cv2.INTER_CUBIC)
# dst = cv2.transpose(src)
# dst = cv2.flip(src, 0)

cv2.imshow('src pic', src)
cv2.imshow('dst pic', dst)
cv2.waitKey(0)
