"""
Product Analysis Script - Contains Duplicated Code Patterns
This script analyzes product performance with duplicated calculation logic.
"""

import pandas as pd
import numpy as np


def calculate_electronics_metrics():
    """Calculate performance metrics for electronics products."""
    products = pd.read_csv('data/electronics_products.csv')
    
    # Calculate revenue
    products['revenue'] = products['quantity_sold'] * products['price']
    
    # Calculate profit
    products['profit'] = products['revenue'] - (products['quantity_sold'] * products['cost'])
    
    # Calculate profit margin
    products['profit_margin'] = (products['profit'] / products['revenue']) * 100
    
    # Summary statistics
    total_revenue = products['revenue'].sum()
    total_profit = products['profit'].sum()
    avg_margin = products['profit_margin'].mean()
    
    print("Electronics Category:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Avg Profit Margin: {avg_margin:.2f}%")
    
    # Find top performers
    top_products = products.nlargest(5, 'profit')
    print("  Top 5 Products by Profit:")
    for idx, row in top_products.iterrows():
        print(f"    - {row['product_name']}: ${row['profit']:,.2f}")
    
    return products


def calculate_clothing_metrics():
    """Calculate performance metrics for clothing products."""
    products = pd.read_csv('data/clothing_products.csv')
    
    # Calculate revenue
    products['revenue'] = products['quantity_sold'] * products['price']
    
    # Calculate profit
    products['profit'] = products['revenue'] - (products['quantity_sold'] * products['cost'])
    
    # Calculate profit margin
    products['profit_margin'] = (products['profit'] / products['revenue']) * 100
    
    # Summary statistics
    total_revenue = products['revenue'].sum()
    total_profit = products['profit'].sum()
    avg_margin = products['profit_margin'].mean()
    
    print("Clothing Category:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Avg Profit Margin: {avg_margin:.2f}%")
    
    # Find top performers
    top_products = products.nlargest(5, 'profit')
    print("  Top 5 Products by Profit:")
    for idx, row in top_products.iterrows():
        print(f"    - {row['product_name']}: ${row['profit']:,.2f}")
    
    return products


def calculate_home_goods_metrics():
    """Calculate performance metrics for home goods products."""
    products = pd.read_csv('data/home_goods_products.csv')
    
    # Calculate revenue
    products['revenue'] = products['quantity_sold'] * products['price']
    
    # Calculate profit
    products['profit'] = products['revenue'] - (products['quantity_sold'] * products['cost'])
    
    # Calculate profit margin
    products['profit_margin'] = (products['profit'] / products['revenue']) * 100
    
    # Summary statistics
    total_revenue = products['revenue'].sum()
    total_profit = products['profit'].sum()
    avg_margin = products['profit_margin'].mean()
    
    print("Home Goods Category:")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Profit: ${total_profit:,.2f}")
    print(f"  Avg Profit Margin: {avg_margin:.2f}%")
    
    # Find top performers
    top_products = products.nlargest(5, 'profit')
    print("  Top 5 Products by Profit:")
    for idx, row in top_products.iterrows():
        print(f"    - {row['product_name']}: ${row['profit']:,.2f}")
    
    return products


if __name__ == '__main__':
    print("Calculating Product Performance Metrics...\n")
    
    electronics = calculate_electronics_metrics()
    print()
    
    clothing = calculate_clothing_metrics()
    print()
    
    home_goods = calculate_home_goods_metrics()
    print()
    
    print("Product analysis complete!")
