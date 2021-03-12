# Reference: https://github.com/Huzaifa-Imran/binaryTreeCreator/tree/5cb2c0b969d516948e7cf5c008965324a99ed670
import re
import math
import os.path
from os import path

class Node():
    def __init__(self, value):
        self.value = self.val = value
        self.left = None
        self.right = None

def infixToPostfix(expression):
    stack = []
    postfix = []
    index = 0
    prec = {'+': 2, '-': 2, '*': 3, '/': 3, '(': 1 ,'^':4}
    while(index < len(expression)):
        element = expression[index]
        if element in "+-*/^":
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

def calc(postfix):
    stack = []
    for node in postfix:
        print(node.value)
        if node.value in "+-*/^":
            try:
                rightVal = int(stack.pop())
                leftVal = int(stack.pop())
            except ValueError:
                print("\nCannot calculate result. Expression has non integer operands.")
                break
            except IndexError:
                print("\nInvalid Expression. Exiting...")
                exit()
            if node.value == '+':
                stack.append(leftVal + rightVal)
            elif node.value == '-':
                stack.append(leftVal - rightVal)
            elif node.value == '*':
                stack.append(leftVal * rightVal)
            elif node.value == '^':
                stack.append(math.pow(leftVal, rightVal))
            elif node.vale == '/':
                stack.append(leftVal / rightVal)
        else:
            stack.append(node.value)
    else:
        if not stack:
            stack.append(0)
        result = stack.pop()
        return result

def expressionTree(expression):
    postfix = infixToPostfix(expression)
    return calc(postfix)

def writeCalResult(expression):
    try:
        result = expressionTree(expression)
    except IncalculableError:
        result = "Unable to calculate"
    if path.exists("calculationResult.txt"):
        os.remove("calculationResult.txt")
    f = open("calculationResult.txt", "w")
    f.write(str(result))
    f.close()
    
'''
    stack = []
    for node in postfix:
        print(node.value)
        if node.value in '+-*/^':
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
        else:
            stack.append(node)
    return {stack.pop()} if stack != [] else None
'''

