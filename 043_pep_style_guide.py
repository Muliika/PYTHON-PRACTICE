# Pep is the official style guide for python code. It provides guidelines and best practices for writing clean, readable and consistent python code. Adhering to PEP 8 improves code maintainability, readability and collaboration among developers.


# Here are some key points from the PEP 8 Stylr Guide:
# Indentation: Use 4 spaces per indentation level. Avoid using tabs.
def example_function():
    if True:
        print("This line is indented with 4 spaces")
    else:
        print("This line is also indented with 4 spaces")


# Whitespaces: Use spaces around operators and after commas, but not directly inside parentheses, brackets or braces.
# Avoid trailing whitespace at the end of lines.
# Line Length: Limit all lines to a maximum of 79 characters. For docstrings or comments, limit lines to 72 characters.
# If a line exceeds the limit, consider breaking it into multiple lines using parentheses or backslashes.
def long_function_name(var_one, var_two, var_three, var_four):
    return var_one + var_two + var_three + var_four


# Imports: Imports should usually be on separate lines. Group imports in the following order: standard library imports, related third-party imports, and local application/library-specific imports.
# Use absolute imports whenever possible.
import os
import sys

import requests
from mymodule import myfunction


# Naming Conventions: Use lowercase with words separated by underscores for function and variable names (e.g., my_function). Use CapitalizedWords for class names (e.g., MyClass). Constants should be in all uppercase with words separated by underscores (e.g., MY_CONSTANT).
class MyClass:
    def __init__(self, my_variable):
        self.my_variable = my_variable


MY_CONSTANT = 42


# Comments: Use comments to explain the purpose of code, especially for complex or non-obvious sections. Use complete sentences and proper punctuation. Avoid obvious comments that do not add value.
# Use docstrings to describe the purpose and usage of modules, classes, and functions.
def my_function():
    """This function does something important."""
    pass


# Avoid using inline comments unless necessary.
# Whitespace in Expressions and Statements: Avoid extraneous whitespace.
# Surround binary operators with a single space on both sides (e.g., a = b + c).
# Do not use spaces around the '=' sign when used to indicate a keyword argument or a default parameter value.
# Use blank lines to separate logical sections of code.


# Function and methods definitions: Use a single blank line to separate function and method definitions within a class. Use two blank lines to separate top-level function and class definitions.
def first_function():
    pass


def second_function():
    pass


class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass


# String Quotes: Use single quotes (' ') or double quotes (" ") consistently for string literals. Choose one style and stick to it throughout your codebase.
single_quoted = "This is a single-quoted string"
double_quoted = "This is a double-quoted string"
# Avoid using triple quotes for single-line strings.
# Avoid using backslashes to continue lines. Instead, use parentheses to wrap long expressions.
total = first_variable + second_variable + third_variable + fourth_variable


# Documentation strings: Use triple double quotes (""" """) for docstrings. The first line should be a short summary of the function's purpose. If there are more details, add them after a blank line.
def example_function_with_docstring(param1, param2):
    """
    This function demonstrates a proper docstring.

    Parameters:
    param1 (int): The first parameter.
    param2 (int): The second parameter.

    Returns:
    int: The sum of param1 and param2.
    """
    return param1 + param2


# Avoid using single quotes for docstrings.
# Avoid using inline comments in docstrings.
# Conditional Expressions: Use parentheses to clarify complex conditional expressions. Avoid using multiple logical operators in a single line without parentheses.
if (condition_one and condition_two) or (condition_three and condition_four):
    do_something()
# Avoid using nested conditional expressions that are hard to read.
# Use explicit comparisons to None, True, or False (e.g., if variable is None).
# Avoid using implicit boolean checks (e.g., if variable).
if my_variable is not None:
    print("my_variable is not None")
# Avoid using double negatives in conditional expressions.
# Avoid using the 'is' operator for comparing values (use '==' instead).
if my_variable == 42:
    print("my_variable is equal to 42")
# Avoid using the 'not' operator in complex expressions (use positive logic instead).
if my_variable > 0:
    print("my_variable is positive")
# Avoid using the 'and' and 'or' operators in complex expressions (use nested if statements instead).
if condition_one:
    if condition_two:
        do_something()
# Avoid using the 'if-else' operator in complex expressions (use nested if statements instead).
if condition_one:
    do_something()
else:
    do_something_else()


# Following the guidelines in PEP 8 helps ensure that your Python code is clean, readable, and consistent with the broader Python community's standards. This makes it easier for others (and yourself) to understand and maintain the code over time. While PEP 8 provides a solid foundation for writing Python code, it's important to remember that these are guidelines rather than strict rules. There may be situations where deviating from PEP 8 is justified for the sake of clarity or specific project requirements. The key is to prioritize readability and maintainability while adhering to the general principles outlined in PEP 8.# Tools like `flake8`, `pylint`, and `black` can help enforce PEP 8 compliance in your codebase.# Regularly reviewing and refactoring your code to align with PEP 8 can lead to a more professional and polished codebase.# Consistency is key; choose a style and stick to it throughout your project.# Adhering to PEP 8 not only improves the quality of your code but also fosters a positive coding culture within your team or community.# Remember, the goal of PEP 8 is to make your code more readable and maintainable, so always prioritize clarity over strict adherence to the guidelines.# Happy coding!
