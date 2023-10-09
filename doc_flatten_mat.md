# `flatten_mat` Function Documentation

## Description

The `flatten_mat()` function is designed to take a correlation matrix, typically obtained from the `feature_cor` function or similar, and flatten it into a ranked list of unique columns based on the pairwise correlations between them.

## Usage

```python
import pandas as pd
from flatten_mat import flatten_mat

flattened_ranked_cor_mat = feature_cor(correlation_matrix, return_cor=False)
```

## Parameters

- `cor_mat` (pd.DataFrame): A Pandas DataFrame representing a correlation matrix. This is typically the output of the `feature_cor()` function or a similar function that computes correlations between features.

- `return_mat` (bool, optional): If set to `True`, the function will print the flattened DataFrame. Default is `False`.

## Returns

`ranked` (pd.DataFrame): A Pandas DataFrame containing unique columns from the input correlation matrix, ranked by their correlations.

## Raises

ValueError: If the input `cor_mat()` is not a Pandas DataFrame.

## Unit Tests

This function has been thoroughly tested using the following unit tests:

- *test_valid_input*: Verifies that the function works correctly with a valid Pandas DataFrame.
- *test_invalid_input*: Checks if the function raises a ValueError when provided with an invalid input.
- *test_return_mat*: Ensures that the function prints the flattened DataFrame when return_mat is set to True.
- *test_returned_df_order*: Validates that the returned DataFrame is ordered by correlation.
- *test_returned_df_columns*: Checks if the returned DataFrame has the expected columns.

## Example

Here's a simple example demonstrating usage.

```python
import pandas as pd
from feature_cor import feature_cor
from flatten_mat import flatten_mat

# Create a sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Compute the correlation matrix
correlation_matrix = feature_cor(data)

# Flatten the correlation matrix and get a feature-ranked DataFrame
ranked_columns = flatten_mat(correlation_matrix)
ranked_columns
```