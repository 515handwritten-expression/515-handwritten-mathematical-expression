#%
import plotly.express as px
import xml.etree.ElementTree as ET
from cv2 import cv2
import numpy as np
import glob
import os
import pickle
#from skimage.morphology import skeletonize
STANDARD_SIZE = 32
symbol = ['alpha','beta','gamma','phi','pi','geq','leq','pm','theta','infty','div','times','sum','ldots','neq','rightarrow','int','sqrt', 'exists','forall','in']

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
    return bin_img

def imgSegmentation(binary_img):
    character_location = []
    character_list = []
    #Using the external contour to find the contour for each character
    contours, hierarchy = cv2.findContours(binary_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        location = cv2.boundingRect(contour)
        x, y, w, h = location
       # cv2.rectangle(binary_img, (x, y), (x+w, y+h), (255, 255, 255), 2)
        #print(len(contours))
        if contour is not None:
            character_location.append(location)
            #Create a black background, add one of the contours to the background each time and fill it with white color
            background = np.zeros(binary_img.shape,np.uint8)
            cv2.drawContours(background, [contour], -1, (255,255,255), cv2.FILLED)
            masked_img = cv2.bitwise_and(background, binary_img)
            #Extract the contour along the rectangle
            char_img = masked_img[y:y+h,x:x+w]
            #Create a new background withSTANDARD_SIZE * STANDARD_SIZE
            standard_background = np.zeros((STANDARD_SIZE,STANDARD_SIZE),np.uint8)
            if(h > w):
                img_resize = cv2.resize(char_img, ((int)(w * STANDARD_SIZE / h), STANDARD_SIZE), interpolation=cv2.INTER_AREA)
                difference = int((STANDARD_SIZE - img_resize.shape[1]) / 2)
                standard_background[0:STANDARD_SIZE, difference:img_resize.shape[1] + difference] = img_resize
            else:
                img_resize = cv2.resize(char_img, (STANDARD_SIZE, (int)(h * STANDARD_SIZE / w)), interpolation=cv2.INTER_AREA)
                difference = int((STANDARD_SIZE - img_resize.shape[0]) / 2)
                standard_background[difference:img_resize.shape[0] + difference, 0:STANDARD_SIZE] = img_resize
            character_list.append(standard_background)
            imgs=[]
            for i in range(len(character_list)):
                imgs.append({'location':character_location[i],'segment_img':character_list[i]})
            imgs.sort(key=lambda x:x['location'][0])
    return imgs


def testImageSegementation(filepath):
    files = glob.glob(filepath)
    for filename in files:
            fileid = filename[13:-4]
            print(fileid)
            oriimg = imgReadIn(filename)
            binimg = imgConvert(oriimg)
            imgs = imgSegmentation(binimg)
            img_list = []
            img_loc = []
            for i in range(len(imgs)):
                img_list.append(imgs[i]['segment_img'])
                img_loc.append(imgs[i]['location'])
            path = os.path.join('data/testPNGSeg', fileid)
            os.mkdir(path)
            for index, img in enumerate(img_list, start=1):
                imgpath = path + '/' + str(index) + '.png'
                cv2.imwrite(imgpath, img)
            picklepath = path + '/' + fileid + '.pkl'
            with open(picklepath,"wb") as f_dump:
                pickle.dump(img_loc, f_dump)
            f_dump.close()

def trainImageSegementation(inkmlfilepath):
    files = glob.glob(inkmlfilepath)
    for inkmlfilename in files:
            fileid = inkmlfilename[15:-6]
            print(fileid)
            ground_truth = readCharacterListFromInkmlFile(inkmlfilename)
            pngfilename = 'data/trainPNG/' + fileid + '.png'
            oriimg = imgReadIn(pngfilename)
            binimg = imgConvert(oriimg)
            imgs = imgSegmentation(binimg)
            print(len(imgs))
            if(len(imgs) == len(ground_truth)):
                for i in range(len(imgs)):
                    path = os.path.join('data/trainPNGSeg', ground_truth[i])
                    if(os.path.exists(path)):
                        pathpng = path + '/' +ground_truth[i] + '/*.png'
                        imgpath = path + '/' + ground_truth[i] + '_' + str(len(glob.glob(pathpng))+1) + '.png'
                    else: 
                        os.mkdir(path)
                        imgpath = path + '/' + ground_truth[i] + '_1.png'
                    cv2.imwrite(imgpath, imgs[i]['segment_img'])


def readCharacterListFromInkmlFile(filename):
    ground_truth = [] # start with $, end with $
    with open(filename, 'r') as file:
        tree = ET.parse(file)
        root = tree.getroot()
        for annotation in root.findall('{http://www.w3.org/2003/InkML}annotation'):
            if (annotation.get('type')) == 'truth':
              ground_truth.append(annotation.text)
        parsedgt = groundTruthParser(ground_truth)
    return parsedgt

def groundTruthParser(ground_truth):
    gt = ground_truth[0]
    gt = gt.replace(' ','')
    gt = gt.replace('$','')
    gt = gt.replace('\\gt','>')
    gt = gt.replace('\\lt','<')
    gt = gt.replace('\\log','log')
    gt = gt.replace('\\cos','cos')
    gt = gt.replace('\\tan','tan')
    gt = gt.replace('\\sin','sin')
    gt = gt.replace('\\lim','lim')
    gt = gt.replace('=','--')
    gt_list = []
    for i in gt:
        if(len(gt)==0):
            break
        i = gt[0]
        gt = gt[1:]
        if(i == '\\'):
            for s in symbol:
                if(gt[0:len(s)] == s):
                    gt_list.append(s)
                    gt = gt[len(s):]
        else:
            gt_list.append(i)
    return gt_list

#path1 = 'data/testPNG/*.png' 
path1 = 'data/trainDat1/*.inkml' 
trainImageSegementation(path1)

