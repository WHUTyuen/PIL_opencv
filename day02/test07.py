# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread(r"1.jpg", 0)
#
# f = np.fft.fft2(np.float32(img))
# f_shift = np.fft.fftshift(f)
# magnitude_spectrum = 20 * np.log(np.abs(f_shift))
#
# plt.subplot(121),plt.imshow(img, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', 0)
f = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

cv2.imshow("", magnitude_spectrum)
cv2.waitKey(0)

# plt.subplot(121), plt.imshow(img, 'gray'), plt.title('input'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(magnitude_spectrum, 'gray'), plt.title('magnitude_spectrum'), plt.xticks([]), plt.yticks(
#     [])
# plt.show()
