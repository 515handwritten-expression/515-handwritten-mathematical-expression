from PIL import Image
import os
trainData = []
trainLabels = []

for root, dirs, files in os.walk('trainPNGSeg'):
    for file in files:
        if (file != ".DS_Store"):
            img = Image.open(os.path.join(root, file), "r")
            trainData.append(img)
            label = '_'.join(file.split('_')[:-1])
            trainLabels.append(label)



# load and compile the LeNet model
model = model.classfier()

model = model.train(model,trainData,trainLabels)
# score = model.eval(model,testData,testLabel)

# train the network


# save the serialized network weights to disk so it can be reused (optional)

