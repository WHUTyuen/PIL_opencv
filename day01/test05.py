import cv2

img = cv2.imread(r"1.jpg")

cv2.line(img, (100, 30), (210, 180), color=(0, 0, 255), thickness=2)
# cv2.circle(img, (50, 50), 30, (0, 0, 255), 1)
# cv2.rectangle(img,(100,30),(210,180),color=(0,0,255),thickness=2)
# cv2.ellipse(img, (100, 100), (100, 50), 0, 0, 360, (255, 0, 0), 2)
cv2.imshow("pic show", img)
cv2.waitKey(0)
