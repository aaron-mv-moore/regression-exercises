# tabular data
import pandas as pd
import numpy as np
# access os system
import os
# credentials
from env import get_db_url
# stats
import scipy.stats as stats
# dtat splits
from sklearn.model_selection import train_test_split


def get_zillow_data():
    '''
    Arguments: none
    Actions: 
        1. If file exists in current working directory, opens file
        2. If file doesn't exist in current working directory, querys MySQL database and saves it to the current working directory
    Returns: df
    Modules: pandas as pd, from env import get_db_url, os
    '''
    
    # assigns filename
    filename = 'zillow.csv'
    
    # checks to see if the file exists in the working directory
    if os.path.exists(filename):
        
        # opens file and assigns it to a variable
        df = pd.read_csv(filename, index_col=0)
        
        # returns the df
        return df
    
    else:
        
        # assigns MySQL query to the variables
        query = '''SELECT
                      bedroomcnt,
                      bathroomcnt,
                      calculatedfinishedsquarefeet,
                      taxvaluedollarcnt,
                      yearbuilt,
                      taxamount,
                      fips
                    FROM properties_2017
                    WHERE propertylandusetypeID = 261;'''
        
        # creates a database variable
        db = 'zillow'
        
        # assign MySQL url to url variable
        url = get_db_url(db)
        
        # reads results from query and assigns it to df
        df = pd.read_sql(query, url)

        # saves results to local file
        df.to_csv(filename)
        
        # returns the dataframe
        return df



def clean_data(df):
    '''
    Arguments: zillow df
    Actions:
        1. Drops null values
        2. Removes outliers
            a. Fips is skipped
            b. Monetary and year variables: 
                lower limit is bottom 5th percentile
                upper limit is Q3 + (1.5*IQR)
            c. Bedroom and Bathroom:
                lower limit is 1
                upper limit is Q3 + (1.5*IQR)
        3. Change column names
    Returns: cleaned df
    Modules:
        1. import scipy.stats as stats
        2. import pandas as pd
        3. import numpy as np
    '''
    # drop null values
    df = df.dropna()
    
    # drop outliers
    # initialize dict
    outlier_limits = {}
    
    # for each column in df
    for col in df:
        # skipping fips - this is a geographic indicator 
        if col == 'fips':
            pass
        # for all other columns
        else:
            # get 3rd quartile 
            Q3 = np.percentile(df[col], 75, interpolation = 'midpoint') 
            
            # get the inter-quartile range
            IQR = stats.iqr(df[col], interpolation = 'midpoint')
           
            # add to dictionary with the upper limits and lower limits
            outlier_limits[col] =  {'low_limit': np.percentile(df[col], 5, interpolation = 'midpoint'), 
                          'up_limit': Q3 + 1.5 * IQR
                         }
    
    # for each cols
    for col in df:
        
        # if col in the dict key
        if col in outlier_limits:
           
            # remove all oservations that exceed upper limit
            df = df[(df[col] <= outlier_limits[col]['up_limit'])]
            
            # for all cols except these two
            if col not in ['bathroomcnt', 'bedroomcnt']:
                
                # remove all observations that are under the lower limit
                df = df[(df[col] >= outlier_limits[col]['low_limit'])]
    
    # drop observations with less than 1 bathroom or bedroom count
    df = df[df['bedroomcnt'] >= 1]
    df = df[df['bathroomcnt'] >= 1]
    
    # change columns names
    df = df.rename(columns={'bedroomcnt': 'beds',
                  'bathroomcnt': 'baths',
                  'calculatedfinishedsquarefeet': 'square_feet',
                  'taxvaluedollarcnt': 'tax_value',
                   'yearbuilt': 'year_built',
                   'taxamount': 'tax_amount'
                  })
    
    # exit function with clean df
    return df



def split_data(df):
    '''
    Arguments: clean dataframe
    Actions: splits Dataframe into a train, validate, and test datasets for explorations
    Returns: train, validate, and test datasets
    Modules:
        1. from sklearn.model_selection import train_test_split
    '''
    # splitting with test focus
    train_val, test = train_test_split(df, train_size=.8, random_state=1017)
    
    #splitting with train/validate focus
    train, validate = train_test_split(train_val, train_size=.7, random_state=1017)

    # exits function and returns train, validate, test
    return train, validate, test



def wrangle_zillow():
    '''
    Arguments: none
    Actions:
        1. Gets zillow data
        2. Cleans zillow data
        3. Splits zillow data
    Returns: train, validate, test
    Modules: get_zillow_data, clean_data, split_data
    '''
    # splits cleaned data into train, validate, test
    train, validate, test = split_data(
        
        # cleans data
        clean_data(
        
            # retrieves data
            get_zillow_data()))
    
    # exits function with wrangled data
    return train, validate, test
