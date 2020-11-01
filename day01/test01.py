import cv2

# 读取图片并显示
img = cv2.imread(r"1.jpg",0)
print(type(img))
print(img.shape)
cv2.imshow("pic show", img)
cv2.waitKey(0)
