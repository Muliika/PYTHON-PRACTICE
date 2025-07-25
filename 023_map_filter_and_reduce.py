# map, filter, and reduce are built-in functions in Python that allow for functional programming styles. They can be used to apply a function to each item in an iterable (like a list) or to filter items based on a condition.
# The `map` function applies a given function to each item in an iterable and returns a map object (which can be converted to a list). It is useful for transforming data.
# The `filter` function filters items in an iterable based on a condition defined by a function and returns a filter object (which can also be converted to a list). It is useful for selecting items that meet certain criteria.
# The `reduce` function, from the `functools` module, applies a rolling computation to sequential pairs of items in an iterable, reducing it to a single value. It is useful for cumulative operations like summing or multiplying all items.
# Example of using `map`:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# This will square each number in the list `numbers` and return a new list `squared_numbers`.
# Example of using `filter`:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# This will return a new list containing only the even numbers from the original list `numbers`.
# Example of using `reduce`:
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
# This will return the product of all numbers in the list `numbers`.
# These functions can be combined with lambda functions for concise and readable code.
# Lambda functions can also be used in sorting operations, where you can specify a custom key for sorting:
