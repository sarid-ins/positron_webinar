"""
Data Utilities Module
Common functions for data loading, cleaning, and validation.
"""

import pandas as pd


def load_and_clean_sales_data(filepath):
    """
    Load and clean sales data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        Cleaned pandas DataFrame
    """
    data = pd.read_csv(filepath)
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)
    return data


def validate_email(email):
    """
    Validate email address format.
    
    Args:
        email: Email address string
        
    Returns:
        Boolean indicating if email is valid
    """
    return '@' in email and '.' in email and len(email) > 5


def validate_customer_data(customers_df):
    """
    Validate customer data, filtering for valid email addresses.
    
    Args:
        customers_df: DataFrame containing customer data with 'email' column
        
    Returns:
        DataFrame with only valid customer records
    """
    valid_customers = []
    for idx, row in customers_df.iterrows():
        if validate_email(row['email']):
            valid_customers.append(row)
    return pd.DataFrame(valid_customers)


def load_and_validate_customers(filepath):
    """
    Load and validate customer data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        Validated pandas DataFrame
    """
    customers = pd.read_csv(filepath)
    return validate_customer_data(customers)
