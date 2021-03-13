import unittest
import handwritten_math_expression.generateStrForLatexAndTree as gs


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

if __name__ == '__main__':
    unittest.main()