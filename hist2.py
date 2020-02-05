#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:40:33 2019

@author: prapti
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray');

img = np.asarray(img)
flat = img.flatten()

# show the histogram
plt.hist(flat, bins=50)

def get_histogram(image, bins):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1
    return histogram

# execute our histogram function
hist = get_histogram(flat, 256)
def cumsum(a):
    a = iter(a)
    b = [next(a)]
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

# execute the fn
cs = cumsum(hist)

# display the result
plt.plot(cs)

# cs = (((cs - cs.min()) * 255) / (cs.max() - cs.min())).astype('uint8')
nj = (cs - cs.min()) * 255
N = cs.max() - cs.min()

# re-normalize the cumsum
cs = nj / N

# cast it back to uint8 since we can't use floating point values in images
cs = cs.astype('uint8')

plt.plot(cs)

img_new = cs[flat]
img_new = np.reshape(img_new, img.shape)

plt.imshow(img_new, cmap='gray')