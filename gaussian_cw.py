import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

img = cv2.imread('noise.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('input', img)
#k = np.ones((5,5), np.float32)/25

sigma = 1
k = np.zeros((5,5))

for i in range(-2, 3):
    for j in range(-2, 3):
        
        k[i+2, j+2] = 1 / (2 * math.pi *sigma) * (math.e ** ((-1) * ((i*i) + (j*j)) / (2 * sigma * sigma)))
        
print(k)

for i in range(5, img.shape[0] - 5):
    for j in range(5, img.shape[1] - 5):
        sum = 0.0
        for x in range(5):
            for y in range(5):
                a = img.item(i+x, j+y)
                b = k[x][y] * a
                sum = sum + b
        img.itemset((i,j), sum)
        
cv2.imshow('output',img)
                
plt.imshow(k, cmap = 'gray')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()