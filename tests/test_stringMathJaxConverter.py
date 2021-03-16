import unittest
import handwritten_math_expression.stringMathJaxConverter as MJAX
import os.path

class TestCalculation(unittest.TestCase):

    def testMathJaxComponent(self):
        self.assertEqual(MJAX.stringToMathJax("1+2-1"), "1 + 2 - 1")
        self.assertEqual(MJAX.stringToMathJax("1/2"), "1 \\div 2")
        self.assertEqual(MJAX.stringToMathJax("1*2"), "1 \\times 2")
        self.assertEqual(MJAX.stringToMathJax("1geq2"), "1 \\geq 2")
        self.assertEqual(MJAX.stringToMathJax("1gt2"), "1 \\gt 2")
        self.assertEqual(MJAX.stringToMathJax("1leq2"), "1 \\leq 2")
        self.assertEqual(MJAX.stringToMathJax("1lt2"), "1 \\lt 2")
        self.assertEqual(MJAX.stringToMathJax("(apmb)neqc"), "(a \\pm b) \\neq c")
        self.assertEqual(MJAX.stringToMathJax("i^2"), "i^{ 2 }")

if __name__ == '__main__':
    unittest.main()