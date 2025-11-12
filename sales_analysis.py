"""
Sales Analysis Script - Contains Duplicated Code Patterns
This script analyzes sales data from multiple regions with duplicated logic.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def analyze_north_region():
    """Analyze sales data for North region."""
    # Load data
    data = pd.read_csv('data/north_sales.csv')
    
    # Clean data
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)
    
    # Calculate statistics
    total_sales = data['amount'].sum()
    avg_sales = data['amount'].mean()
    max_sales = data['amount'].max()
    min_sales = data['amount'].min()
    
    # Print results
    print(f"North Region Analysis:")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Sales: ${avg_sales:,.2f}")
    print(f"Max Sales: ${max_sales:,.2f}")
    print(f"Min Sales: ${min_sales:,.2f}")
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['amount'])
    plt.title('North Region Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/north_sales_plot.png')
    plt.close()
    
    return {
        'total': total_sales,
        'average': avg_sales,
        'max': max_sales,
        'min': min_sales
    }


def analyze_south_region():
    """Analyze sales data for South region."""
    # Load data
    data = pd.read_csv('data/south_sales.csv')
    
    # Clean data
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)
    
    # Calculate statistics
    total_sales = data['amount'].sum()
    avg_sales = data['amount'].mean()
    max_sales = data['amount'].max()
    min_sales = data['amount'].min()
    
    # Print results
    print(f"South Region Analysis:")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Sales: ${avg_sales:,.2f}")
    print(f"Max Sales: ${max_sales:,.2f}")
    print(f"Min Sales: ${min_sales:,.2f}")
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['amount'])
    plt.title('South Region Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/south_sales_plot.png')
    plt.close()
    
    return {
        'total': total_sales,
        'average': avg_sales,
        'max': max_sales,
        'min': min_sales
    }


def analyze_east_region():
    """Analyze sales data for East region."""
    # Load data
    data = pd.read_csv('data/east_sales.csv')
    
    # Clean data
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)
    
    # Calculate statistics
    total_sales = data['amount'].sum()
    avg_sales = data['amount'].mean()
    max_sales = data['amount'].max()
    min_sales = data['amount'].min()
    
    # Print results
    print(f"East Region Analysis:")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Sales: ${avg_sales:,.2f}")
    print(f"Max Sales: ${max_sales:,.2f}")
    print(f"Min Sales: ${min_sales:,.2f}")
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['amount'])
    plt.title('East Region Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/east_sales_plot.png')
    plt.close()
    
    return {
        'total': total_sales,
        'average': avg_sales,
        'max': max_sales,
        'min': min_sales
    }


def analyze_west_region():
    """Analyze sales data for West region."""
    # Load data
    data = pd.read_csv('data/west_sales.csv')
    
    # Clean data
    data = data.dropna()
    data['date'] = pd.to_datetime(data['date'])
    data['amount'] = data['amount'].astype(float)
    
    # Calculate statistics
    total_sales = data['amount'].sum()
    avg_sales = data['amount'].mean()
    max_sales = data['amount'].max()
    min_sales = data['amount'].min()
    
    # Print results
    print(f"West Region Analysis:")
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Average Sales: ${avg_sales:,.2f}")
    print(f"Max Sales: ${max_sales:,.2f}")
    print(f"Min Sales: ${min_sales:,.2f}")
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['amount'])
    plt.title('West Region Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/west_sales_plot.png')
    plt.close()
    
    return {
        'total': total_sales,
        'average': avg_sales,
        'max': max_sales,
        'min': min_sales
    }


if __name__ == '__main__':
    print("Analyzing Regional Sales Data...\n")
    
    north_results = analyze_north_region()
    print()
    
    south_results = analyze_south_region()
    print()
    
    east_results = analyze_east_region()
    print()
    
    west_results = analyze_west_region()
    print()
    
    print("Analysis complete!")
