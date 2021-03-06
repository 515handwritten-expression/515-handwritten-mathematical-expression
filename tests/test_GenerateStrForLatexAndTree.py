import unittest
import handwritten_math_expression.generateStrForLatexAndTree as gs
from unittest.mock import patch

class TestGenerateStrForLatexAndTree(unittest.TestCase):

    def testverifyRecRelationship_1(self):
        rec1 = [204, 90, 265, 186]
        rec2 = [307, 46, 350, 91]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'power')

    def testverifyRecRelationship_2(self):
        rec1 = [351, 24, 406, 182]
        rec2 = [29, 204, 452, 237]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'up')

    def testverifyRecRelationship_3(self):
        rec1 = [71, 83, 183, 184]
        rec2 = [204, 90, 265, 186]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'parallel')

    def testconvertLabelIntoExpressionStr_1(self):
        label = ['pi', 'r', '2', 'h', '-', '3']
        position = [[71, 83, 183, 184], [204, 90, 265, 186], [307, 46, 350, 91], [351, 24, 406, 182],
                    [29, 204, 452, 237], [136, 282, 216, 365]]
        str1 = gs.convertLabelIntoExpressionStr(label, position)
        self.assertEqual(str1, '(pir^2h)/(3)')

    def testconvertLabelIntoExpressionStr_2(self):
        label = ['a', 'b', 'c', 'd']
        position = [[30, 191, 160, 359], [202, 69, 272, 229], [306, 106, 371, 156], [414, 24, 486, 131]]
        str1 = gs.convertLabelIntoExpressionStr(label, position)
        self.assertEqual(str1, 'abcd')

    def testremoveNegativeSymbol_1(self):
        str1 = '12+3-(-4)+7'
        str2 = gs.removeNegativeSymbol(str1)
        self.assertEqual(str2, '12+3-(0-4)+7')

    def testremoveNegativeSymbol_2(self):
        str1 = '-1*(-4)'
        str2 = gs.removeNegativeSymbol(str1)
        self.assertEqual(str2, '0-1*(0-4)')

    def testremoveNegativeSymbol_3(self):
        str1 = '-1'
        str2 = gs.removeNegativeSymbol(str1)
        self.assertEqual(str2, '0-1')

    def testgetStringsForLatexAndTree_1(self):
        label = ['pi', 'r', '2', 'h', '-', '3']
        position = [[71, 83, 183, 184], [204, 90, 265, 186], [307, 46, 350, 91], [351, 24, 406, 182],
                    [29, 204, 452, 237], [136, 282, 216, 365]]
        str1, str2 = gs.getStringsForLatexAndTree(label, position)
        self.assertEqual(str1, '(pir^2h)/(3)')
        self.assertEqual(str2, '(pir^2h)/(3)')

    def testgetStringsForLatexAndTree_2(self):
        label = ['-', '6']
        position = [[30, 101, 198, 115], [283, 17, 486, 231]]
        str1, str2 = gs.getStringsForLatexAndTree(label, position)
        self.assertEqual(str1, '-6')
        self.assertEqual(str2, '0-6')

    def testgetStringsForLatexAndTree_3(self):
        label = ['1']
        position = [[30, 101, 198, 115]]
        str1, str2 = gs.getStringsForLatexAndTree(label, position)
        self.assertEqual(str1, '1')
        self.assertEqual(str2, '1')

    @patch('handwritten_math_expression.generateStrForLatexAndTree.convertLabelIntoExpressionStr')
    def testGetStringsForLatexAndTree_m1(self, mock_convertLabelIntoExpressionStr):
        label = ['6']
        position = [[283, 17, 486, 231]]
        mock_convertLabelIntoExpressionStr.return_value = "6"
        str1, str2 = gs.getStringsForLatexAndTree(label,position)
        self.assertFalse(mock_convertLabelIntoExpressionStr.called)
        self.assertEqual(str1, '6')
        self.assertEqual(str2, '6')

    @patch('handwritten_math_expression.generateStrForLatexAndTree.convertLabelIntoExpressionStr')
    def testGetStringsForLatexAndTree_m2(self, mock_convertLabelIntoExpressionStr):
        label = ['-', '6']
        position = [[30, 101, 198, 115], [283, 17, 486, 231]]
        mock_convertLabelIntoExpressionStr.return_value = "-6"
        str1, str2 = gs.getStringsForLatexAndTree(label,position)
        self.assertTrue(mock_convertLabelIntoExpressionStr.called)
        self.assertEqual(str1, '-6')
        self.assertEqual(str2, '0-6')
        
    @patch('handwritten_math_expression.generateStrForLatexAndTree.verifyRecRelationship')
    def testConvertLabelIntoExpressionStr_m1(self, mock_verifyRecRelationship):
        label = ['a', '2']
        position = [[29, 204, 452, 237], [136, 282, 216, 365]]
        mock_verifyRecRelationship.return_value = ("power")
        str = gs.convertLabelIntoExpressionStr(label,position)
        self.assertTrue(mock_verifyRecRelationship.called)
        self.assertEqual(str, "a^2")
        self.assertEqual(mock_verifyRecRelationship.call_count,1)

    @patch('handwritten_math_expression.generateStrForLatexAndTree.verifyRecRelationship')
    def testConvertLabelIntoExpressionStr_m2(self, mock_verifyRecRelationship):
        label = ['pi', '-', '3']
        position = [[71, 83, 183, 184], [29, 204, 452, 237], [136, 282, 216, 365]]
        mock_verifyRecRelationship.return_value = ("up")
        str = gs.convertLabelIntoExpressionStr(label,position)
        self.assertTrue(mock_verifyRecRelationship.called)
        self.assertEqual(str, "(pi)/(3)")

    @patch('handwritten_math_expression.generateStrForLatexAndTree.verifyRecRelationship')
    def testConvertLabelIntoExpressionStr_m3(self, mock_verifyRecRelationship):
        label = ['a', 'b', 'c']
        position = [[29, 204, 452, 237], [136, 282, 216, 365], [0,0,0,0]]
        mock_verifyRecRelationship.return_value = ("parallel")
        str = gs.convertLabelIntoExpressionStr(label,position)
        self.assertEqual(str, "abc")
        self.assertEqual(mock_verifyRecRelationship.call_count,2)

    @patch('handwritten_math_expression.generateStrForLatexAndTree.verifyRecRelationship')
    def testConvertLabelIntoExpressionStr_m4(self, mock_verifyRecRelationship):
        label = ['a', 'times', 'c']
        position = [[29, 204, 452, 237], [136, 282, 216, 365], [0,0,0,0]]
        mock_verifyRecRelationship.return_value = ("parallel")
        str = gs.convertLabelIntoExpressionStr(label,position)
        self.assertEqual(str, "a*c")
        self.assertEqual(mock_verifyRecRelationship.call_count,2)

if __name__ == '__main__':
    unittest.main()