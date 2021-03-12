import xml.etree.ElementTree as ET
from cv2 import cv2
import numpy as np
import glob
import os
import shutil
import pickle
from skimage.morphology import skeletonize
STANDARD_SIZE = 32
symbol = ['alpha','beta','gamma','phi','pi','geq','leq','pm','theta','infty','div','times','sum','ldots','neq','rightarrow','int','sqrt', 'exists','forall','in']

#Read image from file 
#Convert original image before image segmentation 
def imgReadAndConvert(imgfilename):
    original_img = cv2.imread(imgfilename)   
    # inspect error object
    img_copy = original_img.copy()
    height = img_copy.shape[0]
    width = img_copy.shape[1]
    #Image resize(prevent overflow)
    if(height*width*1000)> 2^31:
        resize = img_copy
    elif(height * width > 2^31):
        resize = cv2.resize(img_copy, dsize =(0.0001, int(0.01*height/width)), interpolation = cv2.INTER_AREA)
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
    #Reverse image color
    bin_img = cv2.bitwise_not(bin_img)
    return bin_img

#Get croppped images and skeletonize
def imgSkeleton(original_img):
    ret,binary_img = cv2.threshold(original_img,0,1,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    extracted_img = skeletonize(binary_img)
    skeleton = extracted_img.astype(np.uint8) * 255
    skeleton = cv2.bitwise_not(skeleton)
    return skeleton
 
def getVerticalProjectionSegmentationPoints(img):
    height, width = img.shape[:2]
    W = np.zeros(width,dtype=np.int32)
    for x in range(0, width):    
        for y in range(0, height):
            if img[y,x] == 0:
                W[x] += 1
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
    return W_Start, W_End

def getHorizontalProjectionSegmentationPoints(img):
    height, width = img.shape[:2]
    H = np.zeros(height,dtype=np.int32)
    for y in range(0, height):    
        for x in range(0, width):
            if img[y,x] == 0:
                H[y] += 1
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
    return H_Start, H_End

#Crop the original image along with the horizontal direction 
#For each cropped images, crop the image along with the vertical direction 
#Return the final segmenting position 
def projectionSegmentation(img):
    h,w =img.shape[:2]
    Position = []
    imgs = []
    H_Start, H_End = getHorizontalProjectionSegmentationPoints(img)
    #For each cropped images, crop the image along with the vertical direction
    for j in range(len(H_Start)):
        cropImg = img[H_Start[j]:H_End[j], 0:w]
        W_Start, W_End = getVerticalProjectionSegmentationPoints(cropImg)
        for x in range(len(W_Start)):
            Position.append([W_Start[x],H_Start[j],W_End[x],H_End[j]])
            img_aftercrop = img[H_Start[j]:H_End[j], W_Start[x]:W_End[x]]
            imgs.append(img_aftercrop)
    return imgs, Position


#After projection segmentation, for each cropped image, 
#cropped off the white space and only keep the character
#Resize and skeletonize the cropped images and store th images 
#and positions into a list of dictionaries
def imgStandardize(imgs,Position):
    character_list = []
    loc = []
    for i in range(len(imgs)):
        #Crop horizontally
        H_Start, H_End = getHorizontalProjectionSegmentationPoints(imgs[i])
        #Crop vertically
        W_Start, W_End = getVerticalProjectionSegmentationPoints(imgs[i])
        #If projection values are not zero at the very end, 
        # set w or h as the end point of croping 
        if(len(W_End)<len(W_Start)):
            W_End.append(imgs[i].shape[1])
        if(len(W_End) == 0):
            W_End.append(imgs[i].shape[1])
        if(len(H_End)<len(H_Start)):
            H_End.append(imgs[i].shape[0])
        if(len(H_End) == 0):
            H_End.append(imgs[i].shape[0])
        char_img = imgs[i][H_Start[0]:H_End[-1],W_Start[0]:W_End[-1]]
        h, w = char_img.shape[:2]
        W1 = Position[i][0]
        H1 = Position[i][1]
        W2 = Position[i][2]
        H2 = Position[i][3]
        loc.append([W1+W_Start[0],H1+H_Start[0],W2-(imgs[i].shape[1]-W_End[-1]),H2-(imgs[i].shape[0]-H_End[-1])])
        #Resize the image to the standard size of 32 * 32 
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
        standard_img = cv2.bitwise_not(standard_background)
        #Skeletonize the image 
        standard_img = imgSkeleton(standard_img)
        character_list.append(standard_img)
        standard_imgs=[]
        #Store the location and segment images in a list 
    for i in range(len(character_list)):
        standard_imgs.append({'location':loc[i],'segment_img':character_list[i]})
        #Sort the images along with the horizontal direction 
        #standard_imgs.sort(key=lambda x:x['location'][0]) 
    return standard_imgs

#Segment test images 
def testImageSegementation(filepath):
    files = glob.glob(filepath)
    # path is 'data/testData/*.png'
    num = 0
    for filename in files:
            fileid = filename[13:-4]
            num += 1
            print(fileid + ':successfully loaded'  + '-' + str(num))
            #Read in original image 
            #Convert image 
            binimg = imgReadAndConvert(filename)
            cropimgs, Position = projectionSegmentation(binimg)
            imgs = imgStandardize(cropimgs,Position)
            img_list = []
            img_loc = []
            for i in range(len(imgs)):
                img_list.append(imgs[i]['segment_img'])
                img_loc.append(imgs[i]['location'])
            path = os.path.join('data/testPNGSeg', fileid)
            if(os.path.exists(path)):
                shutil.rmtree(path)
            os.mkdir(path) 
            for index, img in enumerate(img_list, start=1):
                if index < 10:
                    strindex = '0' + str(index)
                else:
                    strindex = str(index)
                imgpath = path + '/' + strindex + '.png'
                cv2.imwrite(imgpath, img)
            #Store the position as a pickle file 
            picklepath = path + '/' + fileid + '.pkl'
            with open(picklepath,"wb") as f_dump:
                pickle.dump(img_loc, f_dump)
            f_dump.close()

# Read ground truth from inkml file (for training)
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

# Parse ground truth into a list of symbols 
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

# Segment training data 
def trainImageSegementation(inkmlfilepath):
    files = glob.glob(inkmlfilepath)
    num = 0
    for inkmlfilename in files:
        num +=1
        # path = 'data/trainData/*.inkml' 
        fileid = inkmlfilename[15:-6]
        pngfilename = 'data/trainPNG/' + fileid + '.png'
        if(not os.path.isfile(pngfilename)):
            print(fileid +': PNG file not exist' + '-' + str(num))
            continue
        print(fileid + ':successfully loaded'  + '-' + str(num))
        ground_truth = readCharacterListFromInkmlFile(inkmlfilename)
        binimg = imgReadAndConvert(pngfilename)
        cropimgs, Position = projectionSegmentation(binimg)
        imgs = imgStandardize(cropimgs,Position)
        if(len(imgs) == len(ground_truth)):
            for i in range(len(imgs)):
                path = os.path.join('data/trainPNGSeg', ground_truth[i])
                if(os.path.exists(path)):
                    pathpng = path + '/*.png'
                    imgpath = path + '/' + ground_truth[i] + '_' + str(len(glob.glob(pathpng))+1) + '.png'
                else: 
                    os.mkdir(path)
                    imgpath = path + '/' + ground_truth[i] + '_1.png'
                cv2.imwrite(imgpath, imgs[i]['segment_img'])


#filepath = 'data/trainData/*.inkml' 
#trainImageSegementation(filepath)
filepath = 'data/predPNG/*.png' 
testImageSegementation(filepath)
# %
