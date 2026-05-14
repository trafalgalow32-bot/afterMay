# opencv_hsv_medicine.py

import cv2
import numpy as np

img = cv2.imread("opencv_study/images/medicine.png")

hsv = cv2.cvtColor( img, cv2.COLOR_BGR2HSV)

# lower & upper_red
# lower & upper_yellow
# lower & upper_blue
# lower & upper_white?