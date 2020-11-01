import cv2

src = cv2.imread(r"1.jpg")

dst = cv2.medianBlur(src, 5)

cv2.imshow("src show", src)
cv2.imshow("dst show", dst)
cv2.waitKey(0)
