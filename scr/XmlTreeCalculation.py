import xml.etree.ElementTree as ET
import math

# return the calculated result from the parsed xml tree
# If the tree contains letters, return an IncalculableError
def traceTree(root):
    #print(root.tag)
    if root.tag == "number":
        return root.attrib["value"]
    elif root.tag == "expression":
        return traceTree(root[0])
    elif len(root) < 2:
        raise IncalculableError
    else:
        num1 = traceTree(root[0])
        if num1 == "pi":
            num1 = 3.1415
        elif num1 == "e":
            num1 = math.e
        elif num1 == "" and (root.tag == "plus" or root.tag == "minus"):
            num1 = 0
        else:
            try:
                num1 = float(num1)
            except (ValueError,TypeError) as e:
                raise IncalculableError
        num2 = traceTree(root[1])
        if num2 == "pi":
            num2 = 3.1415
        elif num2 == "e":
            num2 = math.e
        else:
            try:
                num2 = float(num2)
            except (ValueError,TypeError) as e:
                raise IncalculableError
        result = calculation(root.tag, num1, num2)
        return result

# Calculate the result using given information
def calculation(tag, num1, num2):
    if tag == "plus":
        return round(num1+num2,10)
    elif tag == "minus":
        return round(num1-num2,10)
    elif tag == "div":
        try:
            return round(num1/num2,10)
        except ZeroDivisionError:
            raise IncalculableError
    elif tag == "times":
        return round(num1*num2,10)
    elif tag == "power":
        return round(num1**num2,10)
    else:
        raise IncalculableError
        return None

class IncalculableError(Exception):
    def __init__(self):
        self.msg = "Unable to calculate"

#file = "test/constantPi.xml"
#newtree = ET.parse(file)
#root = newtree.getroot()
#print(traceTree(root))
