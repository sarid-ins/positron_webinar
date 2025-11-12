"""
Visualization Utilities Module
Common functions for creating visualizations and reports.
"""

import matplotlib.pyplot as plt


def create_time_series_plot(data, date_column, value_column, title, output_path):
    """
    Create a time series plot and save it to file.
    
    Args:
        data: DataFrame containing the data
        date_column: Name of the date column
        value_column: Name of the value column
        title: Plot title
        output_path: Path to save the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data[date_column], data[value_column])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Sales Amount ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def print_sales_statistics(region_name, stats):
    """
    Print formatted sales statistics.
    
    Args:
        region_name: Name of the region
        stats: Dictionary with total, average, max, and min values
    """
    print(f"{region_name} Analysis:")
    print(f"Total Sales: ${stats['total']:,.2f}")
    print(f"Average Sales: ${stats['average']:,.2f}")
    print(f"Max Sales: ${stats['max']:,.2f}")
    print(f"Min Sales: ${stats['min']:,.2f}")


def print_customer_statistics(customer_type, count, age_stats):
    """
    Print formatted customer statistics.
    
    Args:
        customer_type: Type of customer (e.g., "New", "Returning")
        count: Total number of valid customers
        age_stats: Dictionary with average, min, and max age
    """
    print(f"{customer_type} Customers Statistics:")
    print(f"Total Valid: {count}")
    print(f"Average Age: {age_stats['average']:.1f}")
    print(f"Age Range: {age_stats['min']} - {age_stats['max']}")


def print_product_metrics(category_name, metrics, top_products):
    """
    Print formatted product metrics.
    
    Args:
        category_name: Name of the product category
        metrics: Dictionary with total_revenue, total_profit, and avg_margin
        top_products: DataFrame of top performing products
    """
    print(f"{category_name} Category:")
    print(f"  Total Revenue: ${metrics['total_revenue']:,.2f}")
    print(f"  Total Profit: ${metrics['total_profit']:,.2f}")
    print(f"  Avg Profit Margin: {metrics['avg_margin']:.2f}%")
    print("  Top 5 Products by Profit:")
    for idx, row in top_products.iterrows():
        print(f"    - {row['product_name']}: ${row['profit']:,.2f}")
