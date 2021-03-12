import numpy as np
import os, string, pickle
from os.path import isfile
import shutil
from cv2 import cv2
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import ImagePreprocessing as ip

labels = []
positions = []
numeric = string.digits + "e" + "pi"
image_inputpath = './data/testimg/testinkml_1.png'
segimg_savepath = './data/testimg'

#read in input image and do segmantation and resize
def predictImageSegementation(filename,savepath):
    #13 need to be changed according to input path
    fileid = filename[13:-4]
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
    print(input_img_path)
    print ("pred",predictions)
    return predictions

class ModelInputError(Exception):
    def __init__(self):
        self.msg = "Unable to file segments and/or location file"

filepath = "/trainPNGSeg/Shareddrives/515_handwritten/test_2"

#input a folder with all segments.npg and a position.pkl
#output a list of labels and a list of positions
def write_labels_for_all_segs(filepath):
  model = load_model('LeNetModel_v3.h5')
  label_map = 'label_map_v3.npy'
  label = []

  for root,dir,files in os.walk(filepath):
    for file in sorted(files):
      if file.endswith('png'):
        single_label = predict_single_label(os.path.join(root, file),model,label_map)
        # single_label[0] is the value, [1] is the tag (numeric or operator)
        if single_label[0] in numeric:
          single_label.append("numeric")
        else:
          single_label.append("operator")
        label.append(single_label)
      elif file.endswith('pkl'):
        print("pkl:",file)
        with open(os.path.join(root, file), 'rb') as f:
          positions = pickle.load(f)
      else:
        raise ModelInputError

  return label,positions

predictImageSegementation(image_inputpath,segimg_savepath)
labels,positions = write_labels_for_all_segs(segimg_savepath)
print("labels:", labels)
print("positions:",positions)
