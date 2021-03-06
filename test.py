#%
import plotly.express as px
import xml.etree.ElementTree as ET
from cv2 import cv2
import numpy as np
import glob
import os
STANDARD_SIZE = 32
import pickle

from skimage.morphology import skeletonize
STANDARD_SIZE = 32
def imgReadIn(imgfilename):
    #Read image from file 
    original_img = cv2.imread(imgfilename)
    return original_img

def imgConvert(original_img):
    img_copy = original_img.copy()
    height = img_copy.shape[0]
    width = img_copy.shape[1]
    if(height*width*1000)> 2^31:
        resize = img_copy
    else:
        resize = cv2.resize(img_copy, dsize =(1000, int(1000*height/width)), interpolation = cv2.INTER_AREA)
    #GaussianBlur
    blur = cv2.GaussianBlur(resize,(5,5),0)
    #Image graying: reduce the influence of color
    gray = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    #Noises removal from outside the contours 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    img_open = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    #Covert image into binary 
    bin_img = cv2.adaptiveThreshold(img_open,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,20)
    bin_img = cv2.bitwise_not(bin_img)
    return bin_img

def imgSegmentation(imgs,Position):
    character_list = []
    for img in imgs:
        H = getHorizontalProjection(img)
        start1 = 0
        H_Start = []
        H_End = []
        for i in range(len(H)):
            if H[i] > 0 and start1 == 0:
                H_Start.append(i)
                start1 = 1
            if H[i] <= 0 and start1 == 1:
                H_End.append(i)
                start1 = 0

        W = getVerticalProjection(img)
        start2 = 0
        W_Start = []
        W_End = []
        for j in range(len(W)):
            if W[j] > 0 and start2 == 0:
                W_Start.append(j)
                start2 = 1
            if W[j] <= 0 and start2 == 1:
                W_End.append(j)
                start2 = 0
        if(len(W_End) == 0):
            W_End.append(img.shape[1])
        if(len(H_End) == 0):
            H_End.append(img.shape[0])
        char_img = img[H_Start[0]:H_End[-1],W_Start[0]:W_End[-1]]
        h, w = char_img.shape[:2]
        standard_background = np.zeros((STANDARD_SIZE,STANDARD_SIZE),np.uint8)
        if(h > w):
            img_resize = cv2.resize(char_img, ((int)(w * STANDARD_SIZE / h), STANDARD_SIZE), interpolation=cv2.INTER_AREA)
            difference = int((STANDARD_SIZE - img_resize.shape[1]) / 2)
            img_resize = cv2.bitwise_not(img_resize)
            standard_background[0:STANDARD_SIZE, difference:img_resize.shape[1] + difference] = img_resize
        else:
            img_resize = cv2.resize(char_img, (STANDARD_SIZE, (int)(h * STANDARD_SIZE / w)), interpolation=cv2.INTER_AREA)
            difference = int((STANDARD_SIZE - img_resize.shape[0]) / 2)
            img_resize = cv2.bitwise_not(img_resize)
            standard_background[difference:img_resize.shape[0] + difference, 0:STANDARD_SIZE] = img_resize
            #img = skeletonize(standard_background)
        standard_img = cv2.bitwise_not(standard_background)
        character_list.append(standard_img)
        standard_imgs=[]
        for i in range(len(character_list)):
            standard_imgs.append({'location':Position[i],'segment_img':character_list[i]})
            standard_imgs.sort(key=lambda x:x['location'][0]) 
    return standard_imgs



def getVerticalProjection(img):
    height, width = img.shape[:2]
    vertical = np.zeros(width,dtype=np.int32)
    for x in range(0, width):    
        for y in range(0, height):
            if img[y,x] == 0:
                vertical[x] += 1
    return vertical
   # emptyImage = np.zeros((height, width, 3), np.uint8) 
   # for x in range(0,width):
   #     for y in range(0, vertical[x]):
   #         b = (255,255,255)
   #         emptyImage[y,x] = b
   # cv2.imwrite('data/testPN1/v1.png', emptyImage)

def getHorizontalProjection(img):
    height, width = img.shape[:2]
    horizontal = np.zeros(height,dtype=np.int32)
    for y in range(0, height):    
        for x in range(0, width):
            if img[y,x] == 0:
                horizontal[y] += 1
    return horizontal
   # emptyImage = np.zeros((height, width, 3), np.uint8) 
   # for y in range(0,height):
   #     for x in range(0, horizontal[y]):
   #         b = (255,255,255)
   #         emptyImage[y,x] = b
   # cv2.imwrite('data/testPN1/h1.png', emptyImage)

def horizontalProjectionSegmentation(img):
    h,w =img.shape[:2]
    H = getHorizontalProjection(img)
    Position = []
    imgs = []
    start = 0
    H_Start = []
    H_End = []
    for i in range(len(H)):
        if H[i] > 0 and start ==0:
            H_Start.append(i)
            start = 1
        if H[i] <= 0 and start == 1:
            H_End.append(i)
            start = 0
    for j in range(len(H_Start)):
        cropImg = img[H_Start[j]:H_End[j], 0:w]
        W_Start, W_End = verticalProjectionSegmentation(cropImg)
        for x in range(len(W_Start)):
            Position.append([W_Start[x],H_Start[j],W_End[x],H_End[j]])
            img_aftercrop = img[H_Start[j]:H_End[j], W_Start[x]:W_End[x]]
            imgs.append(img_aftercrop)
    return imgs, Position

def verticalProjectionSegmentation(cropImg):
        W = getVerticalProjection(cropImg)
        start = 0
        W_Start = []
        W_End = []
        for j in range(len(W)):
            if W[j] > 0 and start ==0:
                W_Start.append(j)
                start = 1
            if W[j] <= 0 and start == 1:
                W_End.append(j)
                start = 0
        '''interval = []
        sum_interval = 0
        for x in range(len(W_End)-1):
            interval.append(W_Start[x+1]-W_End[x])
            sum_interval += W_Start[x+1]-W_End[x]
        average_interval = sum_interval/len(W_End)
        poppeditem = 0
        print(average_interval)
        for i in range(len(interval)):
            if(interval[i] < average_interval/4):
                W_Start.pop(i - poppeditem +1)
                W_End.pop(i - poppeditem)
                poppeditem += 1'''
        return W_Start, W_End


#def getSegmentationLocation(H_Start,H_End,W_Start,W_End):

#filepath = 'data/testPN1/*.png' 
#testImageSegementation(filepath)

inputimg = 'data/testPN1/formulaire001-equation010.png'
img = imgReadIn(inputimg)
img = imgConvert(img)
W = getVerticalProjection(img)
imgs, Position = horizontalProjectionSegmentation(img)
standard_imgs = imgSegmentation(imgs,Position)
img_list = []
for i in range(len(imgs)):
    img_list.append(standard_imgs[i]['segment_img'])
for index, img1 in enumerate(img_list, start= 1):
    imgpath = 'data/testPN1/' + str(index) + '.png'
    cv2.imwrite(imgpath, img1)
#cv2.imshow('image',img)

# %

# %
