
# insert host name here
host = 'string host name'

# insert your username
user = 'string username'

# insert your password
password = 'string password'

def get_db_url(db):
    '''
    Arguments: database as a string literal
    Actions: Creates a URL to access a MySQL database
    '''

    # creates url with all the info
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'

    # returns url
    return url
