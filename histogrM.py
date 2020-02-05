import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('hist.jpg', cv2.IMREAD_GRAYSCALE)
plt.hist(img.ravel(), 256, [0, 255])

plt.show()
flat = img.flatten()

def get_hist(img, bins):
    nk = np.zeros(bins)
    print(img)
    for p in img:
        nk[p] += 1
    return nk

nk = get_hist(flat, 255)

pr = nk/(img.shape[0]*img.shape[1])

sk = []

for j in range(256):
    sk.append(255 * np.sum(pr[:j]))

sk = np.array(sk, dtype='uint8')
img_new = sk[flat]
img_new = np.reshape(img_new, img.shape)

plt.hist(img_new.ravel(), 256, [0, 255]);
plt.show()
cv2.imshow('img_new', img_new)

cv2.waitKey(0)
cv2.destroyAllWindows()