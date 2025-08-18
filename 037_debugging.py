# Python provides several techniques & tools to help you find and fix issues in your code.
# Here are some common debugging techniques in python:
# Print statements: Use print statements to output the values of variables and expressions during runtime. This helps you understand the state of your program and identify any issues.
# Using pdb (Python Debugger): pdb is a powerful debugger that allows you to step through your code, inspect variables, and set breakpoints. It's particularly useful for debugging complex programs or when you need to debug specific parts of your code.
# for example:

"""
import pdb

def add_numbers(a, b):
    pdb.set_trace()  # Set a breakpoint at the start of the function
    result = a + b
    return result

add_numbers(5, 10)
"""
# You can start the debugger by importing pdb and calling `pdb.set_trace()` at the desired location in your code. Once the debugger is started, you can use the following commands to step through your code: step, next, continue, and quit.

# Using logging: Python's built-in logging module provides a flexible and powerful way to log messages and events in your code. It allows you to configure the logging level, log format, and log destination. By using logging, you can easily track and debug your code, identify issues, and optimize performance.
# You can use logging messages to log messages at different levels (debug, info, warning, error, critical) and format them using the desired log format. For example:

"""
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_numbers(a, b):
    result = a + b
    logging.info(f'Adding {a} and {b} gives {result}')
    return result

add_numbers(5, 10)
"""
# This will log messages like: '2023-03-21 12:34:56 - INFO - Adding 5 and 10 gives 15' in the console.
# You can also specify and control the log destination (e.g., file, console, network) using the `logging.FileHandler` or `logging.StreamHandler` classes.

# Using assertions: Assertions are used to check if a condition is true at runtime. If the condition is false, an AssertionError is raised. Assertions can be used to validate input values, check program logic, and enforce best practices.
# You can use assertions to check conditions in your code and raise an AssertionError if the condition is not met. For example:


def add_numbers(a, b):
    assert isinstance(a, (int, float)), "The first argument must be a number"
    assert isinstance(b, (int, float)), "The second argument must be a number"
    result = a + b
    return result


add_numbers(5, 10)

# This will raise an AssertionError if the first argument is not a number or the second argument is not a number.

# Using pdb in IPython: IPython is a powerful interactive Python shell that provides a rich set of features, including support for debugging. You can use IPython's debugger (pdb) to step through your code, inspect variables, and set breakpoints.

# Debugger in IDEs: Many Integrated Development Environments (IDEs) support debugging Python code. You can use these IDEs to set breakpoints, step through your code, and inspect variables. Some popular IDE with debugging support include PyCharm, Visual Studio Code, and Jupyter Notebook.

# Unit testing and Test Driven Development (TDD): Unit testing is a methodology for writing and running tests for individual units of code. TDD helps you write code in a way that is easy to test and maintain. Unit tests are written using testing frameworks like pytest, unittest, or nose. By writing unit tests for your code, you can ensure that it behaves as expected and catch any bugs or issues early. For example:

# Code Review: Code reviews are a valuable way to improve code quality and collaboration. By reviewing and discussing code with other developers, you can identify potential issues, suggest improvements, and address any concerns.

# Static Analysis Tools: Static analysis tools can help you find potential issues in your code, such as unused variables, unused imports, and code smells. Tools like pylint, flake8, and band check can help you identify these issues and enforce best practices.
