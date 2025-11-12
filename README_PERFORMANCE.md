# Performance Optimization Examples

This directory contains code examples demonstrating common performance issues in data science code and their solutions.

## Files

- **slow_code_examples.py** - Python examples with benchmarks
- **slow_code_examples.R** - R examples with benchmarks
- **PERFORMANCE_GUIDE.md** - Comprehensive guide explaining each optimization
- **requirements.txt** - Python package dependencies

## Quick Start

### Python Examples

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the benchmarks:
```bash
python slow_code_examples.py
```

This will run all 8 performance comparisons and show you the speedup for each optimization.

### R Examples

1. Install required packages:
```r
install.packages(c("dplyr", "data.table"))
```

2. Run the benchmarks:
```r
source("slow_code_examples.R")
```

This will run all 10 performance comparisons and show you the speedup for each optimization.

## What's Inside

Both files contain side-by-side comparisons of:

1. **Inefficient code patterns** (marked as "SLOW")
2. **Optimized versions** (marked as "FAST")
3. **Benchmark functions** to measure the performance difference

### Common Issues Demonstrated

1. **Row-by-row DataFrame operations** → Vectorized operations (100-1000x faster)
2. **Growing collections in loops** → Pre-allocation or vectorization (100-1000x faster)
3. **Repeated concatenation** → Single batch operation (50-500x faster)
4. **Inefficient string building** → join/collapse operations (50-200x faster)
5. **Manual loops** → Built-in vectorized functions (10-100x faster)
6. **Slow filtering** → Boolean indexing (50-500x faster)
7. **List comprehensions** → Generator expressions (reduces memory)
8. **Global variable access** → Local variables (10-30% faster)
9. **Linear search in lists** → Dictionary/hash lookups (100-1000x faster)
10. **Manual matrix operations** → Optimized linear algebra (100-10000x faster)

## Expected Results

When you run the Python benchmarks, you should see output like:

```
Performance Comparison Examples
==================================================

1. DataFrame Operations
--------------------------------------------------
Slow version: 2.5232 seconds
Fast version: 0.0009 seconds
Speedup: 2771.90x faster

2. String Concatenation
--------------------------------------------------
Slow version: 0.0007 seconds
Fast version: 0.0001 seconds
Speedup: 7.70x faster

...
```

The speedup factors demonstrate that small code changes can have **dramatic performance impacts**.

## Learning Objectives

After reviewing these examples, you should understand:

1. Why vectorized operations are crucial for performance
2. The cost of growing collections in loops
3. How to identify inefficient code patterns
4. Best practices for writing performant data science code
5. When and how to use profiling tools

## Using in Positron

These examples are designed to be used in Positron IDE:

1. Open the files in Positron
2. Use the built-in profiler to analyze performance
3. Run individual functions to see the difference
4. Experiment with different data sizes
5. Use Copilot to help optimize your own code

## Further Reading

See **PERFORMANCE_GUIDE.md** for detailed explanations of each optimization pattern and general principles.

---

**Note**: Performance results will vary based on your hardware, dataset size, and system load. The important takeaway is the relative speedup, not the absolute times.
