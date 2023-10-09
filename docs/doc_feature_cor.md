# `feature_cor` Function Documentation

## Description
The `feature_cor()` function calculates the correlation matrix of numeric features within a Pandas DataFrame or Series. It computes the correlation between all numeric columns, filtering out non-numeric columns. The function provides an option to return the correlation matrix and handles various input types gracefully.

## Usage
```python
from feature_cor import feature_cor

correlation_matrix = feature_cor(data, return_cor=False)
```

## Parameters

- `data` (Pandas DataFrame, Series, or scalar): The input data to compute the correlation matrix for. Must be numeric data.

- `return_cor` (bool, optional): If True, the function returns the correlation matrix. If False (default), it returns a Pandas DataFrame containing the maximum absolute correlation values between numeric features.

## Returns
`correlation_matrix` (Pandas DataFrame): If `return_cor=True`, the function returns a Pandas DataFrame containing the correlation matrix of numeric features. If `return_cor=False`, it returns a DataFrame of maximum absolute correlation values between numeric features.

## Exceptions

ValueError: Raised if the `data` parameter is not a Pandas DataFrame, Series, or scalar.

## Unit Tests

Unit tests for the `feature_cor()` function are available in `test_feature_cor.py`. These tests cover various scenarios, including valid inputs, non-numeric column filtering, invalid input types, and checking the return value when return_cor is set to True. Refer to the unit tests for detailed examples.

## Example

Here's a simple example demonstrating usage.

```python
import pandas as pd
import numpy as np
from feature_cor import feature_cor

# Create a sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Compute and return the correlation matrix
correlation_matrix = feature_cor(data)

correlation_matrix
```