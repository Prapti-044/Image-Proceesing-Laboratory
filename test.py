#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:18:11 2019

@author: prapti
"""

import numpy as np
import cv2
from util import *
from skimage.exposure import rescale_intensity
import math
import matplotlib.pyplot as plt

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]
 
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
        cv2.BORDER_REPLICATE)
    
    output = np.zeros((iH, iW), dtype="float32")
    
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            k = (roi * kernel).sum()

            output[y - pad, x - pad] = k
            
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    return output

sigma = 1
kernel = np.zeros((5, 5))
for i in range(-2, 3):
    for j in range(-2, 3):
        kernel[i+2, j+2] = 1/(2 * math.pi * sigma) * (math.e ** (-1 * (i*i+j*j)/(2*sigma*sigma) ))

print(kernel)
plt.imshow(kernel, cmap='gray')

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Original', img)
#plt.imshow(img, cmap='gray')

# cv2.imshow('Gaussian', convolve(img, kernel))

smallBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")
 
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")
kernelBank = (
    ("small_blur", smallBlur),
    ("large_blur", largeBlur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobelX),
    ("sobel_y", sobelY)
)

'''
for k in kernelBank:
    cv2.imshow(k[0], cv2.resize(convolve(img, k[1]), (0,0), fx=0.5, fy=0.5))
'''
cv2.waitKey(0)
cv2.destroyAllWindows()