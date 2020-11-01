import cv2
import numpy as np

src = cv2.imread(r"1.jpg")
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #定义一个核
dst = cv2.filter2D(src, -1, kernel=kernel)


cv2.imshow("src show", src)
cv2.imshow("dst show", dst)
cv2.waitKey(0)
