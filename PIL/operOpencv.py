import cv2
#
img = cv2.imread("../img/pic.jpg")
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("win",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# cv2.imshow("win",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# h\w
print(img.shape)
print(img)

# img = img[0:,0:,2]
# img = cv2.imshow("b",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.line(img,(0,0),(300,300),color=(0,255,0),thickness=3)
# img = cv2.imshow("b",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.rectangle(img,(300,400),(500,500),color=(0,255,0),thickness=3)
# img = cv2.imshow("b",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


img = cv2.circle(img,(330,450),radius=80,color=(0,255,0),thickness=3)
img = cv2.imshow("b",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


