# imports
from wrangle import wrangle_zillow
from preprocess import scale_data

def scale_zillow():
    '''
    Arguments: none
    Actions: Scales all non-object and non-target features with MinMaxScaler
    Returns: train, validate, and test datasets all scaled
    Modules:
        1. from wrangle import wrangle_zillow
        2. from preprocess import scale_data
    '''
    # get data
    train, validate, test = wrangle_zillow()
    
    # assign target
    target = 'tax_amount'
    
    # get list of columns to scale
    scale_cols = [col for col in train if train[col].dtype != 'O' and col != target]
    
    # exit function and return scaled data
    return scale_data(train, scale_cols, scaler='minmax', X_validate=validate, X_test=test)
