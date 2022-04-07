# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 00:00:37 2022

@author: Bharath
"""

# from PIL import Image
from PIL import ImageGrab
import time
# from numpy import sum
import numpy as np
# time.sleep(0)
from matplotlib import pyplot as plt



# @profile
def get_split_screen_colors():

#dividing the rectangle image into 8 triangles
#EN, ES, SE, SW, WS, WN, NW, NE

    # _____________
    # |NW   |   NE|
    # |WN   _   EN|
    # |WS   _   ES|
    # |SW   |   SE|
    # _____________

    im = ImageGrab.grab()
    # px = im.load()
    img=np.asarray(im)
    img=img[::5, ::5]
    
    # plt.imshow(img)
    
    EN=[]
    ES=[]
    SE=[]
    SW=[]
    WS=[]
    WN=[]
    NW=[]
    NE=[]
    
    
    horz=img.shape[1]
    vert=img.shape[0]
    blank = np.zeros_like(img)
    #EN
    for x in range(horz//2,horz):
        y = -int(vert/horz*x)+vert
        # print(y,vert//2,x)
        blank[y:vert//2,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int)
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int)
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int)
    EN=[R,G,B]
    
    #ES
    blank = np.zeros_like(img)
    for x in range(horz//2,horz):
    # for x in range(horz//2,horz//2+100):
        y = int(vert/horz*x)
        # print(vert//2,y,x)
        blank[vert//2:y,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int)
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int)
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int)
    ES=[R,G,B]
    
    #SE
    blank = np.zeros_like(img)
    for x in range(horz//2,horz):
    # for x in range(horz//2,horz//2+100):
        y = int(vert/horz*x)
        # print(y,vert,x)
        blank[y:vert,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    SE=[R,G,B]
    
    #SW
    blank = np.zeros_like(img)
    for x in range(horz//2,0,-1):
    # for x in range(horz//2,horz//2-400,-1):
        y = -int(vert/horz*x)+vert
        # print(y,vert,x)
        blank[y:vert,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    SW=[R,G,B]
    
    #WS
    blank = np.zeros_like(img)
    for x in range(horz//2,0,-1):
    # for x in range(horz//2,horz//2-400,-1):
        y = -int(vert/horz*x)+vert
        # print(vert//2,y,x)
        blank[vert//2:y,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    WS=[R,G,B]
    
    #WN
    blank = np.zeros_like(img)
    for x in range(horz//2,0,-1):
    # for x in range(horz//2,horz//2-100,-1):
        y = int(vert/horz*x)
        # print(y,vert//2,x)
        blank[y:vert//2,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    WN=[R,G,B]
    
    #NW
    blank = np.zeros_like(img)
    for x in range(horz//2,0,-1):
    # for x in range(horz//2,horz//2-200,-1):
        y = int(vert/horz*x)
        # print(0,y,x)
        blank[0:y,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    NW=[R,G,B]
    
    #NE
    blank = np.zeros_like(img)
    for x in range(horz//2,horz):
        y = -int(vert/horz*x)+vert
        # print(0,y,x)
        blank[0:y,x]=1
    # plt.imshow(blank)
    a=(blank*img)
    R=a[:,:,0][a[:,:,0]>0].mean().astype(int) 
    G=a[:,:,1][a[:,:,1]>0].mean().astype(int) 
    B=a[:,:,2][a[:,:,2]>0].mean().astype(int) 
    NE=[R,G,B]
    
    
    seg = [EN,ES,SE,SW,WS,WN,NW,NE]
    return seg


# a = get_split_screen_colors()

# while True:
#     print(get_split_screen_colors())

# import cProfile
# cProfile.run('get_split_screen_colors()')
