# Profiling and benchmarking is for analysing and measuring the performance of your code, identifying bottlenecks and optimizing critical sections to improve overall efficiency.
# Profiling
# This involves analysing the runtime behaviour of your code to identify which parts are consuming the mmost time or resources.
# Python provides s everal built-in and thrid party tools for profiling code, including cProfile, line_profiler and memory_profiler.
# cProfile is a built-in profiler that provides a detailed report of function calls, execution time and other statistics.
# Example of using cProfile to profile a simple function:
import cProfile
import io
import pstats


def example_function():
    total = 0
    for i in range(10000):
        total += i**2
    return total


# Create a cProfile object
pr = cProfile.Profile()
# Enable profiling
pr.enable()
# Call the function to be profiled
example_function()
# Disable profiling
pr.disable()
# Create a stream to hold the profiling results
s = io.StringIO()
# Create a Stats object from the profiling data
ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
# Print the profiling results
ps.print_stats()
print(s.getvalue())

# Line Profiling:
# This tool allows you to profile individual lines of code within a function, providing more granular insights into performance.
# To use line_profiler, you need to install it first (pip install line_profiler) and then use the @profile decorator on the functions you want to profile.
# Example of using line_profiler:
from line_profiler import LineProfiler


def another_example_function():
    total = 0
    for i in range(10000):
        total += i**2
    return total


lp = LineProfiler()
lp.add_function(another_example_function)
lp.enable_by_count()
another_example_function()
lp.disable_by_count()
lp.print_stats()

# Memory Profiling:
# This tool helps you track memory usage of your code, identifying memory leaks and optimizing memory-intensive operations.
# The memory_profiler package provides a @profile decorator to measure memory usage line by line.
# Example of using memory_profiler:
from memory_profiler import profile


@profile
def memory_example_function():
    total = 0
    for i in range(10000):
        total += i**2
    return total


memory_example_function()

# Benchmarking
# This involves measuring the execution time of specific code snippets or functions to compare different implementations or optimizations.
# Python's timeit module is commonly used for benchmarking, allowing you to run code multiple times and get accurate timing results.
# Example of using timeit to benchmark a function:
import timeit


def benchmark_function():
    total = 0
    for i in range(10000):
        total += i**2


# Benchmark the function using timeit
execution_time = timeit.timeit(benchmark_function, number=100)
print(f"Execution time over 100 runs: {execution_time} seconds")
# In this example, the benchmark_function is executed 100 times, and the total execution time is printed.
# You can adjust the number parameter to change how many times the function is executed for benchmarking.
# By using profiling and benchmarking tools, you can gain insights into the performance of your code and make informed decisions about optimizations and improvements.
# Remember to install any third-party packages (line_profiler and memory_profiler) using pip if you haven't already.
# Note: To see the memory profiling output, you need to run the script with the -m memory_profiler option, like this:
# python -m memory_profiler 040_profiling_and_benchmarking.py
# This will display the memory usage line by line for the decorated function.

# Best practices for profiling and benchmarking:
# 1. Profile and benchmark in a controlled environment to minimize external factors affecting performance.
# 2. Use representative data and workloads to get accurate measurements.
# 3. Focus on optimizing critical sections of code that have the most significant impact on overall performance.
# 4. Regularly profile and benchmark your code as it evolves to ensure that performance remains optimal.
# 5. Document and share profiling and benchmarking results with your team to facilitate collaboration and knowledge sharing.
# 6. Use visualization tools to help interpret profiling data and identify bottlenecks more easily.
# 7. Combine profiling and benchmarking with other performance optimization techniques, such as algorithm improvements and code refactoring.
# 8. Be cautious of premature optimization; focus on clear performance issues identified through profiling.
# 9. Consider the trade-offs between performance, readability, and maintainability when optimizing code.
# 10. Stay updated with the latest profiling and benchmarking tools and techniques to leverage new features and improvements.# By following these best practices, you can effectively use profiling and benchmarking to enhance the performance of your codebase.
