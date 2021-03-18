"""
This module intakes a string of math expression and uses expression tree to preform the calculation.
It supports floats, pi, e, and basic math operations such as plus, minus, devide, times, and power.
It writes its calculation result into "results/calculationResult.txt" file.

Reference: https://github.com/Huzaifa-Imran/binaryTreeCreator/tree/5cb2c0b969d516948e7cf5c008965324a99ed670
"""
import re
import math
import os.path
from os import path
import string

class Node():
    def __init__(self, value):
        self.value = self.val = value
        self.left = None
        self.right = None

# change the infix string to postfix string, read as left child, right child, root
# e.g. 1+2 -> 12+
def infixToPostfix(expression):
    stack = []
    postfix = []
    index = 0
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '(': 1 ,'^':4}
    while(index < len(expression)):
        element = expression[index]
        if(element in "+-*^/"):
            if stack == []:
                stack.append(element)
            else:
                top = stack[-1]
                if prec[element] > prec[top]:
                    stack.append(element)
                elif prec[top] == prec[element]:
                    postfix.append(stack.pop())
                    stack.append(element)
                else:
                    postfix.append(stack.pop())
                    continue
        elif element == '(':
            stack.append(element)
        elif element == ')':
            top = stack.pop()
            while top != '(':
                postfix.append(top)
                top = stack.pop()
        else:
            postfix.append(element)
        index += 1
    while stack != []:
        postfix.append(stack.pop())
    return [Node(x) for x in postfix]

# perform calculation using expression tree
# input: a string of expression, output: a float of the calculation result
def expressionTree(expression):
    expression = expression.replace("pi","3.1416")
    expression = expression.replace("e","2.7183")
    invalid = string.ascii_letters + '='
    for char in expression:
        if char in invalid:
            raise IncalculableError
            break
    expression = re.findall(r"([0-9.]+|\d|[-+()/*^])", expression)
    if len(expression) == 1:
        return round(float(expression[0]), 4)
    postfix = infixToPostfix(expression)
    stack = []
    for node in postfix:
        if node.value in "+-*/^":
            try:
                rightVal = float(stack.pop())
                leftVal = float(stack.pop())
            except IndexError:
                raise IncalculableError
                exit()
            if node.value == '+':
                stack.append(leftVal + rightVal)
            elif node.value == '-':
                stack.append(leftVal - rightVal)
            elif node.value == '*':
                stack.append(leftVal * rightVal)
            elif node.value == '^':
                stack.append(math.pow(leftVal, rightVal))
            else:
                try:
                    stack.append(leftVal / rightVal)
                except:
                    raise IncalculableError
        else:
            stack.append(node.value)
    else:
        if not stack:
            stack.append(0)
        calc_result = stack.pop()
        
    stack = []
    for node in postfix:
        if node.value in '+-*/^':
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(node)
    calc_result = round(calc_result, 4)
    return calc_result

class IncalculableError(Exception):                                 # pragma: no cover
    def __init__(self):                                             # pragma: no cover
        print("Unable to calculate")                                # pragma: no cover

# Note: not able to test this module on Travis CI because the working directory is different from where Front end calls this module
def writeCalResult(expression):                                     # pragma: no cover
    try:                                                            # pragma: no cover
        result = expressionTree(expression)                         # pragma: no cover
    except IncalculableError:                                       # pragma: no cover
        result = "Unable to calculate"                              # pragma: no cover
    if path.exists("results/calculationResult.txt"):                # pragma: no cover
        os.remove("results/calculationResult.txt")                  # pragma: no cover
    f = open("results/calculationResult.txt", "w")                  # pragma: no cover
    f.write(str(result))                                            # pragma: no cover
    f.close()                                                       # pragma: no cover
