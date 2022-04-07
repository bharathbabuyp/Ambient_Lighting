# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 01:25:06 2022

@author: Bharath
"""

from Asus_argb_ambient_lighting import get_split_screen_colors

# https://openrgb-python.readthedocs.io/en/latest/pages/advanced.html
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
import numpy as np
import time


client = OpenRGBClient()

client.clear() # Turns everything off

motherboard = client.get_devices_by_type(DeviceType.MOTHERBOARD)[0]
add = client.get_devices_by_type(DeviceType.MOTHERBOARD)[1]
add.leds[20].set_color(RGBColor(0, 255, 0))



cols = []
nleds=41

split_cols = get_split_screen_colors()

EN=[0,5]
ES=[5,10]
SE=[10,16]
SW=[16,21]
WS=[21,26]
WN=[26,32]
NW=[32,37]
NE=[37,41]
splits=[EN,ES,SE,SW,WS,WN,NW,NE]
brightness=0.7


while True:
    split_cols = get_split_screen_colors()
    if np.array(split_cols).max()>255 or np.array(split_cols).min()<0:
        continue
    cols=[]
    for i,split_color in enumerate(split_cols):
        print(i,split_color)
        split_color[0]=int(split_color[0]*brightness)
        split_color[1]=int(split_color[1]*brightness)
        split_color[2]=int(split_color[2]*brightness)
        for k in range(splits[i][0],splits[i][1]):
            cols.append(RGBColor(split_color[0],split_color[1],split_color[2]) )
    add.colors=cols
    add.show()
    
    time.sleep(.005)



while True:
    split_cols = get_split_screen_colors()
    # if np.array(split_cols).max()>255 or np.array(split_cols).min()<0:
        # continue
    mmin = np.array(split_cols).min()
    cols=[]
    for i,split_color in enumerate(split_cols):
        print(i,split_color)
        split_color[0]=int(split_color[0]-mmin)
        split_color[1]=int(split_color[1]-mmin)
        split_color[2]=int(split_color[2]-mmin)
        for k in range(splits[i][0],splits[i][1]):
            cols.append(RGBColor(split_color[0],split_color[1],split_color[2]) )
    add.colors=cols
    add.show()
    
    time.sleep(.05)
    
    
# while True:
#     for i in range(nleds):
#         cols.append(RGBColor(np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)))
#         # cols.append(RGBColor(np.random.randint(0,150), np.random.randint(0,150), np.random.randint(0,150)))
# # RGBColor(np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255))
#     for j in splits:
#         add.colors[j[0]:j[1]]=[RGBColor(np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255))]*(j[1]-j[0])
        
#     # add.colors[:nleds] = cols
#     add.show()
#     # cols=[]
#     time.sleep(1)
    # for device in add.leds:
    #     device.set_color(RGBColor(np.random.randint(0,150), np.random.randint(0,150), np.random.randint(0,150)))
    #     # time.sleep(.001)




