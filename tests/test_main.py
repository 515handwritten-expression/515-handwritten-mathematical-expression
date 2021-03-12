import unittest
import handwritten_math_expression.main as hme
from unittest.mock import patch

class TestMain(unittest.TestCase):

    @patch('handwritten_math_expression.main.predict_single_label')
    def test_file_called(self, mock_predict_single_label):
        print("test_file_called")
        mock_predict_single_label.return_value = "0"
        hme.write_labels_for_all_segs("test_1")
        # self.assertTrue(mock_newsgroup_file.called)
        self.assertEqual(mock_predict_single_label.call_count,5)

if __name__ == '__main__':
    unittest.main()