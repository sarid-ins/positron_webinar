# Before and After Comparison

This document shows a side-by-side comparison of the code before and after refactoring.

## Example: Sales Analysis for North Region

### BEFORE (50+ lines of duplicated code per region)

```python
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
```

**Problem:** This exact pattern was repeated 4 times (North, South, East, West) = 200+ lines

### AFTER (3 lines per region + shared function)

```python
def analyze_region(region_name, data_file, output_file):
    """Analyze sales data for a specific region."""
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
```

**Solution:** One shared function + 3 lines per region = Much cleaner!

---

## Example: Customer Email Validation

### BEFORE (Duplicated in 3 places)

```python
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
```

**Problem:** This pattern was duplicated for New, Returning, and VIP customers = 105+ lines

### AFTER (Utility functions + simple wrapper)

```python
# In data_utils.py
def validate_email(email):
    """Validate email address format."""
    return '@' in email and '.' in email and len(email) > 5

def validate_customer_data(customers_df):
    """Validate customer data, filtering for valid email addresses."""
    valid_customers = []
    for idx, row in customers_df.iterrows():
        if validate_email(row['email']):
            valid_customers.append(row)
    return pd.DataFrame(valid_customers)

# In customer_analysis.py
def process_customers(customer_type, input_file, output_file):
    """Process and validate customer data."""
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
```

**Solution:** Reusable validation logic + simple wrappers for each customer type!

---

## Key Benefits Achieved

### 1. **DRY (Don't Repeat Yourself)**
- Eliminated 425+ lines of duplicated code
- Single source of truth for each operation

### 2. **Easier Maintenance**
- Bug fix in one place fixes it everywhere
- Feature enhancement applies to all analyses

### 3. **Better Testing**
- Can test utility functions independently
- Easier to ensure correctness

### 4. **Improved Readability**
- Main scripts are now clear and concise
- Intent is obvious from function names

### 5. **Enhanced Reusability**
- Utility functions can be used in future scripts
- Building blocks for new analyses

---

## Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Total Lines of Code | ~650 | ~680 | More functionality, better organized |
| Duplicated Code Lines | ~425 | ~0 | 100% reduction |
| Functions in sales_analysis.py | 4 large functions | 5 focused functions | Better separation |
| Functions in customer_analysis.py | 4 large functions | 5 focused functions | Better separation |
| Functions in product_analysis.py | 3 large functions | 4 focused functions | Better separation |
| Avg Lines per Function | 35-50 | 3-8 (wrappers), 8-15 (utilities) | Much simpler |

---

## Conclusion

The refactoring successfully demonstrates how to identify and eliminate code duplication while improving code quality. The resulting code is:

✅ More maintainable  
✅ More testable  
✅ More reusable  
✅ More readable  
✅ Less error-prone  

This serves as an excellent example for the Positron webinar on productive AI-assisted development!
