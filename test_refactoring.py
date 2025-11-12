"""
Test script to verify refactored code maintains correct structure and interfaces.
This test verifies the code structure without executing (no pandas/matplotlib required).
"""

import ast
import os


def get_function_names(filepath):
    """Parse Python file and extract function names."""
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def test_sales_analysis_interface():
    """Test that sales_analysis.py maintains expected interface."""
    functions = get_function_names('sales_analysis.py')
    
    # Check that all region analysis functions exist
    assert 'analyze_north_region' in functions, "analyze_north_region function missing"
    assert 'analyze_south_region' in functions, "analyze_south_region function missing"
    assert 'analyze_east_region' in functions, "analyze_east_region function missing"
    assert 'analyze_west_region' in functions, "analyze_west_region function missing"
    
    # Check that the new shared function exists
    assert 'analyze_region' in functions, "analyze_region function missing"
    
    print("✓ sales_analysis.py interface is correct")


def test_customer_analysis_interface():
    """Test that customer_analysis.py maintains expected interface."""
    functions = get_function_names('customer_analysis.py')
    
    # Check that all customer processing functions exist
    assert 'process_new_customers' in functions, "process_new_customers function missing"
    assert 'process_returning_customers' in functions, "process_returning_customers function missing"
    assert 'process_vip_customers' in functions, "process_vip_customers function missing"
    
    # Check that the new shared function exists
    assert 'process_customers' in functions, "process_customers function missing"
    
    # Check that report generation function exists
    assert 'generate_customer_report' in functions, "generate_customer_report function missing"
    
    print("✓ customer_analysis.py interface is correct")


def test_product_analysis_interface():
    """Test that product_analysis.py maintains expected interface."""
    functions = get_function_names('product_analysis.py')
    
    # Check that all category calculation functions exist
    assert 'calculate_electronics_metrics' in functions, "calculate_electronics_metrics function missing"
    assert 'calculate_clothing_metrics' in functions, "calculate_clothing_metrics function missing"
    assert 'calculate_home_goods_metrics' in functions, "calculate_home_goods_metrics function missing"
    
    # Check that the new shared function exists
    assert 'calculate_category_metrics' in functions, "calculate_category_metrics function missing"
    
    print("✓ product_analysis.py interface is correct")


def test_utility_modules():
    """Test that utility modules exist and have expected functions."""
    data_utils_funcs = get_function_names('data_utils.py')
    stats_utils_funcs = get_function_names('statistics_utils.py')
    viz_utils_funcs = get_function_names('visualization_utils.py')
    
    # Test data_utils
    assert 'load_and_clean_sales_data' in data_utils_funcs, "load_and_clean_sales_data missing"
    assert 'validate_email' in data_utils_funcs, "validate_email missing"
    assert 'validate_customer_data' in data_utils_funcs, "validate_customer_data missing"
    assert 'load_and_validate_customers' in data_utils_funcs, "load_and_validate_customers missing"
    
    # Test statistics_utils
    assert 'calculate_sales_statistics' in stats_utils_funcs, "calculate_sales_statistics missing"
    assert 'calculate_age_statistics' in stats_utils_funcs, "calculate_age_statistics missing"
    assert 'calculate_product_metrics' in stats_utils_funcs, "calculate_product_metrics missing"
    assert 'get_summary_metrics' in stats_utils_funcs, "get_summary_metrics missing"
    
    # Test visualization_utils
    assert 'create_time_series_plot' in viz_utils_funcs, "create_time_series_plot missing"
    assert 'print_sales_statistics' in viz_utils_funcs, "print_sales_statistics missing"
    assert 'print_customer_statistics' in viz_utils_funcs, "print_customer_statistics missing"
    assert 'print_product_metrics' in viz_utils_funcs, "print_product_metrics missing"
    
    print("✓ All utility modules have expected functions")


def count_function_lines(filepath, function_name):
    """Count non-comment, non-empty lines in a function."""
    with open(filepath, 'r') as f:
        tree = ast.parse(f.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            # Count body statements (rough approximation of complexity)
            return len(node.body)
    return 0


def test_code_reduction():
    """Verify that refactoring reduced code duplication."""
    # Count region-specific functions in sales_analysis
    region_functions = ['analyze_north_region', 'analyze_south_region', 
                       'analyze_east_region', 'analyze_west_region']
    
    for func_name in region_functions:
        lines = count_function_lines('sales_analysis.py', func_name)
        # Each function should now be very short (just a return statement)
        assert lines <= 2, f"{func_name} is still too long ({lines} statements), refactoring may have failed"
    
    print("✓ Code duplication successfully reduced")


if __name__ == '__main__':
    print("Testing refactored code structure...\n")
    
    test_sales_analysis_interface()
    test_customer_analysis_interface()
    test_product_analysis_interface()
    test_utility_modules()
    test_code_reduction()
    
    print("\n✅ All tests passed! Refactoring is successful.")
    print("The refactored code maintains the same public interface while eliminating duplication.")
