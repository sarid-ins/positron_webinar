# Usage Guide for Refactored Code

This guide explains how to use the refactored data analysis code in this repository.

## Overview

This repository contains a refactored Python codebase that demonstrates best practices for eliminating code duplication. It includes three analysis modules and three utility modules.

## File Structure

```
positron_webinar/
├── sales_analysis.py          # Regional sales analysis
├── customer_analysis.py       # Customer data processing
├── product_analysis.py        # Product performance metrics
├── data_utils.py             # Data loading and validation utilities
├── statistics_utils.py       # Statistical calculation utilities
├── visualization_utils.py    # Output formatting and plotting utilities
├── test_refactoring.py       # Test suite
├── REFACTORING_SUMMARY.md    # Technical documentation
├── BEFORE_AFTER_COMPARISON.md # Visual examples
└── USAGE.md                  # This file
```

## Requirements

```bash
pip install pandas numpy matplotlib
```

## Using the Analysis Modules

### Sales Analysis

Analyze sales data for different regions:

```python
from sales_analysis import (
    analyze_north_region,
    analyze_south_region,
    analyze_east_region,
    analyze_west_region
)

# Analyze a specific region
north_stats = analyze_north_region()
# Returns: {'total': ..., 'average': ..., 'max': ..., 'min': ...}

# Or use the generic function directly
from sales_analysis import analyze_region
stats = analyze_region('Central Region', 
                      'data/central_sales.csv',
                      'outputs/central_plot.png')
```

### Customer Analysis

Process and validate customer data:

```python
from customer_analysis import (
    process_new_customers,
    process_returning_customers,
    process_vip_customers,
    generate_customer_report
)

# Process specific customer types
new_customers_df = process_new_customers()

# Generate reports
generate_customer_report('new')

# Or use the generic function
from customer_analysis import process_customers
df = process_customers('Premium',
                      'data/premium_customers.csv',
                      'outputs/premium_clean.csv')
```

### Product Analysis

Calculate product performance metrics:

```python
from product_analysis import (
    calculate_electronics_metrics,
    calculate_clothing_metrics,
    calculate_home_goods_metrics
)

# Analyze specific categories
electronics_df = calculate_electronics_metrics()

# Or use the generic function
from product_analysis import calculate_category_metrics
df = calculate_category_metrics('Books', 
                               'data/books_products.csv')
```

## Using Utility Modules Directly

You can also use the utility functions directly in your own scripts:

### Data Utilities

```python
from data_utils import (
    load_and_clean_sales_data,
    validate_email,
    load_and_validate_customers
)

# Load and clean sales data
sales_data = load_and_clean_sales_data('data/my_sales.csv')

# Validate an email
is_valid = validate_email('user@example.com')  # Returns True

# Load and validate customers
customers = load_and_validate_customers('data/customers.csv')
```

### Statistics Utilities

```python
from statistics_utils import (
    calculate_sales_statistics,
    calculate_age_statistics,
    calculate_product_metrics,
    get_summary_metrics
)

# Calculate sales statistics
stats = calculate_sales_statistics(sales_df)

# Calculate age statistics
age_stats = calculate_age_statistics(customers_df)

# Calculate product metrics
products_with_metrics = calculate_product_metrics(products_df)

# Get summary metrics
summary = get_summary_metrics(products_with_metrics)
```

### Visualization Utilities

```python
from visualization_utils import (
    create_time_series_plot,
    print_sales_statistics,
    print_customer_statistics,
    print_product_metrics
)

# Create a time series plot
create_time_series_plot(data, 'date', 'amount',
                       'My Sales Plot',
                       'output.png')

# Print formatted statistics
print_sales_statistics('Q1 2024', sales_stats)
print_customer_statistics('Gold Tier', count, age_stats)
print_product_metrics('Tech', metrics, top_5_df)
```

## Running Tests

Verify that the refactoring is correct:

```bash
python test_refactoring.py
```

Expected output:
```
Testing refactored code structure...

✓ sales_analysis.py interface is correct
✓ customer_analysis.py interface is correct
✓ product_analysis.py interface is correct
✓ All utility modules have expected functions
✓ Code duplication successfully reduced

✅ All tests passed! Refactoring is successful.
```

## Running Analysis Scripts

Each analysis module can be run directly:

```bash
# Sales analysis
python sales_analysis.py

# Customer analysis
python customer_analysis.py

# Product analysis
python product_analysis.py
```

**Note:** These scripts expect data files to exist in the `data/` directory. The scripts demonstrate the refactored code structure but won't execute fully without the data files.

## Benefits of This Structure

1. **Reusability**: Utility functions can be used across multiple scripts
2. **Maintainability**: Changes to core logic only need to be made once
3. **Testability**: Each utility function can be tested independently
4. **Extensibility**: Easy to add new analysis types using existing utilities
5. **Clarity**: Code intent is clear from function names

## Example: Adding a New Analysis

To add a new region to sales analysis:

```python
from sales_analysis import analyze_region

def analyze_central_region():
    """Analyze sales data for Central region."""
    return analyze_region('Central Region',
                         'data/central_sales.csv',
                         'outputs/central_sales_plot.png')
```

That's it! Three lines to add a new region, vs. 50+ lines before refactoring.

## Learning Resources

- **REFACTORING_SUMMARY.md** - Detailed technical documentation of the refactoring
- **BEFORE_AFTER_COMPARISON.md** - Side-by-side code comparisons showing improvements
- **readme.md** - Original repository README

## Questions?

This code is part of a webinar on Positron and AI-assisted development. The refactoring demonstrates how to identify and eliminate code duplication while maintaining functionality.
