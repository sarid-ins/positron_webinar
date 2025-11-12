"""
Examples of Slow and Inefficient Code Patterns
================================================

This file demonstrates common performance issues in Python data science code.
Each example includes both inefficient and optimized versions.
"""

import pandas as pd
import numpy as np
from typing import List
import time


# Example 1: Inefficient Loop-based DataFrame Operations
# -------------------------------------------------------
def process_dataframe_slow(df: pd.DataFrame) -> pd.DataFrame:
    """
    SLOW: Iterates row-by-row through a DataFrame
    This is one of the most common performance issues in pandas code.
    """
    result = df.copy()
    for idx in range(len(df)):
        result.loc[idx, 'total'] = result.loc[idx, 'value1'] + result.loc[idx, 'value2']
        result.loc[idx, 'average'] = (result.loc[idx, 'value1'] + result.loc[idx, 'value2']) / 2
    return result


def process_dataframe_fast(df: pd.DataFrame) -> pd.DataFrame:
    """
    FAST: Uses vectorized operations
    This can be 100-1000x faster than the row-by-row approach.
    """
    result = df.copy()
    result['total'] = result['value1'] + result['value2']
    result['average'] = (result['value1'] + result['value2']) / 2
    return result


# Example 2: Inefficient String Concatenation
# --------------------------------------------
def build_large_string_slow(items: List[str]) -> str:
    """
    SLOW: Repeatedly concatenates strings using += operator
    Each concatenation creates a new string object in memory.
    Time complexity: O(n²)
    """
    result = ""
    for i, item in enumerate(items):
        if i > 0:
            result += ", "
        result += item
    return result


def build_large_string_fast(items: List[str]) -> str:
    """
    FAST: Uses join() which allocates memory once
    Time complexity: O(n)
    """
    return ", ".join(items)


# Example 3: Inefficient List Comprehension vs Generator
# -------------------------------------------------------
def sum_of_squares_slow(n: int) -> int:
    """
    SLOW: Creates entire list in memory before summing
    Memory usage: O(n)
    """
    numbers = [x**2 for x in range(n)]
    return sum(numbers)


def sum_of_squares_fast(n: int) -> int:
    """
    FAST: Uses generator expression - computes values on-the-fly
    Memory usage: O(1)
    """
    return sum(x**2 for x in range(n))


# Example 4: Inefficient DataFrame Filtering
# -------------------------------------------
def filter_dataframe_slow(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    SLOW: Uses iterrows() which is slow and unpythonic
    Also creates intermediate DataFrames in a loop.
    """
    filtered_rows = []
    for idx, row in df.iterrows():
        if row['value1'] > threshold and row['value2'] > threshold:
            filtered_rows.append(row)
    return pd.DataFrame(filtered_rows)


def filter_dataframe_fast(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    FAST: Uses boolean indexing with vectorized operations
    """
    mask = (df['value1'] > threshold) & (df['value2'] > threshold)
    return df[mask]


# Example 5: Inefficient Dictionary Lookup
# -----------------------------------------
def count_items_slow(items: List[str]) -> dict:
    """
    SLOW: Uses list to check if key exists, then updates dictionary
    Each 'in' operation on a list is O(n).
    """
    result = {}
    keys_list = []
    for item in items:
        if item in keys_list:
            result[item] += 1
        else:
            result[item] = 1
            keys_list.append(item)
    return result


def count_items_fast(items: List[str]) -> dict:
    """
    FAST: Uses dictionary's get() method or defaultdict
    Dictionary lookup is O(1).
    """
    result = {}
    for item in items:
        result[item] = result.get(item, 0) + 1
    return result


# Example 6: Inefficient Global Variable Usage
# ---------------------------------------------
global_counter = 0

def process_with_global_slow(items: List[int]) -> int:
    """
    SLOW: Accesses global variable in tight loop
    Global variable access is slower than local variable access.
    """
    global global_counter
    for item in items:
        global_counter += item
    return global_counter


def process_with_local_fast(items: List[int]) -> int:
    """
    FAST: Uses local variable, which is faster to access
    """
    local_counter = 0
    for item in items:
        local_counter += item
    return local_counter


# Example 7: Inefficient NumPy Array Creation
# --------------------------------------------
def create_array_slow(n: int) -> np.ndarray:
    """
    SLOW: Appends to list then converts to array
    Requires memory reallocation on each append.
    """
    result = []
    for i in range(n):
        result.append(i * 2)
    return np.array(result)


def create_array_fast(n: int) -> np.ndarray:
    """
    FAST: Pre-allocates array or uses vectorized operations
    """
    return np.arange(n) * 2


# Example 8: Inefficient DataFrame Concatenation
# -----------------------------------------------
def concatenate_dataframes_slow(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    SLOW: Repeatedly concatenates DataFrames in a loop
    Each concat creates a new DataFrame, causing O(n²) behavior.
    """
    result = pd.DataFrame()
    for df in dfs:
        result = pd.concat([result, df], ignore_index=True)
    return result


def concatenate_dataframes_fast(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """
    FAST: Concatenates all DataFrames at once
    O(n) time complexity.
    """
    return pd.concat(dfs, ignore_index=True)


# Benchmark Functions
# -------------------
def benchmark_example(slow_func, fast_func, *args, **kwargs):
    """
    Utility function to compare performance of two implementations.
    """
    # Warm-up
    slow_func(*args, **kwargs)
    fast_func(*args, **kwargs)
    
    # Benchmark slow version
    start = time.time()
    slow_result = slow_func(*args, **kwargs)
    slow_time = time.time() - start
    
    # Benchmark fast version
    start = time.time()
    fast_result = fast_func(*args, **kwargs)
    fast_time = time.time() - start
    
    print(f"Slow version: {slow_time:.4f} seconds")
    print(f"Fast version: {fast_time:.4f} seconds")
    print(f"Speedup: {slow_time / fast_time:.2f}x faster")
    
    return slow_time, fast_time


if __name__ == "__main__":
    print("Performance Comparison Examples")
    print("=" * 50)
    
    # Test Example 1: DataFrame Operations
    print("\n1. DataFrame Operations")
    print("-" * 50)
    df = pd.DataFrame({
        'value1': np.random.rand(10000),
        'value2': np.random.rand(10000)
    })
    benchmark_example(process_dataframe_slow, process_dataframe_fast, df)
    
    # Test Example 2: String Concatenation
    print("\n2. String Concatenation")
    print("-" * 50)
    items = [f"item{i}" for i in range(10000)]
    benchmark_example(build_large_string_slow, build_large_string_fast, items)
    
    # Test Example 3: Sum of Squares
    print("\n3. Sum of Squares (Generator vs List)")
    print("-" * 50)
    benchmark_example(sum_of_squares_slow, sum_of_squares_fast, 1000000)
    
    # Test Example 4: DataFrame Filtering
    print("\n4. DataFrame Filtering")
    print("-" * 50)
    df = pd.DataFrame({
        'value1': np.random.rand(10000),
        'value2': np.random.rand(10000)
    })
    benchmark_example(filter_dataframe_slow, filter_dataframe_fast, df, 0.5)
    
    # Test Example 5: Dictionary Operations
    print("\n5. Counting Items")
    print("-" * 50)
    items = [f"item{i % 100}" for i in range(10000)]
    benchmark_example(count_items_slow, count_items_fast, items)
    
    # Test Example 6: Global vs Local Variables
    print("\n6. Global vs Local Variables")
    print("-" * 50)
    items = list(range(1000000))
    global_counter = 0  # Reset global counter
    benchmark_example(process_with_global_slow, process_with_local_fast, items)
    
    # Test Example 7: NumPy Array Creation
    print("\n7. NumPy Array Creation")
    print("-" * 50)
    benchmark_example(create_array_slow, create_array_fast, 100000)
    
    # Test Example 8: DataFrame Concatenation
    print("\n8. DataFrame Concatenation")
    print("-" * 50)
    dfs = [pd.DataFrame({'value': np.random.rand(100)}) for _ in range(100)]
    benchmark_example(concatenate_dataframes_slow, concatenate_dataframes_fast, dfs)
    
    print("\n" + "=" * 50)
    print("Benchmark completed!")
