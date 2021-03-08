import xml.etree.ElementTree as ET

# parse an xml file. example of parameter: "test.xml"
def parseXml(file):
    newtree = ET.parse(file)
    root = newtree.getroot()
    print(traceTree(root))

# return the calculated result from the parsed xml tree
# If the tree contains letters, return an IncalculableError
def traceTree(root):
    #print(root.tag)
    if root.tag == "number":
        return root.attrib["value"]
    elif root.tag == "expression":
        return traceTree(root[0])
    else:
        num1 = traceTree(root[0])
        try:
            num1 = float(num1)
        except ValueError:
            if num1 == "pi":
                num1 = 3.1415
            else:
                raise IncalculableError
        num2 = None
        if len(root > 1):
            num2 = traceTree(root[1])
            try:
                num2 = float(num2)
            except ValueError:
                if num2 == "pi":
                    num2 == 3.1415
                else:
                    raise IncalculableError
        result = calculation(root.tag, num1, num2)
        return result

# Calculate the result using given information
def calculation(tag, num1, num2=None):
    if tag == "+":
        return num1+num2
    elif tag == "-":
        return num1-num2
    elif tag == "div":
        try:
            return num1/num2
        except ValueError:
            raise IncalculableError
    elif tag == "times":
        return num1*num2
    elif tag == "^":
        return num1**num2
#    elif tag == "log":
#        try:
#            return math.log(num1)
#        except ValueError:
#            raise IncalculableError
#    elif tag == "sin":
#        return math.sin(num1)
#    elif tag == "cos":
#        return math.cos(num1)
#    elif tag == "tan":
#        return math.tan(num1)
#    elif tag == "sqrt":
#        try:
#            return math.sqrt(num1)
#        except ValueError:
#            raise IncalculableError
#    elif tag == "factorial":
#        try:
#            return math.factorial(num1)
#        except ValueError:
#            raise IncalculableError
    else:
        return None

class IncalculableError(Exception):
    def __init__(self):
        print("Unable to calculate")


