# Performance Optimization Guide

This guide documents common performance issues in data science code and how to fix them. Examples are provided in both Python and R.

## Overview

Performance optimization is crucial in data science when working with large datasets. Small changes in code patterns can result in dramatic performance improvements - often 10x to 1000x faster execution times.

## Common Performance Anti-Patterns

### 1. Row-by-Row DataFrame Operations

**Problem**: Iterating through DataFrames row-by-row is one of the most common and severe performance issues.

**Python Example**:
```python
# ❌ SLOW - O(n) with high constant factor
for idx in range(len(df)):
    df.loc[idx, 'total'] = df.loc[idx, 'value1'] + df.loc[idx, 'value2']

# ✅ FAST - Vectorized, O(n) with low constant factor
df['total'] = df['value1'] + df['value2']
```

**R Example**:
```r
# ❌ SLOW
for (i in 1:nrow(df)) {
  df$total[i] <- df$value1[i] + df$value2[i]
}

# ✅ FAST
df$total <- df$value1 + df$value2
```

**Why it matters**: Vectorized operations are optimized at the C level and process entire arrays at once, while loops involve Python/R interpreter overhead for each iteration.

**Performance Impact**: 100-1000x speedup for large datasets

---

### 2. Growing Collections in Loops

**Problem**: Appending to vectors/lists in loops causes repeated memory reallocation.

**Python Example**:
```python
# ❌ SLOW - O(n²) time complexity
result = []
for i in range(n):
    result.append(i**2)
result = np.array(result)

# ✅ FAST - O(n) time complexity
result = np.arange(n) ** 2
```

**R Example**:
```r
# ❌ SLOW - O(n²) time complexity
result <- c()
for (i in 1:n) {
  result <- c(result, i^2)
}

# ✅ FAST - O(n) time complexity
result <- (1:n)^2
```

**Why it matters**: Each append/concatenation creates a new object and copies all previous data, leading to quadratic time complexity.

**Performance Impact**: 100-1000x speedup for large datasets

---

### 3. Repeated DataFrame Concatenation

**Problem**: Concatenating DataFrames in a loop is similar to growing vectors - each operation copies all previous data.

**Python Example**:
```python
# ❌ SLOW - O(n²)
result = pd.DataFrame()
for df in dfs:
    result = pd.concat([result, df])

# ✅ FAST - O(n)
result = pd.concat(dfs, ignore_index=True)
```

**R Example**:
```r
# ❌ SLOW - O(n²)
result <- data.frame()
for (i in 1:n) {
  result <- rbind(result, new_row)
}

# ✅ FAST - O(n)
row_list <- lapply(1:n, function(i) new_row)
result <- do.call(rbind, row_list)
```

**Performance Impact**: 50-500x speedup

---

### 4. Inefficient String Concatenation

**Problem**: Repeated string concatenation with `+` or `paste()` creates many intermediate string objects.

**Python Example**:
```python
# ❌ SLOW - O(n²)
result = ""
for item in items:
    result += item + ", "

# ✅ FAST - O(n)
result = ", ".join(items)
```

**R Example**:
```r
# ❌ SLOW
result <- ""
for (s in strings) {
  result <- paste(result, s, sep = ", ")
}

# ✅ FAST
result <- paste(strings, collapse = ", ")
```

**Performance Impact**: 50-200x speedup for large strings

---

### 5. Using Loops Instead of Vectorization

**Problem**: Loops involve interpreter overhead on each iteration, while vectorized operations are compiled and optimized.

**Python Example**:
```python
# ❌ SLOW
result = [x**2 for x in values]

# ✅ FAST (for NumPy arrays)
result = values ** 2
```

**R Example**:
```r
# ❌ SLOW
result <- apply(df, 1, function(row) row['value'] * 2)

# ✅ FAST
result <- df$value * 2
```

**Performance Impact**: 10-100x speedup

---

### 6. Inefficient Filtering

**Problem**: Using loops to filter data instead of vectorized boolean indexing.

**Python Example**:
```python
# ❌ SLOW
filtered = []
for idx, row in df.iterrows():
    if row['value'] > threshold:
        filtered.append(row)
result = pd.DataFrame(filtered)

# ✅ FAST
result = df[df['value'] > threshold]
```

**R Example**:
```r
# ❌ SLOW
indices <- c()
for (i in 1:nrow(df)) {
  if (df$value[i] > threshold) {
    indices <- c(indices, i)
  }
}
result <- df[indices, ]

# ✅ FAST
result <- df[df$value > threshold, ]
```

**Performance Impact**: 50-500x speedup

---

### 7. Using Lists Instead of Generators (Python)

**Problem**: List comprehensions load all data into memory at once, which is wasteful if you only need to iterate once.

**Python Example**:
```python
# ❌ SLOW - Loads all into memory
numbers = [x**2 for x in range(1000000)]
total = sum(numbers)

# ✅ FAST - Computes on-the-fly
total = sum(x**2 for x in range(1000000))
```

**Memory Impact**: Can reduce memory usage from O(n) to O(1)

---

### 8. Global Variable Access (Python)

**Problem**: Accessing global variables is slower than local variables in Python.

**Python Example**:
```python
# ❌ SLOW
global_counter = 0
def process(items):
    global global_counter
    for item in items:
        global_counter += item

# ✅ FAST
def process(items):
    local_counter = 0
    for item in items:
        local_counter += item
    return local_counter
```

**Performance Impact**: 10-30% speedup in tight loops

---

### 9. Inefficient Dictionary Operations (Python)

**Problem**: Using list membership checks instead of dictionary operations.

**Python Example**:
```python
# ❌ SLOW - O(n) for each 'in' check
result = {}
keys_list = []
for item in items:
    if item in keys_list:  # O(n) operation
        result[item] += 1
    else:
        result[item] = 1
        keys_list.append(item)

# ✅ FAST - O(1) for dictionary operations
result = {}
for item in items:
    result[item] = result.get(item, 0) + 1
```

**Performance Impact**: 100-1000x speedup for large datasets

---

### 10. Manual Matrix Operations

**Problem**: Implementing matrix operations manually instead of using optimized linear algebra libraries.

**R Example**:
```r
# ❌ SLOW - Manual loops
result <- matrix(0, n, m)
for (i in 1:n) {
  for (j in 1:m) {
    for (k in 1:p) {
      result[i, j] <- result[i, j] + A[i, k] * B[k, j]
    }
  }
}

# ✅ FAST - Built-in with BLAS/LAPACK
result <- A %*% B
```

**Performance Impact**: 100-10000x speedup

---

## General Optimization Principles

### 1. **Vectorize Operations**
Always prefer vectorized operations over loops when working with arrays and DataFrames.

### 2. **Pre-allocate Memory**
If you must use loops, pre-allocate the result container with the final size.

### 3. **Use Built-in Functions**
Built-in functions and library methods are often highly optimized (e.g., `sum()`, `join()`, `%*%`).

### 4. **Choose the Right Data Structure**
- Use NumPy arrays for numerical operations
- Use dictionaries for lookups (not lists)
- Use sets for membership testing
- Consider data.table in R for large datasets

### 5. **Profile Before Optimizing**
Use profiling tools to identify actual bottlenecks:
- Python: `cProfile`, `line_profiler`, `memory_profiler`
- R: `Rprof()`, `profvis`, `bench::mark()`

### 6. **Avoid Premature Optimization**
Focus on correctness first, then optimize the parts that are actually slow.

---

## Testing Performance

Both example files (`slow_code_examples.py` and `slow_code_examples.R`) include benchmark functions that you can run:

**Python**:
```bash
python slow_code_examples.py
```

**R**:
```r
source("slow_code_examples.R")
```

These will demonstrate the performance differences between slow and fast implementations.

---

## Additional Resources

### Python
- [NumPy Performance Tips](https://numpy.org/doc/stable/user/performance.html)
- [Pandas Performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
- [Python Profiling Guide](https://docs.python.org/3/library/profile.html)

### R
- [Advanced R - Performance](https://adv-r.hadley.nz/perf-improve.html)
- [Efficient R Programming](https://csgillespie.github.io/efficientR/)
- [data.table Performance](https://rdatatable.gitlab.io/data.table/)

---

## Summary

The key to writing performant data science code is:
1. **Avoid loops** when vectorized operations are available
2. **Pre-allocate** memory when loops are necessary
3. **Use built-in functions** and optimized libraries
4. **Profile your code** to find actual bottlenecks
5. **Choose appropriate data structures** for your use case

Remember: Small changes in code patterns can lead to dramatic performance improvements!
