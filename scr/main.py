from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
from os.path import isfile

# input the path of a single image, output a single label
def predict(input_img_path)
    # loading saved model
    model = load_model('LeNetModel.h5')

    #input image for prediction, a single image at a time
    image = load_img(input_img_path,target_size=(32, 32), color_mode="grayscale")
    input_arr = img_to_array(image)

    # Convert single image to a batch and predict
    input_arr = np.array([input_arr])
    pred = model.predict(input_arr)

    # read lavel_map from local
    if isfile('label_map.npy'):
        class_indices = np.load('label_map.npy',allow_pickle=True).item()

    # predicted_class_indices = location of the predicted label in label_map
    # predictions = the actual predicted label
    predicted_class_indices=np.argmax(pred, axis =1 )
    class_indices = dict((v, k) for k, v in class_indices.items())
    predictions = [class_indices[k] for k in predicted_class_indices]
    print (predictions)
    return predictions