"""
This module intakes a string of math expression and convers it to LaTex expression.
It writes the output strinf into "results/MathJaxResult.txt".
"""
import re,os
import os.path
from os import path

# Note: not able to test this module on Travis CI because the working directory is different from where Front end calls this module
def convertMathjax(string):                             # pragma: no cover
    result = stringToMathJax(string)                    # pragma: no cover
    if path.exists("results/MathJaxResult.txt"):        # pragma: no cover
        os.remove("results/MathJaxResult.txt")          # pragma: no cover
    f = open("results/MathJaxResult.txt", "w")          # pragma: no cover
    f.write(str(result))                                # pragma: no cover
    f.close()                                           # pragma: no cover

# return the Latex string of the expression
def stringToMathJax(string):
    # first deal with power since need to insert brackets for power. e.g. 2^2 -> 2^{2}
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
    
    # then just replace all other operators and special chars with the LaTex syntax
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
