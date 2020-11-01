import cv2
import numpy as np

img = cv2.imread(r"1.jpg")

# 定义四个顶点坐标
pts = np.array([[10, 5], [50, 10], [70, 20], [20, 30]], np.int32)
# 顶点个数：4，矩阵变成4*1*2维
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 255), 2)

cv2.imshow("pic show", img)
cv2.waitKey(0)
