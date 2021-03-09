import unittest
import math
import xml.etree.ElementTree as ET
from XmlTreeCalculation import IncalculableError
import XmlTreeCalculation as XTC


class TestCalculation(unittest.TestCase):
    def testTraceTreeCalculation(self):
        expression_result = round((12*(7-(3**2)))/6+8,10)
        self.assertEqual(XTC.traceTree(ET.parse("expression.xml").getroot()), expression_result)
        expressionFull_result = round((math.e*(3.1415-(3**2)))/(-6)+8,10)
        self.assertEqual(XTC.traceTree(ET.parse("expressionFull.xml").getroot()), expressionFull_result)

    def testTraceTreeSpecialConstant(self):
        constantE_Result = 1
        constantETimes_Result = round(2 * math.e,10)
        constantPi_Result = 1
        constantPiTimes_Result = round(2 * 3.1415,10)
        self.assertEqual(XTC.traceTree(ET.parse("constantE.xml").getroot()), constantE_Result)
        self.assertEqual(XTC.traceTree(ET.parse("constantETimes.xml").getroot()), constantETimes_Result)
        self.assertEqual(XTC.traceTree(ET.parse("constantPi.xml").getroot()), constantPi_Result)
        self.assertEqual(XTC.traceTree(ET.parse("constantPiTimes.xml").getroot()), constantPiTimes_Result)

    def testTraceTreePositiveNegativeSign(self):
        self.assertEqual(XTC.traceTree(ET.parse("negativeNumber.xml").getroot()), -8)
        self.assertEqual(XTC.traceTree(ET.parse("positiveNumber.xml").getroot()), 8)


    def testTraceTreeErrorLetters(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorLetter.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorLetterAlpha.xml").getroot())

    def testTraceTreeErrorOperation(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationPm.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationGeq.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationGt.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationLeq.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationLt.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("errorOperationNeq.xml").getroot())

    def testTraceTreeRaiseExceptionMissingChild(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingOneChild.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingOneChildPlus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingTwoChild.xml").getroot())

    def testTraceTreeRaiseExceptionMissingValue(self):
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingLeftValueDiv.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingLeftValueTimes.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingRightValueDiv.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingRightValueMinus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingRightValuePlus.xml").getroot())
        self.assertRaises(IncalculableError, XTC.traceTree, ET.parse("missingRightValueTimes.xml").getroot())

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
