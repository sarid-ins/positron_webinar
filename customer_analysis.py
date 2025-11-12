"""
Customer Analysis Script - Contains Duplicated Code Patterns
This script analyzes customer data with duplicated validation and processing logic.
"""

import pandas as pd
import numpy as np


def process_new_customers():
    """Process and validate new customer data."""
    customers = pd.read_csv('data/new_customers.csv')
    
    # Validate email
    valid_customers = []
    for idx, row in customers.iterrows():
        email = row['email']
        if '@' in email and '.' in email:
            if len(email) > 5:
                valid_customers.append(row)
    
    valid_df = pd.DataFrame(valid_customers)
    
    # Calculate age statistics
    avg_age = valid_df['age'].mean()
    min_age = valid_df['age'].min()
    max_age = valid_df['age'].max()
    
    print(f"New Customers Statistics:")
    print(f"Total Valid: {len(valid_df)}")
    print(f"Average Age: {avg_age:.1f}")
    print(f"Age Range: {min_age} - {max_age}")
    
    # Save cleaned data
    valid_df.to_csv('outputs/new_customers_clean.csv', index=False)
    
    return valid_df


def process_returning_customers():
    """Process and validate returning customer data."""
    customers = pd.read_csv('data/returning_customers.csv')
    
    # Validate email
    valid_customers = []
    for idx, row in customers.iterrows():
        email = row['email']
        if '@' in email and '.' in email:
            if len(email) > 5:
                valid_customers.append(row)
    
    valid_df = pd.DataFrame(valid_customers)
    
    # Calculate age statistics
    avg_age = valid_df['age'].mean()
    min_age = valid_df['age'].min()
    max_age = valid_df['age'].max()
    
    print(f"Returning Customers Statistics:")
    print(f"Total Valid: {len(valid_df)}")
    print(f"Average Age: {avg_age:.1f}")
    print(f"Age Range: {min_age} - {max_age}")
    
    # Save cleaned data
    valid_df.to_csv('outputs/returning_customers_clean.csv', index=False)
    
    return valid_df


def process_vip_customers():
    """Process and validate VIP customer data."""
    customers = pd.read_csv('data/vip_customers.csv')
    
    # Validate email
    valid_customers = []
    for idx, row in customers.iterrows():
        email = row['email']
        if '@' in email and '.' in email:
            if len(email) > 5:
                valid_customers.append(row)
    
    valid_df = pd.DataFrame(valid_customers)
    
    # Calculate age statistics
    avg_age = valid_df['age'].mean()
    min_age = valid_df['age'].min()
    max_age = valid_df['age'].max()
    
    print(f"VIP Customers Statistics:")
    print(f"Total Valid: {len(valid_df)}")
    print(f"Average Age: {avg_age:.1f}")
    print(f"Age Range: {min_age} - {max_age}")
    
    # Save cleaned data
    valid_df.to_csv('outputs/vip_customers_clean.csv', index=False)
    
    return valid_df


def generate_customer_report(customer_type):
    """Generate a detailed customer report."""
    if customer_type == 'new':
        df = pd.read_csv('outputs/new_customers_clean.csv')
        title = "New Customer Report"
    elif customer_type == 'returning':
        df = pd.read_csv('outputs/returning_customers_clean.csv')
        title = "Returning Customer Report"
    elif customer_type == 'vip':
        df = pd.read_csv('outputs/vip_customers_clean.csv')
        title = "VIP Customer Report"
    
    print(f"\n{title}")
    print("=" * 50)
    print(f"Total Customers: {len(df)}")
    print(f"Average Age: {df['age'].mean():.1f}")
    print(f"Male: {len(df[df['gender'] == 'M'])}")
    print(f"Female: {len(df[df['gender'] == 'F'])}")


if __name__ == '__main__':
    print("Processing Customer Data...\n")
    
    new_df = process_new_customers()
    returning_df = process_returning_customers()
    vip_df = process_vip_customers()
    
    generate_customer_report('new')
    generate_customer_report('returning')
    generate_customer_report('vip')
    
    print("\nCustomer processing complete!")
