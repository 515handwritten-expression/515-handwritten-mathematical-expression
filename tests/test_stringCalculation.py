import unittest
import handwritten_math_expression.stringCalculation as XTC
from handwritten_math_expression.stringCalculation import IncalculableError
import os.path, math

class TestCalculation(unittest.TestCase):

    def testNode(self):
        node = XTC.Node("1")
        self.assertEqual(node.value,"1")
        self.assertEqual(node.left,None)
        self.assertEqual(node.right, None)

    def testConstant(self):
        self.assertEqual(XTC.expressionTree("pi"),3.1416)
        self.assertEqual(XTC.expressionTree("e"),2.7183)
        self.assertEqual(XTC.expressionTree("1"), 1)
        self.assertEqual(XTC.expressionTree(""), 0)

    def testCalculationPlus(self):
        self.assertEqual(XTC.expressionTree("1+2"),3.0)
        self.assertEqual(XTC.expressionTree("1.5+2"),3.5)
        self.assertEqual(XTC.expressionTree("pi+1"),4.1416)

    def testCalculationMinus(self):
        self.assertEqual(XTC.expressionTree("1-2"),-1)
        self.assertEqual(XTC.expressionTree("1-(0-2)"),3)
        self.assertEqual(XTC.expressionTree("1-((0-2))"),3)
        self.assertEqual(XTC.expressionTree("1.1-0.2"),0.9)

    def testCalculationTimes(self):
        self.assertEqual(XTC.expressionTree("1*2"),2)
        self.assertEqual(XTC.expressionTree("2*0"),0)
        self.assertEqual(XTC.expressionTree("(0*0)"),0)
        self.assertEqual(XTC.expressionTree("1.1*0.2"),0.22)

    def testCalculationDiv(self):
        self.assertEqual(XTC.expressionTree("(1/(1+1))"),0.5)
        self.assertEqual(XTC.expressionTree("0/2"),0)

    def testCalculationPower(self):
        self.assertEqual(XTC.expressionTree("1^2"),1.0)
        self.assertEqual(XTC.expressionTree("2^2^2"),16.0)

    def testInfixToPostfixNo1(self):
        result = []
        expected = ['3', '1', '-', '1', '^']
        postfix = XTC.infixToPostfix("(3-1)^1")
        for node in postfix:
            result += node.value
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def testInfixToPostfixNo2(self):
        result = []
        expected = ['1', '2', '^', '2', '+', '3', '*', '1', '/']
        postfix = XTC.infixToPostfix("(1^2+2)*3/1")
        for node in postfix:
            result += node.value
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def testIncalculableError(self):
        self.assertRaises(IncalculableError, XTC.expressionTree, "2/0")
        self.assertRaises(IncalculableError, XTC.expressionTree, "2neq0")
        self.assertRaises(IncalculableError, XTC.expressionTree, "1+")
        self.assertRaises(IncalculableError, XTC.expressionTree, "^1")
        self.assertRaises(IncalculableError, XTC.expressionTree, "x=1")

if __name__ == '__main__':
    unittest.main()
