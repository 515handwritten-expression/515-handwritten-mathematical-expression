import xml.etree.ElementTree as ET

#load datasets
ground_truth = [] # start with $, end with $

with open('formulaire001-equation030.inkml', 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()
    for annotation in root.findall('{http://www.w3.org/2003/InkML}annotation'):
        if (annotation.get('type')) == 'truth':
            ground_truth.append(annotation.text)
for i in range(len(ground_truth)):
    print(ground_truth[i])


# training files


# partition dataset into training and testing splits


# load and compile the LeNet model


# train the network

# save the serialized network weights to disk so it can be reused (optional)

