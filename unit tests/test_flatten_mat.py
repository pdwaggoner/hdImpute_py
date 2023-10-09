import unittest
import pandas as pd
import numpy as np
from flatten_mat import flatten_mat

class TestFlattenMat(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {
            'A': [1.0, 0.5, 0.2],
            'B': [0.5, 1.0, -0.3],
            'C': [0.2, -0.3, 1.0]
        }
        self.cor_mat = pd.DataFrame(data) # placeholder correlation matrix from feature_cor()

    def test_valid_input(self):
        # Test with a valid Pandas DataFrame
        result = flatten_mat(self.cor_mat)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(result.shape[0], 3)  # Check the number of rows

    def test_invalid_input(self):
        # Test with an invalid input (non-Pandas DataFrame)
        with self.assertRaises(ValueError):
            flatten_mat("invalid_input")

    def test_return_mat(self):
        # Test with return_mat=True
        result = flatten_mat(self.cor_mat, return_mat=True)
        self.assertIsNone(result)  # Since return_mat=True, it should print and return None

    def test_returned_df_order(self):
        # Test whether the returned DataFrame is ordered by correlation
        result = flatten_mat(self.cor_mat)
        expected_order = [1.0, 1.0, 0.5, 0.5, 0.2, -0.3]
        self.assertEqual(list(result['cor']), expected_order)

    def test_returned_df_columns(self):
        # Test whether the returned DataFrame has the expected columns
        result = flatten_mat(self.cor_mat)
        expected_columns = ['col']
        self.assertListEqual(list(result.columns), expected_columns)

if __name__ == '__main__':
    unittest.main()
