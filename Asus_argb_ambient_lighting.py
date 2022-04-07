# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:00:37 2022

@author: Bharath
"""

from PIL import Image
from PIL import ImageGrab
import time
from numpy import sum
import numpy as np
time.sleep(0)




im = ImageGrab.grab()
px = im.load()
img=np.asarray(im)

#dividing the rectangle image into 8 triangles
