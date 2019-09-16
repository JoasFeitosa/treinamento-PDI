# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:08:20 2019

@author: joasm
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

%matplotlib inline

imhole = io.imread('C:\\Users\\joasm\\OneDrive\\Imagens\\holeimage.jpg')
plt.imshow(imhole)
height, width = imhole.shape[:2]