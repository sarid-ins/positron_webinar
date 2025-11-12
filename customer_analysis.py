"""
Customer Analysis Script - Refactored Version
This script analyzes customer data using shared utility functions.
"""

import pandas as pd
from data_utils import load_and_validate_customers
from statistics_utils import calculate_age_statistics
from visualization_utils import print_customer_statistics


def process_customers(customer_type, input_file, output_file):
    """
    Process and validate customer data.
    
    Args:
        customer_type: Type of customer (e.g., "New", "Returning", "VIP")
        input_file: Path to input CSV file
        output_file: Path to output CSV file
        
    Returns:
        Validated DataFrame
    """
    valid_df = load_and_validate_customers(input_file)
    age_stats = calculate_age_statistics(valid_df)
    print_customer_statistics(customer_type, len(valid_df), age_stats)
    valid_df.to_csv(output_file, index=False)
    return valid_df


def process_new_customers():
    """Process and validate new customer data."""
    return process_customers('New', 
                            'data/new_customers.csv', 
                            'outputs/new_customers_clean.csv')


def process_returning_customers():
    """Process and validate returning customer data."""
    return process_customers('Returning', 
                            'data/returning_customers.csv', 
                            'outputs/returning_customers_clean.csv')


def process_vip_customers():
    """Process and validate VIP customer data."""
    return process_customers('VIP', 
                            'data/vip_customers.csv', 
                            'outputs/vip_customers_clean.csv')


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
