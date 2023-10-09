import unittest
import pandas as pd
import numpy as np
from impute_batches import impute_batches

class TestImputeBatches(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame with missing values for testing
        self.data = pd.DataFrame({
            'A': [1, 2, np.nan, 4, 5],
            'B': [np.nan, 2, 3, 4, 5],
            'C': [1, 2, 3, 4, 5]
        })

        self.features = pd.DataFrame({
            'col': ['A', 'B', 'C']
        })

    def test_impute_batches_with_seed(self):
        # Test impute_batches with a specified seed
        imputed_data = impute_batches(self.data, self.features, batch=2, seed=42)
        self.assertTrue(np.all(~imputed_data.isnull().any()))  # Check if there are no missing values

    def test_impute_batches_no_seed(self):
        # Test impute_batches without specifying a seed
        imputed_data = impute_batches(self.data, self.features, batch=2)
        self.assertTrue(np.all(~imputed_data.isnull().any()))  # Check if there are no missing values

    def test_impute_batches_no_missing_values(self):
        # Test impute_batches with data that has no missing values
        complete_data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [6, 7, 8, 9, 10],
            'C': [11, 12, 13, 14, 15]
        })
        imputed_data = impute_batches(complete_data, self.features, batch=2)
        self.assertTrue(imputed_data.equals(complete_data))  # Check if output is the same as input

    def test_impute_batches_rounding(self):
        # Test impute_batches with custom decimal_places parameter
        imputed_data = impute_batches(self.data, self.features, batch=2, decimal_places=2)
        self.assertTrue(np.all(~imputed_data.isnull().any()))  # Check if there are no missing values
        self.assertEqual(imputed_data['A'][2], 2.33)  # Check if the rounding is applied

if __name__ == '__main__':
    unittest.main()