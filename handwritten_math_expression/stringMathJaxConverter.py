import string
import os.path
from os import path

def convertMathjax(string):
    result = stringToMathJax(string)
    if path.exists("index/results/MathJaxResult.txt"):
        os.remove("index/results/MathJaxResult.txt")
    f = open("index/results/MathJaxResult.txt", "w")
    f.write(str(result))
    f.close()

# return the MathJax expression from the parsed xml tree
def stringToMathJax(string):
    #string.replace(old, new)
    result = string.replace("pi","\\pi")
    result = result.replace("*","\\times")
    result = result.replace("/" ,"\\div")
    result = result.replace("neq","\\neq")
    result = result.replace("geq" ,"\\geq")
    result = result.replace("gt" ,"\\gt")
    result = result.replace("leq" ,"\\leq")
    result = result.replace("lt" ,"\\lt")
    result = result.replace("pm" ,"\\pm")
    return result
