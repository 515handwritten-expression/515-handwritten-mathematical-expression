import unittest
import handwritten_math_expression.generateStrForLatexAndTree as gs
from unittest.mock import patch

class TestGenerateStrForLatexAndTree(unittest.TestCase):

    def testVerifyRecRelationship_1(self):
        rec1 = [204, 90, 265, 186]
        rec2 = [307, 46, 350, 91]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'power')

    def testVerifyRecRelationship_2(self):
        rec1 = [351, 24, 406, 182]
        rec2 = [29, 204, 452, 237]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'up')

    def testVerifyRecRelationship_3(self):
        rec1 = [71, 83, 183, 184]
        rec2 = [204, 90, 265, 186]
        relationship = gs.verifyRecRelationship(rec1, rec2)
        self.assertEqual(relationship, 'parallel')

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

    @patch('handwritten_math_expression.generateStrForLatexAndTree.verifyRecRelationship')
    def testConvertLabelIntoExpressionStr_1(self, mock_verifyRecRelationship):
        print("test_file_called")
        label = ['2', '3']
        position = [[29, 204, 452, 237], [136, 282, 216, 365]]
        mock_verifyRecRelationship.return_value = ("parallel")
        gs.convertLabelIntoExpressionStr(label,position)
        # self.assertTrue(mock_verifyRecRelationship.called)
        self.assertEqual(mock_verifyRecRelationship.call_count,1)


if __name__ == '__main__':
    unittest.main()