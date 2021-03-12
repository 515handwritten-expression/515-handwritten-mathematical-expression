import unittest
import scr.generateStrForLatexAndTree as gs


class TestGenerateStrForLatexAndTree(unittest.TestCase):

    def testverifyRecRelationship_1(self):
        rec1 = [204, 90, 265, 186] 
        rec2 = [307, 46, 350, 91]
        relationship = gs.verifyRecRelationship(rec1,rec2)
        self.assertEqual(relationship,'power')

    def testverifyRecRelationship_2(self):
        rec1 = [351, 24, 406, 182] 
        rec2 = [29, 204, 452, 237]
        relationship = gs.verifyRecRelationship(rec1,rec2)
        self.assertEqual(relationship,'up')

    def testverifyRecRelationship_3(self):
        rec1 = [71, 83, 183, 184]
        rec2 = [204, 90, 265, 186]
        relationship = gs.verifyRecRelationship(rec1,rec2)
        self.assertEqual(relationship,'parallel')

    def testconvertLabelIntoExpressionStr_1(self):
        label = ['pi','r','2','h','-','3']
        position = [[71, 83, 183, 184], [204, 90, 265, 186] , [307, 46, 350, 91] ,[351, 24, 406, 182] ,[29, 204, 452, 237] ,[136, 282, 216, 365]]
        str1 = gs.convertLabelIntoExpressionStr(label,position)
        self.assertEqual(str1, '(pir^2h)/(3)')

    def testconvertLabelIntoExpressionStr_2(self):  
        label = ['a','b','c','d']
        position = [[30, 191, 160, 359], [202, 69, 272, 229] ,[306, 106, 371, 156] ,[414, 24, 486, 131]]
        str1 = gs.convertLabelIntoExpressionStr(label,position)
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
        label = ['pi','r','2','h','-','3']
        position = [[71, 83, 183, 184], [204, 90, 265, 186] , [307, 46, 350, 91] ,[351, 24, 406, 182] ,[29, 204, 452, 237] ,[136, 282, 216, 365]]
        str1,str2 = gs.getStringsForLatexAndTree(label,position)
        self.assertEqual(str1, '(pir^2h)/(3)')
        self.assertEqual(str2, '(pir^2h)/(3)')

    def testgetStringsForLatexAndTree_2(self):
        label = ['-','6']
        position = [[30, 101, 198, 115],[283, 17, 486, 231]]
        str1,str2 = gs.getStringsForLatexAndTree(label,position)
        self.assertEqual(str1, '-6')
        self.assertEqual(str2, '0-6')