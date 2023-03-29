# imports
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


### SCALING FUNCTIONS
def min_max_scaler(X_train, 
                    col_list,
                    X_validate = None,
                    X_test = None
                   ):
    '''
    Arguments: 
        Required: X_train dataframe, list of columns to be scaled (should be continuous data)
        Optional: X_validate dataframe, X_test dataframe
    Actions:
        1. Create df to be scaled from X_train
        2. Initialize the scaler
        3. Fit the scaler to train only
        4. Create a dataframe with the scaled train data
        5. If DataFrames are used in keyword arguments:
            a. Create a dataframe to be scaled from X_validate or X_test
            b. Create a dataframe with the scaled validate or test data
    Returns: scaled dataframe
    Modules: 
        1. from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler, QuantileTransformer
        2. import pandas as pd
    '''
    
    # Create a dataframe with only the columns that need to be scaled
    X_train_to_scale = X_train[col_list]
    
    # initiailize the scaler
    scaler = MinMaxScaler()
    
    # fit the scaled to the dataframe
    scaler.fit(X_train_to_scale)

    # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
    X_train_scaled = pd.DataFrame(scaler.transform(X_train_to_scale), index=X_train_to_scale.index, columns=X_train_to_scale.columns)
    
    ## OPTIONALS
    # if X_validate and X_test are pandas dataframes
    if isinstance(X_validate, pd.DataFrame) and isinstance(X_test, pd.DataFrame):
        
        # Create a dataframe with only the columns that need to be scaled
        X_validate_to_scale = X_validate[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_validate_scaled = pd.DataFrame(scaler.transform(X_validate_to_scale), index=X_validate_to_scale.index, columns=X_validate_to_scale.columns)

        # Create a dataframe with only the columns that need to be scaled
        X_test_to_scale = X_test[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_test_scaled = pd.DataFrame(scaler.transform(X_test_to_scale), index=X_test_to_scale.index, columns=X_test_to_scale.columns)
        
        # Exit the funciton and return the scaled train data and the scaled test data
        return X_train_scaled, X_validate_scaled, X_test_scaled
    
    # with no keyword arguments(optional), the function will exist wiuth only the scaled train data
    return X_train_scaled


def robust_scaler(X_train, 
                    col_list,
                    X_validate = None,
                    X_test = None
                   ):
    '''
    Arguments: 
        Required: X_train dataframe, list of columns to be scaled (should be continuous data)
        Optional: X_validate dataframe, X_test dataframe
    Actions:
        1. Create df to be scaled from X_train
        2. Initialize the scaler
        3. Fit the scaler to train only
        4. Create a dataframe with the scaled train data
        5. If DataFrames are used in keyword arguments:
            a. Create a dataframe to be scaled from X_validate or X_test
            b. Create a dataframe with the scaled validate or test data
    Returns: scaled dataframe
    Modules: 
        1. from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler, QuantileTransformer
        2. import pandas as pd
    '''
    
    # Create a dataframe with only the columns that need to be scaled
    X_train_to_scale = X_train[col_list]
    
    # initiailize the scaler
    scaler = RobustScaler()
    
    # fit the scaled to the dataframe
    scaler.fit(X_train_to_scale)

    # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
    X_train_scaled = pd.DataFrame(scaler.transform(X_train_to_scale), index=X_train_to_scale.index, columns=X_train_to_scale.columns)
    
    # OPTIONALS
    # if X_validate and X_test are pandas dataframes
    if isinstance(X_validate, pd.DataFrame) and isinstance(X_test, pd.DataFrame):
        
        # Create a dataframe with only the columns that need to be scaled
        X_validate_to_scale = X_validate[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_validate_scaled = pd.DataFrame(scaler.transform(X_validate_to_scale), index=X_validate_to_scale.index, columns=X_validate_to_scale.columns)

        # Create a dataframe with only the columns that need to be scaled
        X_test_to_scale = X_test[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_test_scaled = pd.DataFrame(scaler.transform(X_test_to_scale), index=X_test_to_scale.index, columns=X_test_to_scale.columns)
        
        # Exit the funciton and return the scaled train data and the scaled test data
        return X_train_scaled, X_validate_scaled, X_test_scaled
    
    # with no keyword arguments(optional), the function will exist wiuth only the scaled train data
    return X_train_scaled


def standard_scaler(X_train, 
                    col_list,
                    X_validate = None,
                    X_test = None
                   ):
    '''
    Arguments: 
        Required: X_train dataframe, list of columns to be scaled (should be continuous data)
        Optional: X_validate dataframe, X_test dataframe
    Actions:
        1. Create df to be scaled from X_train
        2. Initialize the scaler
        3. Fit the scaler to train only
        4. Create a dataframe with the scaled train data
        5. If DataFrames are used in keyword arguments:
            a. Create a dataframe to be scaled from X_validate or X_test
            b. Create a dataframe with the scaled validate or test data
    Returns: scaled dataframe
    Modules: 
        1. from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler, QuantileTransformer
        2. import pandas as pd
    '''
    
    # Create a dataframe with only the columns that need to be scaled
    X_train_to_scale = X_train[col_list]
    
    # initiailize the scaler
    scaler = StandardScaler()
    
    # fit the scaled to the dataframe
    scaler.fit(X_train_to_scale)

    # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
    X_train_scaled = pd.DataFrame(scaler.transform(X_train_to_scale), index=X_train_to_scale.index, columns=X_train_to_scale.columns)
    
    # OPTIONALS
    # if X_validate and X_test are pandas dataframes
    if isinstance(X_validate, pd.DataFrame) and isinstance(X_test, pd.DataFrame):
        
        # Create a dataframe with only the columns that need to be scaled
        X_validate_to_scale = X_validate[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_validate_scaled = pd.DataFrame(scaler.transform(X_validate_to_scale), index=X_validate_to_scale.index, columns=X_validate_to_scale.columns)

        # Create a dataframe with only the columns that need to be scaled
        X_test_to_scale = X_test[col_list]
        
        # scale the data and make the array a dataframe with the same columns and same index as the original and assign it to a variable
        X_test_scaled = pd.DataFrame(scaler.transform(X_test_to_scale), index=X_test_to_scale.index, columns=X_test_to_scale.columns)
        
        # Exit the funciton and return the scaled train data and the scaled test data
        return X_train_scaled, X_validate_scaled, X_test_scaled
    
    # with no keyword arguments(optional), the function will exist wiuth only the scaled train data
    return X_train_scaled



def scale_data(X_train, col_list, scaler, X_validate = None, X_test = None):
    '''
    Argumments:
        Required: X_train dataframe, list of columns to be scaled (should be continuous data), type of scaler ('standard', 'robust', 'minmax')
        Optional: X_validate dataframe, X_test dataframe
    Actions: Calls functions for specific scaler specified in the arguments
    Returns: scaled dataframe
    Modules:
        1. from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler, QuantileTransformer
        2. import numpy as np
        3. import pandas as pd       
    '''
    
    # when scaler is string literal 'standard'
    if scaler == 'standard':
        
        # call standard scaler function with arguments from main function specified
        return standard_scaler(X_train, col_list, X_validate=X_validate, X_test=X_test)
    
    # when scaler is string literal 'robust'
    elif scaler == 'robust':
        
        # call robust scaler function with arguments from main function specified
        return robust_scaler(X_train, col_list, X_validate=X_validate, X_test=X_test)
    
    # when scaler is string literal 'minmax'
    elif scaler == 'minmax':
        
        # call min max scaler function with arguments from main function specified
        return min_max_scaler(X_train, col_list, X_validate=X_validate, X_test=X_test)
    
    # when scaler is anything else
    else:
        
        # prompt user to try again
        return print('Please specify the scaler from this list [\'standard\', \'robust\', \'minmax\']')
