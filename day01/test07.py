import cv2

img = cv2.imread(r"1.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'beautiful girl', (10, 30), font, 1, (0, 0, 255), 1, lineType=cv2.LINE_AA)

cv2.imshow("pic show", img)
cv2.waitKey(0)
