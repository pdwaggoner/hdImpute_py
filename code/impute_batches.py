import pandas as pd
import numpy as np
import time
from fancyimpute import IterativeImputer

def impute_batches(data, features, batch, seed=None, decimal_places=1):
    if seed is not None:
        np.random.seed(seed)

    if not isinstance(data, pd.DataFrame):
        raise ValueError('data must be a Pandas data frame')

    if not data.isnull().any().any():
        print("Warning: The input data is complete with no missing values. Returning the original data.")
        return data
    
    # Step 1
    features['batch'] = (features.index // batch) + 1
    splits = features.groupby('batch')

    # Step 2
    imputed_dataframes = []

    start_time = time.time()
    
    for _, split in splits:
        # Extract column names from 'col' column
        col_names = split['col'].tolist()
        # Filter columns in the data
        batch_data = data[col_names]

        if not batch_data.empty:
            # Skip non-numeric columns and only impute numeric columns
            numeric_columns = batch_data.select_dtypes(include=[np.number])
            
            if not numeric_columns.empty:
                imputer = IterativeImputer(random_state=seed)
                imputed_data = imputer.fit_transform(numeric_columns)
                imputed_numeric = pd.DataFrame(imputed_data, columns=numeric_columns.columns)
            else:
                imputed_numeric = pd.DataFrame()

            # Reconstruct the batch_data with imputed numeric columns
            imputed_batch_data = pd.concat([imputed_numeric, batch_data.select_dtypes(exclude=[np.number])], axis=1)
        else:
            imputed_batch_data = pd.DataFrame(columns=batch_data.columns)

        imputed_dataframes.append(imputed_batch_data)

    # Concatenate DataFrames for all batches
    imputed = pd.concat(imputed_dataframes, axis=1)
    
    # Add any missing columns from the original data
    missing_columns = set(data.columns) - set(imputed.columns)
    for column in missing_columns:
        imputed[column] = data[column]

    elapsed_time = time.time() - start_time
    print("Imputed and joined in {:.2f} seconds".format(elapsed_time))

    if decimal_places is not None:
        # Round columns that have decimal places
        imputed = imputed.round(decimal_places)
    else:
        # Detect the current number of decimal places and round accordingly
        imputed = imputed.round(imputed.applymap(lambda x: len(str(x).split('.')[1])).max(), skipna=True)
        
    return imputed