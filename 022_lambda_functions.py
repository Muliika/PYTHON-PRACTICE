# Lambda functions also known as anonymous functions, are a way to create small, one-time use functions in Python. They are defined using the `lambda` keyword and can take any number of arguments but only have one expression. Lambda functions are often used for short operations that are not reused elsewhere in the code.
# They are particularly useful in functional programming contexts, such as when used with functions like `map`, `filter`, and `reduce`.
# Example of a lambda function:
add = lambda x, y: x + y
# This function takes two arguments, `x` and `y`, and returns their sum.
# Lambda functions can be used in places where you might use a regular function, but they are typically used for short, throwaway functions that are not reused elsewhere in the code.
# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
# This will square each number in the list `numbers` and return a new list `squared_numbers`.
# Lambda functions can also be used in conjunction with `filter` to filter elements from a list:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# This will return a new list containing only the even numbers from the original list `numbers`.
# Lambda functions are often used in places where you need a small function for a short period of time, such as in sorting or filtering operations, without the need to formally define a function using `def`.
# Lambda functions can also be used in conjunction with `reduce` to apply a function cumulatively to the items of an iterable:
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
# This will return the product of all numbers in the list `numbers`.
# Lambda functions are a powerful feature in Python that allows for concise and readable code, especially when dealing with small, one-off functions that do not require a full function definition.
# Lambda functions can also be used in sorting operations, where you can specify a custom key for sorting:
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
sorted_people = sorted(people, key=lambda person: person["age"])
# This will sort the list of dictionaries `people` by the `age` key.
# Lambda functions can also be used in list comprehensions for more complex operations:
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
# This will create a new list containing the squares of only the even numbers from the original list `numbers`.
# In summary, lambda functions are a powerful and flexible feature in Python that allow for concise and readable code, especially when dealing with small, one-off functions that do not require a full function definition. They are commonly used in functional programming contexts and can be combined with other functions like `map`, `filter`, and `reduce` to perform operations on iterables efficiently.
# Lambda functions can also be used in event handling, such as in GUI applications or web frameworks, where you might want to define a small function to handle an event without the need for a full function definition.
