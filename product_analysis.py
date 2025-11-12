"""
Product Analysis Script - Refactored Version
This script analyzes product performance using shared utility functions.
"""

import pandas as pd
from statistics_utils import calculate_product_metrics, get_summary_metrics
from visualization_utils import print_product_metrics


def calculate_category_metrics(category_name, data_file):
    """
    Calculate performance metrics for a product category.
    
    Args:
        category_name: Name of the product category
        data_file: Path to the CSV file containing product data
        
    Returns:
        DataFrame with calculated metrics
    """
    products = pd.read_csv(data_file)
    products = calculate_product_metrics(products)
    metrics = get_summary_metrics(products)
    top_products = products.nlargest(5, 'profit')
    print_product_metrics(category_name, metrics, top_products)
    return products


def calculate_electronics_metrics():
    """Calculate performance metrics for electronics products."""
    return calculate_category_metrics('Electronics', 
                                     'data/electronics_products.csv')


def calculate_clothing_metrics():
    """Calculate performance metrics for clothing products."""
    return calculate_category_metrics('Clothing', 
                                     'data/clothing_products.csv')


def calculate_home_goods_metrics():
    """Calculate performance metrics for home goods products."""
    return calculate_category_metrics('Home Goods', 
                                     'data/home_goods_products.csv')


if __name__ == '__main__':
    print("Calculating Product Performance Metrics...\n")
    
    electronics = calculate_electronics_metrics()
    print()
    
    clothing = calculate_clothing_metrics()
    print()
    
    home_goods = calculate_home_goods_metrics()
    print()
    
    print("Product analysis complete!")
