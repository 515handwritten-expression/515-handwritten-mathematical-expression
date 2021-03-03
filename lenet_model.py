# Reference: https://pub.towardsai.net/the-architecture-implementation-of-lenet-5-eef03a68d1f7
# Reference: https://www.pyimagesearch.com/2016/08/01/lenet-convolutional-neural-network-in-python/

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense
from keras.models import Sequential

class classfier:

    def __init__():
        # initialize sequential model
        model = Sequential()
        activation = 'tanh'
        # Add the first convolution layer
        model.add(Convolution2D(filters=6, kernel_size=(5, 5), padding="valid", input_shape=(28, 28, 1)))
        model.add(activation=activation)
        # 2 x 2 max-pooling
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # define the second set
        model.add(Convolution2D(filters=16, kernel_size=(5, 5), padding='valid'))
        model.add(activation=activation)
        model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
        # take the output of the preceding MaxPooling2D  layer and flatten it into a single vector
        model.add(Flatten())
        model.add(Dense(120))
        model.add(Activation("tanh"))
        # numClasses = number of chars to recognize
        model.add(Dense(numClasses))
        model.add(Activation("softmax"))

        model.summary()

    def train(model):
        model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
        model.fit(trainData, trainLabels, batch_size=128, epochs=20, verbose=1, validation_data=(testData, testLabels))
        # model.fit(trainData, trainLabels, batch_size=128, epochs=20, verbose=1)
        print("[INFO] evaluating...")
        score = model.evaluate(testData, testLabels, batch_size=128, verbose=1)
        return model