import unittest
import handwritten_math_expression.stringMathJaxConverter as MJAX
import os.path

class TestCalculation(unittest.TestCase):

    def testMathJaxComponent(self):
        self.assertEqual(MJAX.stringToMathJax("1+2"), "1+2")
        self.assertEqual(MJAX.stringToMathJax("1/2"), "1\\div2")
        self.assertEqual(MJAX.stringToMathJax("1*2"), "1\\times2")
        self.assertEqual(MJAX.stringToMathJax("1geq2"), "1\\geq2")
        self.assertEqual(MJAX.stringToMathJax("(a*b)neqc"), "(a\\timesb)\\neqc")
        self.assertEqual(MJAX.stringToMathJax("i^2"), "i^2")

if __name__ == '__main__':
    unittest.main()