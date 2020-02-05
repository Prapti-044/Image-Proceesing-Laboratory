import numpy as np
import cv2
import math

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
#box.jpg
print(img.shape)

#r_max = img.shape[0]
x_center = img.shape[0]//2
y_center = img.shape[0]//2

degree = int(input("enter degree:"))
r_max = int(input("Enter rmax:"))
alpha = -math.pi/180 * degree
twirl_img = np.zeros(img.shape, dtype='uint8')

for xp in range(0, img.shape[0]-1):
    for yp in range(0, img.shape[1]-1):
        
        dx = xp - x_center
        dy = yp - y_center
        r = math.sqrt( (dx * dx) + (dy * dy) )
        beta = math.atan2(dy, dx) + (alpha * ((r_max - r)/r_max))
        
        if r <= r_max:
            x = round(x_center + (r * math.cos(beta)))
            y = round(y_center + (r * math.sin(beta)))
        elif r > r_max:
            x = xp
            y = yp
            
        if 0 <= x < img.shape[0] and 0 <= y <img.shape[1]:
            twirl_img[xp][yp] = img[x][y]

cv2.imshow('original', img)
cv2.imshow('output', twirl_img)
cv2.waitKey(0)
cv2.destroyAllWindows()