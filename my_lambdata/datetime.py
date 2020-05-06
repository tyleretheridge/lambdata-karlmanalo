# my_lambdata\datetime.py

# Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

from pandas import to_datetime


def split_date(X):

    # Copy data frame to prevent setting with copy warnings
    X = X.copy()

    # Converting date to datetime format
    X['date'] = to_datetime(X['date'], infer_datetime_format=True)

    # Extracting year, month and day from datetime
    X['year'] = X['date'].dt.year
    X['month'] = X['date'].dt.month
    X['day'] = X['date'].dt.day

    # Dropping date column due to redundancy
    X = X.drop(columns='date')

    return X
