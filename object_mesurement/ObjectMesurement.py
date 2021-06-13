import cv2
import numpy as np
import utils

image_path = './1.jpg'
use_webcam = False

if use_webcam: 
    cap = cv2.VideoCapture(0)
    # cap.set(3, 500) # camera height
    # cap.set(4, 100) # camera width

while(True):
    if use_webcam:
        ret, image = cap.read()
        if ret != True: break
    else:
        image = cv2.imread(image_path)
        h, w, _ = image.shape
        image = cv2.resize(image, (418, int(418*(h/w)) ))

    # image = utils.getContours(image)
    cv2.imshow("haha", image)
    if cv2.waitKey(1) == ord('q'):
        break