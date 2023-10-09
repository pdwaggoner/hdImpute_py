# `impute_batches` Function Documentation

## Description

The `impute_batches()` function is designed to impute missing values in a given Pandas DataFrame in a batch-wise manner using the Iterative Imputer from the `fancyimpute` library. This is in the same spirit, though still distinct from, a chained equations set up (as implemented in the R version of `hdImpute`). The function splits the input data into batches based on user-specified batch size, imputes missing values for each batch, and then combines the imputed batches to produce a complete DataFrame.

At present, the function only works with numeric data. If there are non-numeric columns in the DataFrame (e.g., strings, dates/times), `impute_batches()` simply skips those in the imputation process, but returns them with the full, imputed DataFrame.

## Usage

```python
import pandas as pd
from impute_batches import impute_batches

impute_batches(data, features=flattened_ranked_cor_mat, batch=2, seed=None, decimal_places=1)
```

## Parameters

- `data` (Pandas DataFrame): The input data with missing values to be imputed.

- `features` (Pandas DataFrame): The features used for imputation. This DataFrame should be generated using the `flatten_mat()` function/module, which is responsible for extracting relevant features from the data.

- `batch` (int): The batch size for splitting the data. The data will be divided into batches of this size for imputation.

- `seed` (int, optional): The seed for randomization. If provided, it ensures reproducibility of the imputation process. Default is `None`.

- `decimal_places` (int, optional): The number of decimal places to round the imputed values. Default is 1. If set to `None`, the function will detect the current number of decimal places and round accordingly.

## Returns

`imputed` (Pandas DataFrame): The DataFrame with missing values imputed. It has the same structure as the input data.

*Note*: the time taken to create batches, impute, and join is returned as well. 

## Behavior

If the input data (data) contains no missing values, the function will return the original data without any imputation.

The input data should be a Pandas DataFrame. If it is not, a ValueError will be raised.

The function rounds imputed values to the specified number of decimal places (or auto-detects the decimal places if None is provided).

## Unit Tests

Unit tests for the `impute_batches()` function have been provided to ensure its correctness and functionality. 

These tests cover various scenarios, including data with and without missing values, different rounding options, and seed-based reproducibility. Refer to these tests in the unit test script to validate the behavior of the function in your specific environment.

## Examples

Example 1: Basic Usage

```python
import pandas as pd
from feature_cor import feature_cor
from flatten_mat import flatten_mat
from impute_batches import impute_batches

# Create a sample DataFrame
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# step 1: Compute the correlation matrix
correlation_matrix = feature_cor(data)

# step 2: Flatten the correlation matrix and get a feature-ranked DataFrame
ranked_columns = flatten_mat(correlation_matrix)

# step 3: Impute missing values in batches of size 2
imputed_data = impute_batches(data, features=ranked_columns, batch=2)
```

Example 2: Adjusting Column Rounding (for DF output)

```python
imputed_data = impute_batches(data, features=ranked_columns, batch=2, decimal_places=2)
```

Here, all numeric columns in the returned DataFrame will be rounded to 2 decimal places. 