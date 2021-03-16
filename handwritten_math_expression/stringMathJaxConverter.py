import string,re,os
import os.path
from os import path

def convertMathjax(string):
    result = stringToMathJax(string)
    if path.exists("results/MathJaxResult.txt"):
        os.remove("results/MathJaxResult.txt")
    f = open("results/MathJaxResult.txt", "w")
    f.write(str(result))
    f.close()

# return the MathJax expression from the parsed xml tree
def stringToMathJax(string):
    result = ""
    str_seg = re.findall(r"([a-z]+|\d|[-+()/*^])", string)
    numhat = re.findall(r"\^", string)
    i=0
    if len(numhat) != 0:
      for i in range(len(str_seg)+len(numhat)+1):
          element = str_seg[i]
          if(element == "^"):
            str_seg.insert(i+1, "{ ")
            str_seg.insert(i+3, " }")
      for ele in str_seg:
        result += ele
    else:
      result = string

    #string.replace(old, new)
    result = result.replace("+"," + ")
    result = result.replace("-"," - ")
    result = result.replace("pi"," \\pi ")
    result = result.replace("*"," \\times ")
    result = result.replace("/" ," \\div ")
    result = result.replace("neq"," \\neq ")
    result = result.replace("geq" ," \\geq ")
    result = result.replace("gt" ," \\gt ")
    result = result.replace("leq" ," \\leq ")
    result = result.replace("lt" ," \\lt ")
    result = result.replace("pm" ," \\pm ")

    return result

convertMathjax("1+1")