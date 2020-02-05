#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:57:05 2019

@author: prapti
"""

from skimage.exposure import cumulative_distribution
import numpy as np
import math
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
#dst = cv2.imread('shell.png', cv2.IMREAD_GRAYSCALE)
def gaussian(mu=128, sigma=20, size=256):
    #gaus = []
    x = np.array(range(256))
    #for i in range(0,size):
    gaus = 1 / (sigma * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x - mu)/sigma)**2)
    return gaus

g1 = gaussian(85, 25)
g2 = gaussian(170, 15)
hist_g = (g1 + g2)/2 * 256 * 256
print(np.sum(hist_g))

plt.subplot(411)
plt.plot(np.array(range(256)), hist_g)

hist_img = np.zeros((256))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        hist_img[img[i, j]] += 1
        
print(np.sum(hist_img))

plt.subplot(412)
plt.plot(np.array(range(256)), hist_img)

new_hist_img = hist_img.copy()
for i in range(256):
    minimum = 9999999
    min_index = -1
    for j in range(256):
        diff = np.abs(hist_img[i] - hist_g[j])
        if diff < minimum:
            minimum = diff
            min_index = j
    new_hist_img[i] = min_index

plt.subplot(413)
plt.plot(np.array(range(256)), new_hist_img)

print(np.sum(new_hist_img))

#cv2.waitKey(0)
#cv2.destroyAllWindows()