"""
Sales Analysis Script - Refactored Version
This script analyzes sales data from multiple regions using shared utility functions.
"""

from data_utils import load_and_clean_sales_data
from statistics_utils import calculate_sales_statistics
from visualization_utils import create_time_series_plot, print_sales_statistics


def analyze_region(region_name, data_file, output_file):
    """
    Analyze sales data for a specific region.
    
    Args:
        region_name: Name of the region (e.g., "North", "South")
        data_file: Path to the CSV file containing sales data
        output_file: Path to save the visualization
        
    Returns:
        Dictionary with sales statistics
    """
    data = load_and_clean_sales_data(data_file)
    stats = calculate_sales_statistics(data)
    print_sales_statistics(region_name, stats)
    create_time_series_plot(data, 'date', 'amount', 
                            f'{region_name} Region Sales Over Time', 
                            output_file)
    return stats


def analyze_north_region():
    """Analyze sales data for North region."""
    return analyze_region('North Region', 
                         'data/north_sales.csv', 
                         'outputs/north_sales_plot.png')


def analyze_south_region():
    """Analyze sales data for South region."""
    return analyze_region('South Region', 
                         'data/south_sales.csv', 
                         'outputs/south_sales_plot.png')


def analyze_east_region():
    """Analyze sales data for East region."""
    return analyze_region('East Region', 
                         'data/east_sales.csv', 
                         'outputs/east_sales_plot.png')


def analyze_west_region():
    """Analyze sales data for West region."""
    return analyze_region('West Region', 
                         'data/west_sales.csv', 
                         'outputs/west_sales_plot.png')


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
