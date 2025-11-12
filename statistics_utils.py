"""
Statistics Utilities Module
Common functions for statistical calculations and analysis.
"""

import pandas as pd


def calculate_sales_statistics(data):
    """
    Calculate standard sales statistics.
    
    Args:
        data: DataFrame with 'amount' column
        
    Returns:
        Dictionary with total, average, max, and min values
    """
    return {
        'total': data['amount'].sum(),
        'average': data['amount'].mean(),
        'max': data['amount'].max(),
        'min': data['amount'].min()
    }


def calculate_age_statistics(data):
    """
    Calculate age-related statistics.
    
    Args:
        data: DataFrame with 'age' column
        
    Returns:
        Dictionary with average, min, and max age
    """
    return {
        'average': data['age'].mean(),
        'min': data['age'].min(),
        'max': data['age'].max()
    }


def calculate_product_metrics(products_df):
    """
    Calculate product performance metrics.
    
    Args:
        products_df: DataFrame with quantity_sold, price, and cost columns
        
    Returns:
        DataFrame with added revenue, profit, and profit_margin columns
    """
    products_df = products_df.copy()
    products_df['revenue'] = products_df['quantity_sold'] * products_df['price']
    products_df['profit'] = products_df['revenue'] - (products_df['quantity_sold'] * products_df['cost'])
    products_df['profit_margin'] = (products_df['profit'] / products_df['revenue']) * 100
    return products_df


def get_summary_metrics(products_df):
    """
    Calculate summary metrics for product data.
    
    Args:
        products_df: DataFrame with revenue, profit, and profit_margin columns
        
    Returns:
        Dictionary with total revenue, total profit, and average margin
    """
    return {
        'total_revenue': products_df['revenue'].sum(),
        'total_profit': products_df['profit'].sum(),
        'avg_margin': products_df['profit_margin'].mean()
    }
