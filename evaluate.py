# imports
import pandas as pd
from sklearn.metrics import mean_squared_error 
import matplotlib.pyplot as plt


def plot_residuals(train, y='', yhat=''):
    '''
    Arguments: 
        1. train dataset
        2. y: the column name for the actual outcomes
        3. yhat: the column name for the predicted outcomes
    Actions:
        1. Creates a columns in the train dataset to hold the residuals
        2. Plots the residuals with labels
    Modules:
        1. import pandas as pd
        2. import matplotlib.pyplot as plt
    '''
    # adding a residuals column to train
    train['yhat_residuals'] = train[y] - train[yhat]

    # plotting yhat residuals
    plt.scatter(train[yhat], train.yhat_residuals)
    plt.axhline(train[y].mean(), c='red')
    
    # labeling the axes
    plt.xlabel('x=yhat')
    plt.ylabel('y=yhat_residuals')
    # labeling the chart
    plt.title('Linear Regression Model Residuals')
    plt.show()
    
    return

def regression_errors(train, y, yhat):
    '''
    Arguments: 
        1. train dataset
        2. y: the column name that holds the actual outcomes
        3. yhat: the column name that holds the predicted outcomes
    Actions:
        1. Computes the SSE, ESS, TSS, MSE, and RMSE for a model
    Returns:
        1. Display of SSE, ESS, TSS, MSE, and RMSE
        2. Returns RMSE
    Modules:
        1. import pandas as pd
        2. from sklearn.metrics import mean_squared_error
    '''
    # calculate the sum of squared errors
    SSE = mean_squared_error(train[y], train[yhat]) * len(train)
    
    # calculate the explained sum of squared error
    ESS = ((train[yhat] - train[y].mean())**2).sum()
    
    # calculate the total sum of squared error
    TSS = ((train[y] - train[y].mean())**2).sum()
    
    # calculate the meas squared error
    MSE = mean_squared_error(train[y], train[yhat])
    
    # calculate the root mean sqaured error
    RMSE = mean_squared_error(train[y], train[yhat], squared=False)
    
    print(f'''Model Metrics
    SSE = {SSE}
    ESS = {ESS}
    TSS = {TSS}
    MSE = {MSE}
    RMSE = {RMSE}
    ''')
    
    # exit function and return RMSE
    return RMSE

def baseline_mean_errors(train, y=''):
    '''
    Arguments: 
        1. train dataset
        2. y: the column name that holds the actual outcomes
    Actions:
        1. Creates a column in the train dataset to hold the baseline dataset
        2. Computes the SSE, MSE, and RMSE for the baseline model
    Returns:
        1. Displays the SSE, MSE, and RMSE for the baseline model
        2. Returns RMSE
    Modules:
        1. import pandas as pd
        2. from sklearn.metrics import mean_squared_error
    '''
    train['baseline'] = train[y].mean()
    
    # calculate the baseline sum of squared errors
    baseline_SSE = mean_squared_error(train[y], train['baseline']) * len(train)
    
    # calculate the baseline mean of squared error
    baseline_MSE = mean_squared_error(train[y], train['baseline'])
    
    # calculate the root mean of squared error
    baseline_RMSE = mean_squared_error(train[y], train['baseline'], squared=False)
    
    # print results
    print(f'''Baseline Model Metrics
    SSE = {baseline_SSE}
    MSE = {baseline_MSE}
    RMSE = {baseline_RMSE}
    ''')
    
    # exit function and return RMSE
    return baseline_RMSE


def better_than_baseline(train, y='', yhat=''):
    '''
    Arguments: 
        1. train dataset
        2. y: the column name that holds the actual outcomes
        3. yhat: the column name that holds the predicted outcomes
    Actions:
        1. Computes the SSE, MSE, and RMSE for the baseline model
        2. Computes the SSE, ESS, TSS, MSE, and RMSE for a model
    Returns:
        1. Displays the SSE, MSE, and RMSE for the baseline model
        2. Display of SSE, ESS, TSS, MSE, and RMSE for the model created
        3. Returns True if model RMSE is less than baseline RMSE
    Modules:
    '''
    
    # compares the baseline and model RMSE
    return baseline_mean_errors(train, y=y) > regression_errors(train, y=y, yhat=yhat) 
