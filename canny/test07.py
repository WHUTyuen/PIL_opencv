import cv2

img = cv2.imread('9.jpg')

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imggray,127,255,0)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 30
approx = cv2.approxPolyDP(contours[0],epsilon,True)

img_contour= cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)

cv2.imshow("img_contour", img_contour)
cv2.waitKey(0)