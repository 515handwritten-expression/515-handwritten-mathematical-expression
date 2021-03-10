import inkml2img
import glob

path1 = 'data/TrainINKML_2013/*.inkml' 
files = glob.glob(path1)
for filename in files:
    fileid = filename[21:-6]
    outputfile = "./data/TrainINKML_2013PNG/" + fileid + ".png"
    inkml2img.inkml2img(filename,outputfile)

path2 = 'data/TestINKML_2013/*.inkml' 
files = glob.glob(path2)
for filename in files:
    fileid = filename[20:-6]
    outputfile = "./data/TestINKML_2013PNG/" + fileid + ".png"
    inkml2img.inkml2img(filename,outputfile)
