import cv2

src = cv2.imread(r"6.jpg")

dst = cv2.GaussianBlur(src, (5, 5), 0)
dst = cv2.addWeighted(src, 3, dst, -2, 0)

print(dst.shape)

cv2.imshow("src show", src)
cv2.imshow("dst show", dst)
cv2.waitKey(0)
