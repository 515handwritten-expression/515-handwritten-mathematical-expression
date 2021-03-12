import xml.etree.ElementTree as ET
import os.path
from os import path

def convertXmlMathjax(xml_tree):
    result = treeToMathJax(xml_tree.getroot())
    if path.exists("MathJaxResult.txt"):
        os.remove("MathJaxResult.txt")
    f = open("MathJaxResult.txt", "w")
    f.write(str(result))
    f.close()

# return the MathJax expression from the parsed xml tree
def treeToMathJax(root):
    if root.tag == "number":
        return root.attrib["value"]
    elif root.tag == "expression":
        return treeToMathJax(root[0])
    else:
        num1 = ""
        num2 = ""
        try:
            num1 = treeToMathJax(root[0])
        except IndexError:
            pass
        try:
            num2 = treeToMathJax(root[1])
        except IndexError:
            pass
        if num1 == "pi":
            num1 == "\pi"
        if num2 == "pi":
            num2 == "\pi"
        result = mathJaxComponent(root.tag, num1, num2)
        return result

# Make small component of the MathJax with the corresponding tag and number
def mathJaxComponent(tag, num1, num2):
    if tag == "plus":
        return num1 + " + " + num2
    elif tag == "minus":
        num2 = parenthesesCheck(num2)
        return num1 + " - " + num2
    elif tag == "power":
        num1 = parenthesesCheck(num1)
        return num1 + "^{" + num2 + "}"
    elif tag == "div":
        return "{" + num1 + " \over " + num2 + "}"
    elif tag == "equal":
        return num1 + " = " + num2
    elif tag == "times":
        num1 = parenthesesCheck(num1)
        num2 = parenthesesCheck(num2)
        return num1 + " \\times " + num2
    elif tag == "neq":
        return num1 + " \\neq " + num2
    elif tag == "geq" or tag == "gt" or tag == "leq" or tag == "lt" or tag == "pm":
        return num1 + " \\" + tag + " " + num2

# Check if we need parentheses around the number
def parenthesesCheck(num):
    try:
        float(num)
    except (ValueError,TypeError) as e:
        if num != "x" and num != "e" and num != "\pi":
            num = "(" + num + ")"
    return num

#print(mathJaxComponent("times", "1+1", "2"))

#print(treeToMathJax(ET.parse("data/xml/negativeNumber.xml").getroot()))