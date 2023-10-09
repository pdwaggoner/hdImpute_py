import unittest
import pandas as pd
import numpy as np
from feature_cor import feature_cor

class TestFeatureCor(unittest.TestCase):

    def test_valid_dataframe_input(self):
        # Test with a valid Pandas DataFrame input
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = feature_cor(data)
        self.assertIsInstance(result, pd.DataFrame)

    def test_valid_series_input(self):
        # Test with a valid Pandas Series input
        data = pd.Series([1, 2, 3, 4])
        result = feature_cor(data)
        self.assertIsInstance(result, pd.DataFrame)

    def test_valid_scalar_input(self):
        # Test with a valid scalar input
        data = 42
        result = feature_cor(data)
        self.assertIsInstance(result, pd.DataFrame)

    def test_non_numeric_columns_filtered(self):
        # Test if non-numeric columns are filtered out
        data = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})
        result = feature_cor(data)
        self.assertEqual(result.shape, (1, 1))  # Only one numeric column should remain

    def test_invalid_input_type(self):
        # Test with an invalid input type
        with self.assertRaises(ValueError):
            data = "invalid_data"
            feature_cor(data)

    def test_return_correlation_matrix(self):
        # Test if return_cor=True returns a correlation matrix
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        result = feature_cor(data, return_cor=True)
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
