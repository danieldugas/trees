import skimage
import skimage.io
import skimage.transform

import os
import scipy as scp
import scipy.misc

import numpy as np
import logging
import tensorflow as tf
import sys

import matplotlib.pyplot as plt

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)

img1 = skimage.io.imread("./trees.png")[:,:,0]

y = 300

plt.figure()
plt.imshow(img1)
plt.axhline(y, color='r')
plt.plot(img1[y,:]+y)
plt.tight_layout()
plt.show()

from skimage.filters import roberts, sobel
img2 = roberts(img1)
img3 = sobel(img1)
plt.figure()
plt.subplot(2,1,1)
plt.imshow(img2)
plt.title('Roberts Edge Detection')
plt.subplot(2,1,2)
plt.imshow(img3)
plt.title('Sobel Edge Detection')
plt.show()

from skimage.feature import canny
from skimage.transform import probabilistic_hough_line
img4 = canny(img1, 2, 1, 25)
lines = probabilistic_hough_line(img1,threshold=10, line_length=5, line_gap=3)
plt.figure()
plt.subplot(2,1,1)
plt.imshow(img3)
plt.title('Canny Edge Detection')
# plt.subplot(2,1,2)
# for line in lines:
#     p0, p1 = line
#     plt.plot((p0[0], p1[0]), (p0[1], p1[1]))
# plt.title('Probablistic Hough Line Detection')
plt.show()
