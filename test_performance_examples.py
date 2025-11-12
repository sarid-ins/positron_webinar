"""
Test suite for performance examples
Validates that both slow and fast versions produce correct results
"""

import pandas as pd
import numpy as np
import slow_code_examples as sce


def test_dataframe_operations():
    """Test that slow and fast DataFrame operations produce same results"""
    df = pd.DataFrame({
        'value1': [1.0, 2.0, 3.0],
        'value2': [4.0, 5.0, 6.0]
    })
    
    result_slow = sce.process_dataframe_slow(df)
    result_fast = sce.process_dataframe_fast(df)
    
    assert result_slow['total'].equals(result_fast['total']), "Total column mismatch"
    assert result_slow['average'].equals(result_fast['average']), "Average column mismatch"
    assert result_slow['total'].tolist() == [5.0, 7.0, 9.0], "Total calculation incorrect"
    print("✓ test_dataframe_operations passed")


def test_string_concatenation():
    """Test that slow and fast string concatenation produce same results"""
    items = ["a", "b", "c"]
    
    result_slow = sce.build_large_string_slow(items)
    result_fast = sce.build_large_string_fast(items)
    
    assert result_slow == result_fast, "String concatenation results differ"
    assert result_fast == "a, b, c", "String concatenation incorrect"
    print("✓ test_string_concatenation passed")


def test_sum_of_squares():
    """Test that slow and fast sum of squares produce same results"""
    n = 100
    
    result_slow = sce.sum_of_squares_slow(n)
    result_fast = sce.sum_of_squares_fast(n)
    
    assert result_slow == result_fast, "Sum of squares results differ"
    expected = sum(x**2 for x in range(n))
    assert result_fast == expected, "Sum of squares calculation incorrect"
    print("✓ test_sum_of_squares passed")


def test_dataframe_filtering():
    """Test that slow and fast filtering produce same results"""
    df = pd.DataFrame({
        'value1': [0.3, 0.6, 0.8, 0.4],
        'value2': [0.7, 0.2, 0.9, 0.6]
    })
    
    result_slow = sce.filter_dataframe_slow(df, 0.5)
    result_fast = sce.filter_dataframe_fast(df, 0.5)
    
    # Reset index for comparison
    result_slow = result_slow.reset_index(drop=True)
    result_fast = result_fast.reset_index(drop=True)
    
    assert result_slow.equals(result_fast), "Filtering results differ"
    assert len(result_fast) == 1, "Should have 1 row after filtering"
    print("✓ test_dataframe_filtering passed")


def test_count_items():
    """Test that slow and fast counting produce same results"""
    items = ["a", "b", "a", "c", "b", "a"]
    
    result_slow = sce.count_items_slow(items)
    result_fast = sce.count_items_fast(items)
    
    assert result_slow == result_fast, "Count results differ"
    assert result_fast == {"a": 3, "b": 2, "c": 1}, "Count calculation incorrect"
    print("✓ test_count_items passed")


def test_array_creation():
    """Test that slow and fast array creation produce same results"""
    n = 10
    
    result_slow = sce.create_array_slow(n)
    result_fast = sce.create_array_fast(n)
    
    assert np.array_equal(result_slow, result_fast), "Array results differ"
    expected = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    assert np.array_equal(result_fast, expected), "Array calculation incorrect"
    print("✓ test_array_creation passed")


def test_dataframe_concatenation():
    """Test that slow and fast concatenation produce same results"""
    dfs = [
        pd.DataFrame({'value': [1, 2]}),
        pd.DataFrame({'value': [3, 4]}),
        pd.DataFrame({'value': [5, 6]})
    ]
    
    result_slow = sce.concatenate_dataframes_slow(dfs)
    result_fast = sce.concatenate_dataframes_fast(dfs)
    
    # Reset index for comparison
    result_slow = result_slow.reset_index(drop=True)
    result_fast = result_fast.reset_index(drop=True)
    
    assert result_slow.equals(result_fast), "Concatenation results differ"
    assert result_fast['value'].tolist() == [1, 2, 3, 4, 5, 6], "Concatenation incorrect"
    print("✓ test_dataframe_concatenation passed")


def test_local_vs_global():
    """Test that local variable function produces correct result"""
    items = [1, 2, 3, 4, 5]
    
    result = sce.process_with_local_fast(items)
    
    assert result == 15, "Local variable calculation incorrect"
    print("✓ test_local_vs_global passed")


def run_all_tests():
    """Run all tests"""
    print("Running performance example tests...")
    print("=" * 50)
    
    test_dataframe_operations()
    test_string_concatenation()
    test_sum_of_squares()
    test_dataframe_filtering()
    test_count_items()
    test_array_creation()
    test_dataframe_concatenation()
    test_local_vs_global()
    
    print("=" * 50)
    print("All tests passed! ✓")


if __name__ == "__main__":
    run_all_tests()
