import unittest
import xml.etree.ElementTree as ET
import scr.XmlTreeMathJaxConverter as XTMJC
import os.path

class TestCalculation(unittest.TestCase):
    def testCalculateXml(self):
        XTMJC.convertXmlMathjax(ET.parse("../data/xml/expression.xml"))
        self.assertTrue(os.path.exists("MathJaxResult.txt"))
        XTMJC.convertXmlMathjax(ET.parse("../data/xml/expressionFull.xml"))
        self.assertTrue(os.path.exists("MathJaxResult.txt"))

    def testTreeToMathJax(self):
        expressionMathJax = "{12 \\times (7 - (3^{2})) \over 6} + 8"
        self.assertEqual(XTMJC.treeToMathJax(ET.parse("../data/xml/expression.xml").getroot()), expressionMathJax)

    def testMathJaxComponent(self):
        self.assertEqual(XTMJC.mathJaxComponent("plus","1","2"), "1 + 2")
        self.assertEqual(XTMJC.mathJaxComponent("minus","1","2"), "1 - 2")
        self.assertEqual(XTMJC.mathJaxComponent("div","1","2"), "{1 \over 2}")
        self.assertEqual(XTMJC.mathJaxComponent("times","1","2"), "1 \\times 2")
        self.assertEqual(XTMJC.mathJaxComponent("geq","1","2"), "1 \geq 2")
        self.assertEqual(XTMJC.mathJaxComponent("gt","1","2"), "1 \gt 2")
        self.assertEqual(XTMJC.mathJaxComponent("leq","1","2"), "1 \leq 2")
        self.assertEqual(XTMJC.mathJaxComponent("lt","1","2"), "1 \lt 2")
        self.assertEqual(XTMJC.mathJaxComponent("neq","1","2"), "1 \\neq 2")
        self.assertEqual(XTMJC.mathJaxComponent("pm","1","2"), "1 \pm 2")
        self.assertEqual(XTMJC.mathJaxComponent("plus","e","2"), "e + 2")
        self.assertEqual(XTMJC.mathJaxComponent("plus","\pi","2"), "\pi + 2")
        self.assertEqual(XTMJC.mathJaxComponent("power","1","2"), "1^{2}")

        self.assertEqual(XTMJC.mathJaxComponent("minus","1","2 + 1"), "1 - (2 + 1)")
        self.assertEqual(XTMJC.mathJaxComponent("times","1","2 + 1"), "1 \\times (2 + 1)")
        self.assertEqual(XTMJC.mathJaxComponent("power","1 + 1","2"), "(1 + 1)^{2}")

    def testParenthesesCheck(self):
        self.assertEqual(XTMJC.parenthesesCheck("1"), "1")
        self.assertEqual(XTMJC.parenthesesCheck("1.1"), "1.1")
        self.assertEqual(XTMJC.parenthesesCheck("\pi"), "\pi")
        self.assertEqual(XTMJC.parenthesesCheck("x"), "x")
        self.assertEqual(XTMJC.parenthesesCheck("e"), "e")
        self.assertEqual(XTMJC.parenthesesCheck("1 + 1"), "(1 + 1)")
        self.assertEqual(XTMJC.parenthesesCheck("{1 \over 1}"), "({1 \over 1})")
