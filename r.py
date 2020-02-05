"""
Created on Wed Apr 17 12:06:32 2019

@author: prapti
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hist.jpg',0)
img = cv2.resize(img, (512, 512))
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([]);

def get_mask(r, size, center):
    mask = np.zeros(size)
    for i in range(size[0]):
        for j in range(size[1]):
            dist = np.sqrt((center[0] - i) * (center[0] - i) + (center[1] - j) * (center[1] - j))
            if dist <= r:
                mask[i, j] = 1
    return mask
mask = get_mask(float(input('radius : ')), fshift.shape, (fshift.shape[0]//2, fshift.shape[1]//2))
plt.imshow(mask, cmap='gray');

low_passed_fshift = mask * fshift
low_passed_magnitude_spectrum = np.log(np.abs(low_passed_fshift))
low_passed_magnitude_spectrum /= low_passed_magnitude_spectrum.max() * 255

plt.imshow(low_passed_magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum');

low_passed_f = np.fft.ifftshift(low_passed_fshift)

img_back = np.fft.ifft2(low_passed_f)
img_back = np.abs(img_back)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(img_back, cmap='gray')
