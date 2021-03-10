import keras
from keras.callbacks import ModelCheckpoint
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator

# numClasses = how many characters total
numClasses = 30

# generate training data-75% and validation data-25%
train_data_dir = "/trainPNGSeg/Shareddrives/515_handwritten/trainPNGSeg"
data_gen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True, validation_split=0.25)

train_dataset = data_gen.flow_from_directory(train_data_dir, target_size=(32, 32), color_mode="grayscale", batch_size= 15, subset='training')
validation_dataset = data_gen.flow_from_directory(train_data_dir, target_size=(32, 32), color_mode="grayscale", batch_size= 15, subset='validation')

# overwrite and save the model with the best val_acc (the accuracy of a batch of testing data)
checkpoint = ModelCheckpoint(train_data_dir, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')

# initialize lenet model
model = Sequential()
model.add(Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), input_shape = (32,32,1), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(1,1)))

model.add(Conv2D(filters=64, kernel_size=(3,3), strides=(1,1), activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=(1,1)))

model.add(Flatten())
model.add(Dense(units=120, activation='relu'))
model.add(Dense(units=84, activation='relu'))
model.add(Dense(units=numClasses, activation = 'softmax'))

# compile model & fit model with training and validation data
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print("training...")
model.fit_generator(train_dataset, steps_per_epoch = len(train_dataset), validation_data = validation_dataset,  validation_steps = len(validation_dataset), epochs = 15, callbacks = [checkpoint])

#saving model to .h5 file in train_data_dir
print("saving model...")
model.save('LeNetModel.h5')

print("evaluating...")
score = model.evaluate(validation_dataset)
print('Test Loss:', score[0])
print('Test accuracy:', score[1])
