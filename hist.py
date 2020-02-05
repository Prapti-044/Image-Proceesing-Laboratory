#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:06:05 2019

@author: prapti
"""
import cv2
import numpy as np

import matplotlib.pyplot as plt

img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('input',img)
flat = img.flatten()
plt.hist(flat, bins=255);

def get_hist(img, bins):
    histogram = np.zeros(bins)
    
    for p in img:
        histogram[p] += 1
    
    return histogram
hist = get_hist(flat, 255)
plt.plot(hist);

plt.hist(img.ravel(), 256, [0, 255]);

def cumsum(a):
    a = iter(a)
    b = [next(a)]
    
    for i in a:
        b.append(b[-1] + i)
    return np.array(b)

nj = (cs - cs.min()) * 255
N = cs.max() - cs.min()
cs = nj / N


# cs = (((cs - cs.min()) * 255) / (cs.max() - cs.min())).astype('uint8')
plt.plot(cs)
img_new = cs[flat]
img_new = np.reshape(img_new, img.shape)

plt.imshow(img_new, cmap='gray')


# cs = (((cs - cs.min()) * 255) / (cs.max() - cs.min())).astype('uint8')
plt.plot(cs)

plt.plot(histogram);


plt.hist(img.ravel(), 128, [0,255])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


