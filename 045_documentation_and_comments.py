# Documentation and comments play a crucial role in making code understandable and maintainable. Here are some best practices for writing effective documentation and comments in your code:
# Use Doc strings: Docstrings provide a concise and informative description of the purpose, functionality, and usage of a function, class, or module. They should be placed at the beginning of the relevant code block.
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b
# Use Inline Comments: Inline comments should be used to explain specific lines or blocks of code that may not be immediately clear. They should be concise and relevant.
def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of the input integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i  # Multiply result by the current number
    return result
# Use Meaningful Variable and Function Names: Choose descriptive names that convey the purpose of the variable or function. This reduces the need for excessive comments.
def calculate_area_of_circle(radius):
    """
    Calculates the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2
# Keep Comments Up-to-Date: Ensure that comments accurately reflect the current state of the code. Outdated comments can be misleading.
# Avoid Redundant Comments: Do not state the obvious. Comments should add value and provide insights that are not immediately clear from the code itself.
# Example of a redundant comment:
# Increment i by 1
# i += 1  # This comment is unnecessary
# Use Consistent Formatting: Follow a consistent style for writing comments and documentation throughout your codebase. This includes indentation, capitalization, and punctuation.
# Example of consistent formatting:
"""
def calculate_area_of_circle(radius):
    """
    Calculates the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.
    Returns:
    float: The area of the circle.
    """
    import math
    return math.pi * radius ** 2
"""
# By following these best practices, you can enhance the readability and maintainability of your code, making it easier for others (and yourself) to understand and work with it in the future.