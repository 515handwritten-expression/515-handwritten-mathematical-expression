# Reference: https://pub.towardsai.net/the-architecture-implementation-of-lenet-5-eef03a68d1f7
# Reference: https://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.optimizers import SGD
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense
from keras.models import Sequential

class classfier:

    def __init__(self):
        # initialize sequential model
        model = Sequential()
        # Add the first convolution layer
        model.add(Convolution2D(filters=32, kernel_size=(3, 3), padding="same", input_shape=(32,32,1),activation='relu'))
        # 2 x 2 max-pooling
        model.add(MaxPooling2D(pool_size=(3, 3), strides=3))
        # define the second set
        model.add(Convolution2D(filters=64, kernel_size=(3, 3), padding='same',activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3), strides=3))
        # take the output of the preceding MaxPooling2D  layer and flatten it into a single vector
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation('relu'))
        # dropout?
        model.add(Dense(24))
        model.add(Activation("softmax"))
        model.summary()

    def train(model, trainData, trainLabels):
        model.compile(loss="categorical_crossentropy", optimizer=SGD(lr=0.01), metrics=["accuracy"])
        model.fit(trainData, trainLabels, batch_size=128, epochs=20, verbose=1)
        return model

    def eval(model, testData, testLabels):
        print("[INFO] evaluating...")
        score = model.evaluate(testData, testLabels, batch_size=128, verbose=1)
        print('Test Loss:', score[0])
        print('Test accuracy:', score[1])
        return score
