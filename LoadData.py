import inkml2img
import glob

path1 = 'data/trainData/*.inkml' 
files = glob.glob(path1)
for filename in files:
    fileid = filename[15:-6]
    outputfile = "./data/trainPNG/" + fileid + ".png"
    inkml2img.inkml2img(filename,outputfile)

path2 = 'data/testData/*.inkml' 
files = glob.glob(path2)
for filename in files:
    fileid = filename[15:-6]
    outputfile = "./data/testPNG/" + fileid + ".png"
    inkml2img.inkml2img(filename,outputfile)

