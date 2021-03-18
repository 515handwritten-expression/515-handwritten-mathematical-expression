"""
This is the main function that gets called by the front end. It reads a PNG image of math expression from the 'upload' folder, calls the image preprocessing module, load the saved Lenet model to do the prediction, calls the generateStrForLatexAndTree module to do the post-processing and calls the calculation module and MathJaxConverter to create the output files. These two module would write the expression in LaTex syntax to a TXT file, and the calculation result to another TxT file in the 'results' folder.
"""
import numpy as np
import os, string, pickle, shutil
from os.path import isfile
from cv2 import cv2
import glob
# from handwritten_math_expression 
import stringCalculation, stringMathJaxConverter, generateStrForLatexAndTree
# from handwritten_math_expression 
import ImagePreprocessing as ip
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

#read in input image and do segmantation and resize
def predictImageSegementation(uploadpath,savepath):
    files = glob.glob(uploadpath)
    fileid = 'imgseg'
    for filename in files:
        #Read in original image 
        #Convert image 
        binimg = ip.imgReadAndConvert(filename)
        cropimgs, Position = ip.projectionSegmentation(binimg)
        imgs = ip.imgStandardize(cropimgs,Position)
        img_list = []
        img_loc = []
        for i in range(len(imgs)):
            img_list.append(imgs[i]['segment_img'])
            img_loc.append(imgs[i]['location'])
        path = os.path.join(savepath, fileid)
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

# input the path of a single image, output a single label
def predict_single_label(input_img_path,model,label_map):
    #input image for prediction, a single image at a time
    image = load_img(input_img_path,target_size=(32, 32), color_mode="grayscale")
    input_arr = img_to_array(image)

    # Convert single image to a batch and predict
    input_arr = np.array([input_arr])
    pred = model.predict(input_arr)

    # read lavel_map from local
    if isfile(label_map):
        class_indices = np.load(label_map,allow_pickle=True).item()

    # predicted_class_indices = location of the predicted label in label_map
    # predictions = the actual predicted label
    predicted_class_indices=np.argmax(pred, axis =1 )
    class_indices = dict((v, k) for k, v in class_indices.items())
    predictions = [class_indices[k] for k in predicted_class_indices]
    print("input_img_path:",input_img_path)
    print("pred",predictions)
    return predictions

#input a folder with all segments.npg and a position.pkl
#output a list of predicted labels and a list of positions
def write_labels_for_all_segs(filepath):
  model = load_model('../LeNetModel_v3.h5')
  label_map = '../label_map_v3.npy'
  label = []
  positions = []
  filepath = os.path.join(filepath, "imgseg")
  for root,dir,files in os.walk(filepath):
    for file in sorted(files):
      print("file:",file)
      if file.endswith('png'):
        single_label = predict_single_label(os.path.join(root, file),model,label_map)
        label += single_label
      elif file.endswith('pkl'):
        print("pkl:",file)
        with open(os.path.join(root, file), 'rb') as f:
          positions = pickle.load(f)
  return label,positions

def my_func():
    labels = []
    positions = []
    image_inputpath = 'uploads/*.png' 
    segimg_savepath = 'uploads'

    predictImageSegementation(image_inputpath,segimg_savepath)
    # a list of predicted labels and a list of positions
    (labels,positions) = write_labels_for_all_segs(segimg_savepath)
    # convert 2 lists into a string by comparing the position of each pair of chars
    # string_for_calc had zeros inserted before all negative numbers. e.g. (0-2) for -2
    string_for_latex,string_for_calc = generateStrForLatexAndTree.getStringsForLatexAndTree(labels,positions)
    
    # this function takes a string of expression, output calculation result to txt
    stringCalculation.writeCalResult(string_for_calc)
    # this function takes a string of expression, output LaTex expression to txt
    stringMathJaxConverter.convertMathjax(string_for_latex)


if __name__ == '__main__':
    # test1.py executed as script
    # do something
    my_func()
