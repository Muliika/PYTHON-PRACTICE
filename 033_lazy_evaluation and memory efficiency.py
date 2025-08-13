# Lazy evaluation and memory efficiency are essential concepts in python especially when dealing with large dataset or infinite streams of data. They are frequently achieved through techniques like generators and iterators.
# Lazy evaluation:
# Lazy evaluation is a programming technique where an expression is not evaluated until its value is actually needed. This can improve performance and reduce memory usage, especially when dealing with large datasets or expensive computations. It normally used with generators.

# Memory efficiency:
# Memory efficiency refers to the optimal use of memory resources especially when working with large datasets or infinite streams of data. Lazy evaluation and iterators help to achieve this by generating values on-the-fly, reducing memory usage and improving performance.
# Techniques like lazy evaluation, streaming and incremental processing are some of the ways to achieve memory efficiency in python.

# Example:
# Let's create a simple generator function to generate values on-the-fly.


def lazy_evaluation_example():
    for i in range(10):
        yield i * 2


# We can iterate over the generated values using a for loop.

lazy_gen = lazy_evaluation_example()
for num in lazy_gen:
    print(num)
    # Output: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
    # As the values are generated on-the-fly, the memory usage is reduced.
# This technique is particularly useful when working with large datasets or when the computation of values is expensive.
# It allows you to process data in chunks, reducing memory usage and improving performance.
