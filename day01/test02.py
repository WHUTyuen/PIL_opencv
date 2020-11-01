import numpy as np
import cv2

img = np.empty((200, 100, 3), np.uint8)

img[..., 0] = 255
img[..., 1] = 0
img[..., 2] = 0

img = img[:,:,::-1]

cv2.imwrite("2.jpg", img)
