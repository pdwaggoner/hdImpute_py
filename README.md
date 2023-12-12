# `hdImpute` in Python
*A python implementation of the batch-based `hdImpute` algorithm for high dimensional missing data problems.* 

This is built in the same spirit as the more mature [version in R](https://github.com/pdwaggoner/hdImpute) based on the [recent paper](https://link.springer.com/article/10.1007/s00180-023-01325-9) introducing the hdImpute method for addressing high dimensional missing data problems. There are a few important distinctions, at least in the present version, listed below.

**Note**: This module is a work in progress. At present, the software includes the "individual" approach to the algorithm, proceeding in 3 stages: 

  1. Build the cross-feature correlation matrix ([`feature_cor`](https://github.com/pdwaggoner/hdImpute_py/blob/main/code/feature_cor.py))
  2. Flatten the matrix and rank features based on absolute correlations ([`flatten_mat`](https://github.com/pdwaggoner/hdImpute_py/blob/main/code/flatten_mat.py))
  3. Impute batches of features based on correlation structure, of sizes determined by the user ([`impute_batches`](https://github.com/pdwaggoner/hdImpute_py/blob/main/code/impute_batches.py))

The current approach differs from the R approach in the following ways (though continued development will address these and other issues in time):

  - Only numeric features are supported. The algorithm will skip over any non-numeric features (e.g., strings, dates, times, etc.). These columns are appended after the final stage to return a data matrix of the same dimensions as the input data frame.
  - Instead of chained random forests, a similar algorithm in the same spirit from `fancyimpute` is used. Namely, the imputation engine under the hood is `IterativeImputer`, which is now mainly supported in `scikit-learn` but also still in `fancyimpute`. `IterativeImputer` is "a strategy for imputing missing values by modeling each feature with missing values as a function of other features in a round-robin fashion (read more [here](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html) or [here](https://pypi.org/project/fancyimpute/))."
  - As noted above, instead of a single function option as in [hdImpute in R](https://github.com/pdwaggoner/hdImpute), users must proceed in sequence across the three stages: 1. build the corr matrix, 2. flatten and rank features, and 3. impute batches and join.

## Usage

See the [code](https://github.com/pdwaggoner/hdImpute_py/tree/main/code), [docs](https://github.com/pdwaggoner/hdImpute_py/tree/main/docs), and [tests](https://github.com/pdwaggoner/hdImpute_py/tree/main/unit%20tests) for more detail on the functions and process. But a simple demonstration of usage with some synthetic data might look something like this:

Define the data (with a few missing values).

```python
import pandas as pd

data = pd.DataFrame({
    'Feature1': [1.0, 2.0, np.nan, 4.0, 5.0],
    'Feature2': [np.nan, 2.0, 3.0, np.nan, 5.0],
    'Feature3': [1.0, 2.0, 7.0, 4.0, 5.0],
    'Feature4': [1.0, np.nan, 10.0, 4.0, 5.0],
    'Feature5': ["a", "b", "c", "d", "e"]
})
```

Build the cross-feature correlation matrix.

```python
cor_out = feature_cor(data, return_cor=True) # (optional) returning to inspect
```

Flatten the matrix and rank features based on absolute correlations.

```python
flat_out = flatten_mat(cor_out)
```

Impute batches of features based on correlation structure.

```python
# either store and inspect obj
imputed_data = impute_batches(data, flat_out, batch=2, decimal_places=2)
imputed_data

# or run directly to print output
impute_batches(data, flat_out, batch=2, decimal_places=2)
```

*Importantly*, users should always remember to closely inspect the data output to ensure missingness is not only dealt with (completed cases), but done so in a reliable and reasonable way. For more on checking the quality of imputations, take a look at the [`mad()` function](https://github.com/pdwaggoner/hdImpute/blob/main/vignettes/MAD-Evaluation.md) in the R version. Development of a similar function for this python module is forthcoming. 

## Contribute

As mentioned, this py version of `hdImpute` is very much under active development. Contributions in any form are appreciated. For example:

  - [Pulls](https://github.com/pdwaggoner/hdImpute_py/pulls) (direct contributions)
  - [Issues](https://github.com/pdwaggoner/hdImpute_py/issues) (suggestions, bugs, etc.)
  - [Reach out](https://pdwaggoner.github.io/) (for anything else)

Thanks!
