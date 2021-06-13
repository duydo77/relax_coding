from ast import iter_fields
import cv2
import numpy as np
from numpy.lib.function_base import iterable

def getContours(im, cThr=[100, 100], show_canny=False):
    
    imGray  = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    imBlur  = cv2.GaussianBlur(imGray, (5,5), 1)
    imCanny = cv2.Canny(imBlur, cThr[0], cThr[1])
    kernel = np.ones((5,5))
    imDilate = cv2.dilate(imCanny, kernel, iterations = 3)
    imThre = cv2.erode(imDilate, kernel, iterations = 2)
    
    if show_canny: cv2.imshow("canny", imCanny)

    contours, hiearachy = cv2.findContours(imThre, cv2.RETR_E)
    return imThre
