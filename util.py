import matplotlib.pyplot as plt # For showing image in notebook
import cv2
def show_img(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB));
    
def show_spyder_img(img, cnt=0):
    cv2.imshow('frame' + str(cnt), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()