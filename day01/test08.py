import cv2

src = cv2.imread(r"1.jpg")

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2YUV)

cv2.imshow("src show", src)
cv2.imshow("dst show", dst)
cv2.waitKey(0)