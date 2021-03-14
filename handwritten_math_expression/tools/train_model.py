# Reference: https://pub.towardsai.net/the-architecture-implementation-of-lenet-5-eef03a68d1f7
# Reference: https://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/

import keras
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import numpy as np


# generate training data-75% and validation data-25%
train_data_dir = "/trainPNGSeg/Shareddrives/515_handwritten/trainPNGSeg"
data_gen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split=0.25)

train_dataset = data_gen.flow_from_directory(train_data_dir, target_size=(32, 32), color_mode="grayscale", batch_size= 15, subset='training')
validation_dataset = data_gen.flow_from_directory(train_data_dir, target_size=(32, 32), color_mode="grayscale", batch_size= 15, subset='validation')

# numClasses = how many characters total in label_map
label_map = (train_dataset.class_indices)
numClasses = len(label_map)

# save tge label_map to local as .npy
np.save('label_map_v3.npy', label_map)

# overwrite and save the model with the best val_acc (the accuracy of a batch of testing data)
checkpoint = ModelCheckpoint(train_data_dir, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

# initialize lenet model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(5,5), strides=(1,1), padding='same', input_shape = (32,32,1), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Conv2D(filters=48, kernel_size=(5,5), strides=(1,1), padding='valid', activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=84, activation='relu'))
model.add(Dense(units=numClasses, activation = 'softmax'))

# compile model & fit model with training and validation data
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("training...")

model.fit(train_dataset, steps_per_epoch = len(train_dataset), validation_data = validation_dataset,  validation_steps = len(validation_dataset), epochs = 15, callbacks = [checkpoint])

#saving model to .h5 file in train_data_dir
print("saving model...")
model.save('LeNetModel_v3.h5')

print("evaluating...")
score = model.evaluate(validation_dataset)
print('Test Loss:', score[0])
print('Test accuracy:', score[1])

