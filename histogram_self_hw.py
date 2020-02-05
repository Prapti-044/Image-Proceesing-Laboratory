import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png',0)
cv2.imshow("input",img)

m1=float(input("mean1= "))
s1=float(input("sigma1= "))
m2=float(input("mean2= "))
s2=float(input("sigma2= "))

def g_calc(mu, sigma):
    x = np.array(range(256))
    gaus = 1 / (sigma * np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x - mu)/sigma)**2)
    return gaus

g1 = g_calc(m1, s1)
g2 = g_calc(m2, s2)

g = g1 + g2
summ = 0

for i in range(256):
    summ += g[i]
    
for i in range(256):
    g[i] = g[i] / summ

plt.plot(np.array(range(256)),g1) 
plt.plot(np.array(range(256)),g2) 
plt.plot(np.array(range(256)),g) 
plt.title("Gaussian") 
plt.show() 

sk_g = np.zeros(256)
pr = 0

for i in range(256):
    pr = g[i] + pr
    s = round(255 * pr)
    sk_g[i] = s
    
nk = np.zeros(256)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        p = img[i][j]
        nk[p] += 1

p1=0
sk_img = np.zeros(256)
sk = np.zeros(256)
l = len(nk)

for i in range(l):
    p1 = (nk[i]/(img.shape[0] * img.shape[1])) + p1
    r = round(255 * p1)
    sk_img[i] = r
    
for i in range(l):
    #temp = sk_img[i]
    idx=0
    diff=9999999
    for j in range(l):
        sub = abs(sk_img[i] - sk_g[j])
        if sub < diff:
            diff = sub
            idx = j
    sk[i] = idx
    


plt.hist(sk_g.ravel(),256, [0,255])
plt.show()
plt.hist(sk_img.ravel(),256, [0,255])
plt.show()
plt.hist(sk.ravel(),256, [0,255])
plt.show()

new_img = img.copy()

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        x = img.item(i,j)
        new_img[i][j] = sk[x]

plt.hist(img.ravel(),256,[0,255])
plt.hist(new_img.ravel(),256, [0,255])
plt.show()

cv2.imshow("output", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()