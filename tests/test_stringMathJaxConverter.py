import unittest
from unittest.mock import patch
from os import path

import handwritten_math_expression.stringMathJaxConverter as MJAX
import os.path

class TestMathJax(unittest.TestCase):

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
"""
    @patch('handwritten_math_expression.stringMathJaxConverter.stringToMathJax')
    def testConvertMathjax(self, mock_stringToMathJax):
        path = './tests/results'
        path = os.path.realpath(path)
        MJAX.convertMathjax("",path)
        mock_stringToMathJax.return_value = ""
        self.assertTrue(mock_stringToMathJax.called)
        self.assertTrue(path.exists('results/MathJaxResult.txt'))
"""
if __name__ == '__main__':
    unittest.main()