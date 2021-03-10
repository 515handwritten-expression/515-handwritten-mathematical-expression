import unittest
import math
import xml.etree.ElementTree as ET
from scr.XmlTreeCalculation import IncalculableError
import scr.XmlTreeCalculation as XTC
import os.path

class TestCalculation(unittest.TestCase):
    def testCalculateXml(self):
        XTC.calculateXml(ET.parse("../data/xml/expression.xml"))
        self.assertTrue(os.path.exists("CalculationResult.txt"))
        XTC.calculateXml(ET.parse("../data/xml/expressionFull.xml"))
        self.assertTrue(os.path.exists("CalculationResult.txt"))

    def testTraceTreeCalculation(self):
        expression_result = round((12*(7-(3**2)))/6+8,10)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/expression.xml").getroot()), expression_result)
        expressionFull_result = round((math.e*(3.1415-(3**2)))/(-6)+8,10)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/expressionFull.xml").getroot()), expressionFull_result)

    def testTraceTreeSpecialConstant(self):
        constantE_Result = 1
        constantETimes_Result = round(2 * math.e,10)
        constantPi_Result = 1
        constantPiTimes_Result = round(2 * 3.1415,10)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/constantE.xml").getroot()), constantE_Result)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/constantETimes.xml").getroot()), constantETimes_Result)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/constantPi.xml").getroot()), constantPi_Result)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/constantPiTimes.xml").getroot()), constantPiTimes_Result)

    def testTraceTreePositiveNegativeSign(self):
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/negativeNumber.xml").getroot()), -8)
        self.assertEqual(XTC.traceTree(ET.parse("../data/xml/positiveNumber.xml").getroot()), 8)


    def testTraceTreeErrorLetters(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorLetter.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorLetterAlpha.xml").getroot())

    def testTraceTreeErrorOperation(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationPm.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationGeq.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationGt.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationLeq.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationLt.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/errorOperationNeq.xml").getroot())

    def testTraceTreeRaiseExceptionMissingChild(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingOneChild.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingOneChildPlus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingTwoChild.xml").getroot())

    def testTraceTreeRaiseExceptionMissingValue(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingLeftValueDiv.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingLeftValueTimes.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingRightValueDiv.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingRightValueMinus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingRightValuePlus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("../data/xml/missingRightValueTimes.xml").getroot())

    def testCalculationPlus(self):
        self.assertEqual(XTC.calculation("plus",1,2),3)
        self.assertEqual(XTC.calculation("plus",1,-2),-1)
        self.assertEqual(XTC.calculation("plus",1,-1),0)
        self.assertEqual(XTC.calculation("plus",1.5,2),3.5)
        self.assertEqual(XTC.calculation("plus",1.1,1.2),2.3)

    def testCalculationMinus(self):
        self.assertEqual(XTC.calculation("minus",1,2),-1)
        self.assertEqual(XTC.calculation("minus",2,1),1)
        self.assertEqual(XTC.calculation("minus",0,0),0)
        self.assertEqual(XTC.calculation("minus",1,-1),2)
        self.assertEqual(XTC.calculation("minus",1.1, 0.2),0.9)

    def testCalculationTimes(self):
        self.assertEqual(XTC.calculation("times",1,2),2)
        self.assertEqual(XTC.calculation("times",2,0),0)
        self.assertEqual(XTC.calculation("times",0,0),0)
        self.assertEqual(XTC.calculation("times",1,-1),-1)
        self.assertEqual(XTC.calculation("times",1.1, 0.2),0.22)

    def testCalculationDiv(self):
        self.assertEqual(XTC.calculation("div",1,2),0.5)
        self.assertEqual(XTC.calculation("div",0,2),0)

    def testCalculationDivByZero(self):
        self.assertRaises(IncalculableError, XTC.calculation, "div",2,0)
        self.assertRaises(IncalculableError, XTC.calculation, "div",0,0)

    def testCalculationPower(self):
        self.assertEqual(XTC.calculation("power",1,2),1)
        self.assertEqual(XTC.calculation("power",2,2),4)
        self.assertEqual(XTC.calculation("power",-2,2),4)
        self.assertEqual(XTC.calculation("power",2,1),2)
        self.assertEqual(XTC.calculation("power",2,0),1)


if __name__ == '__main__':
    unittest.main()
