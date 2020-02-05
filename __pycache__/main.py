from skimage.exposure import cumulative_distribution
import matplotlib.pylab as plt
import numpy as np
import cv2

def cdf(im):
    '''
    computes the CDF of an image im as 2D numpy ndarray
    '''
    c, b = cumulative_distribution(im) 
    # pad the beginning and ending pixels and their CDF values
    c = np.insert(c, 0, [0]*b[0])
    c = np.append(c, [1]*(255-b[-1]))
    return c

def hist_matching(c, c_t, im):
    '''
    c: CDF of input image computed with the function cdf()
    c_t: CDF of template image computed with the function cdf()
    im: input image as 2D numpy ndarray
    returns the modified pixel values
    ''' 
    pixels = np.arange(256)
    # find closest pixel-matches corresponding to the CDF of the input image, given the value of the CDF H of   
    # the template image at the corresponding pixels, s.t. c_t = H(pixels) <=> pixels = H-1(c_t)
    new_pixels = np.interp(c, c_t, pixels) 
    im = (np.reshape(new_pixels[im.ravel()], im.shape)).astype(np.uint8)
    return im

img = cv2.imread('lenna.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('shell.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Source', img)
cv2.imshow('Destination', dst)




ret = hist_matching(cdf(img), cdf(dst), img)

cv2.imshow('Matched', ret)


#plt.imshow(ret, cmap='gray')



cv2.waitKey(0)
cv2.destroyAllWindows()