
import urllib.request
import cv2
import numpy as np
from PIL import Image
import os
from urllib import request
def Orange_Count():
    s1="E:\FYP\openCV\Hue\ColorDetect/ColorSource.jpg"
    s2="E:\FYP\openCV\Hue\ColorDetect/Orange.png"
    try:
        #os.remove(s1)
        os.remove(s2)
    except: pass
    #urllib.request.urlretrieve(img,s1)

    img = cv2.imread(s1)

    ## convert to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    ## mask of green (36,25,25) ~ (86, 255,255)
    # mask = cv2.inRange(hsv, (36, 25, 25), (86, 255,255))
    mask = cv2.inRange(hsv, (15, 0, 0),(25, 255, 255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    ## save
    cv2.imwrite(s2, green)

    BLACK_MIN = np.array([0, 0, 0], np.uint8)
    BLACK_MAX = np.array([0, 0, 0], np.uint8)
    dst = cv2.inRange(green, BLACK_MIN, BLACK_MAX)
    no_black = cv2.countNonZero(dst)

    a=str(no_black)
    a=int(a)
    cv2.waitKey(0)
    width, height = Image.open(s2).size
    c=width*height
    #print (a)
    #print (c)
    b=((c-a)/c)*100
    return b
#print("Orange percentage: %.2f"% Orange_Count("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Color_icon_green.svg/2000px-Color_icon_green.svg.png"))