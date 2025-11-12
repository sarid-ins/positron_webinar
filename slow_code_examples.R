# Examples of Slow and Inefficient Code Patterns in R
# ======================================================
#
# This file demonstrates common performance issues in R data science code.
# Each example includes both inefficient and optimized versions.

library(dplyr)
library(data.table)


# Example 1: Inefficient Loop-based Vector Growth
# ------------------------------------------------

process_vector_slow <- function(n) {
  # SLOW: Growing vector in a loop
  # R has to reallocate memory on each iteration
  # Time complexity: O(n²)
  result <- c()
  for (i in 1:n) {
    result <- c(result, i^2)
  }
  return(result)
}

process_vector_fast <- function(n) {
  # FAST: Pre-allocate vector or use vectorized operations
  # Time complexity: O(n)
  result <- (1:n)^2
  return(result)
}


# Example 2: Inefficient Data Frame Row-by-Row Operations
# --------------------------------------------------------

process_dataframe_slow <- function(df) {
  # SLOW: Using a loop to compute on each row
  # Extremely inefficient in R
  result <- df
  for (i in 1:nrow(df)) {
    result$total[i] <- result$value1[i] + result$value2[i]
    result$average[i] <- (result$value1[i] + result$value2[i]) / 2
  }
  return(result)
}

process_dataframe_fast <- function(df) {
  # FAST: Vectorized operations
  # Can be 100-1000x faster
  result <- df
  result$total <- result$value1 + result$value2
  result$average <- (result$value1 + result$value2) / 2
  return(result)
}


# Example 3: Inefficient apply() vs Vectorization
# ------------------------------------------------

calculate_with_apply_slow <- function(df) {
  # SLOW: Using apply when vectorization is possible
  # apply() still loops internally
  df$result <- apply(df, 1, function(row) {
    as.numeric(row['value1']) * 2 + as.numeric(row['value2']) * 3
  })
  return(df)
}

calculate_vectorized_fast <- function(df) {
  # FAST: Direct vectorized operations
  df$result <- df$value1 * 2 + df$value2 * 3
  return(df)
}


# Example 4: Inefficient Data Frame Concatenation
# ------------------------------------------------

bind_rows_slow <- function(n) {
  # SLOW: Growing data frame in a loop with rbind
  # Causes repeated memory reallocation
  result <- data.frame()
  for (i in 1:n) {
    new_row <- data.frame(id = i, value = rnorm(1))
    result <- rbind(result, new_row)
  }
  return(result)
}

bind_rows_fast <- function(n) {
  # FAST: Create list first, then combine
  # Or use data.table which is optimized for this
  row_list <- lapply(1:n, function(i) {
    data.frame(id = i, value = rnorm(1))
  })
  result <- do.call(rbind, row_list)
  return(result)
}


# Example 5: Inefficient Filtering Without dplyr
# -----------------------------------------------

filter_dataframe_slow <- function(df, threshold) {
  # SLOW: Manual subsetting with multiple operations
  indices <- c()
  for (i in 1:nrow(df)) {
    if (df$value1[i] > threshold && df$value2[i] > threshold) {
      indices <- c(indices, i)
    }
  }
  return(df[indices, ])
}

filter_dataframe_fast <- function(df, threshold) {
  # FAST: Vectorized logical indexing or dplyr
  result <- df[df$value1 > threshold & df$value2 > threshold, ]
  return(result)
}


# Example 6: Inefficient Repeated Subsetting
# -------------------------------------------

compute_with_subsetting_slow <- function(df) {
  # SLOW: Repeatedly subsetting the same data
  # Each subset operation has overhead
  result <- sum(df[df$category == "A", ]$value) +
            sum(df[df$category == "B", ]$value) +
            sum(df[df$category == "C", ]$value)
  return(result)
}

compute_with_grouping_fast <- function(df) {
  # FAST: Group once and summarize
  result <- sum(tapply(df$value, df$category, sum))
  return(result)
}


# Example 7: Inefficient Use of ifelse in Loops
# ----------------------------------------------

categorize_slow <- function(values) {
  # SLOW: Using a loop with if statements
  result <- character(length(values))
  for (i in 1:length(values)) {
    if (values[i] < 0) {
      result[i] <- "negative"
    } else if (values[i] == 0) {
      result[i] <- "zero"
    } else {
      result[i] <- "positive"
    }
  }
  return(result)
}

categorize_fast <- function(values) {
  # FAST: Vectorized ifelse or case_when
  result <- ifelse(values < 0, "negative",
                   ifelse(values == 0, "zero", "positive"))
  return(result)
}


# Example 8: Inefficient String Operations
# -----------------------------------------

paste_strings_slow <- function(strings) {
  # SLOW: Growing string in a loop
  result <- ""
  for (s in strings) {
    result <- paste(result, s, sep = ", ")
  }
  return(result)
}

paste_strings_fast <- function(strings) {
  # FAST: Use paste with collapse
  result <- paste(strings, collapse = ", ")
  return(result)
}


# Example 9: Inefficient Matrix Operations
# -----------------------------------------

matrix_multiply_slow <- function(A, B) {
  # SLOW: Manual matrix multiplication with loops
  # Very slow and error-prone
  n <- nrow(A)
  m <- ncol(B)
  p <- ncol(A)
  result <- matrix(0, n, m)
  
  for (i in 1:n) {
    for (j in 1:m) {
      for (k in 1:p) {
        result[i, j] <- result[i, j] + A[i, k] * B[k, j]
      }
    }
  }
  return(result)
}

matrix_multiply_fast <- function(A, B) {
  # FAST: Use built-in matrix multiplication
  # Optimized with BLAS/LAPACK
  return(A %*% B)
}


# Example 10: Inefficient Data Frame Column Addition
# ---------------------------------------------------

add_columns_slow <- function(df, n_cols) {
  # SLOW: Adding columns one at a time in a loop
  for (i in 1:n_cols) {
    df[, paste0("col", i)] <- rnorm(nrow(df))
  }
  return(df)
}

add_columns_fast <- function(df, n_cols) {
  # FAST: Create all columns at once
  new_cols <- replicate(n_cols, rnorm(nrow(df)), simplify = FALSE)
  names(new_cols) <- paste0("col", 1:n_cols)
  result <- cbind(df, as.data.frame(new_cols))
  return(result)
}


# Benchmark Function
# ------------------

benchmark_example <- function(slow_func, fast_func, ..., description = "") {
  # Utility function to compare performance of two implementations
  
  cat("\n", description, "\n")
  cat(strrep("-", nchar(description)), "\n")
  
  # Warm-up
  invisible(slow_func(...))
  invisible(fast_func(...))
  
  # Benchmark slow version
  slow_time <- system.time(slow_result <- slow_func(...))[["elapsed"]]
  
  # Benchmark fast version
  fast_time <- system.time(fast_result <- fast_func(...))[["elapsed"]]
  
  cat(sprintf("Slow version: %.4f seconds\n", slow_time))
  cat(sprintf("Fast version: %.4f seconds\n", fast_time))
  
  if (fast_time > 0) {
    speedup <- slow_time / fast_time
    cat(sprintf("Speedup: %.2fx faster\n", speedup))
  }
  
  return(c(slow_time = slow_time, fast_time = fast_time))
}


# Main Benchmarking Script
# -------------------------

if (interactive() || !exists("being_sourced")) {
  cat("Performance Comparison Examples in R\n")
  cat(strrep("=", 50), "\n")
  
  # Test Example 1: Vector Growth
  benchmark_example(
    process_vector_slow,
    process_vector_fast,
    10000,
    description = "1. Vector Growth"
  )
  
  # Test Example 2: Data Frame Operations
  set.seed(42)
  df <- data.frame(
    value1 = runif(10000),
    value2 = runif(10000)
  )
  benchmark_example(
    process_dataframe_slow,
    process_dataframe_fast,
    df,
    description = "2. Data Frame Row Operations"
  )
  
  # Test Example 3: apply vs Vectorization
  set.seed(42)
  df <- data.frame(
    value1 = runif(10000),
    value2 = runif(10000)
  )
  benchmark_example(
    calculate_with_apply_slow,
    calculate_vectorized_fast,
    df,
    description = "3. apply() vs Vectorization"
  )
  
  # Test Example 4: Data Frame Concatenation
  benchmark_example(
    bind_rows_slow,
    bind_rows_fast,
    1000,
    description = "4. Data Frame Concatenation (rbind)"
  )
  
  # Test Example 5: Filtering
  set.seed(42)
  df <- data.frame(
    value1 = runif(10000),
    value2 = runif(10000)
  )
  benchmark_example(
    filter_dataframe_slow,
    filter_dataframe_fast,
    df,
    0.5,
    description = "5. Data Frame Filtering"
  )
  
  # Test Example 6: Repeated Subsetting
  set.seed(42)
  df <- data.frame(
    category = sample(c("A", "B", "C"), 10000, replace = TRUE),
    value = runif(10000)
  )
  benchmark_example(
    compute_with_subsetting_slow,
    compute_with_grouping_fast,
    df,
    description = "6. Repeated Subsetting vs Grouping"
  )
  
  # Test Example 7: Categorization
  set.seed(42)
  values <- rnorm(100000)
  benchmark_example(
    categorize_slow,
    categorize_fast,
    values,
    description = "7. Loop-based vs Vectorized Categorization"
  )
  
  # Test Example 8: String Concatenation
  strings <- paste0("item", 1:10000)
  benchmark_example(
    paste_strings_slow,
    paste_strings_fast,
    strings,
    description = "8. String Concatenation"
  )
  
  # Test Example 9: Matrix Multiplication
  set.seed(42)
  A <- matrix(rnorm(100 * 100), 100, 100)
  B <- matrix(rnorm(100 * 100), 100, 100)
  benchmark_example(
    matrix_multiply_slow,
    matrix_multiply_fast,
    A,
    B,
    description = "9. Matrix Multiplication"
  )
  
  # Test Example 10: Adding Columns
  set.seed(42)
  df <- data.frame(id = 1:1000)
  benchmark_example(
    add_columns_slow,
    add_columns_fast,
    df,
    10,
    description = "10. Adding Multiple Columns"
  )
  
  cat("\n", strrep("=", 50), "\n")
  cat("Benchmark completed!\n")
}
