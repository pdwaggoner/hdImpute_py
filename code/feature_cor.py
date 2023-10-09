import numpy as np
import pandas as pd
import warnings

def feature_cor(data, return_cor=False):
    if not isinstance(data, (pd.DataFrame, pd.Series, pd.Series)) and not np.isscalar(data):
        raise ValueError('data must be a Pandas data frame or series\nYou have provided an object of class: {}'.format(type(data).__name__))

    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include=[np.number])

    nvar = numeric_data.shape[1] if isinstance(data, (pd.DataFrame, pd.Series)) else 1
    data_matrix = np.zeros((nvar, nvar), dtype=float)
    data_matrix = pd.DataFrame(data_matrix, index=numeric_data.columns, columns=numeric_data.columns)
    x = numeric_data.to_numpy() if isinstance(data, (pd.DataFrame, pd.Series)) else np.array([numeric_data])
    r = ~np.isnan(x)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        v = np.abs(np.corrcoef(x, rowvar=False))
        v[np.isnan(v)] = 0
        u = np.abs(np.corrcoef(x=r, rowvar=False))
        u[np.isnan(u)] = 0
    max_cor = np.maximum(v, u)

    # Create a Pandas DataFrame from max_cor
    correlation_df = pd.DataFrame(max_cor, index=numeric_data.columns, columns=numeric_data.columns)

    return correlation_df
