# Tyr except blocks also known as exception handling allow to handle errors and exceptions gracefully in Python. They provide a way to anticipate and manage potential errors that may occur during the execution of a program, ensuring that the program can continue running or exit gracefully without crashing.

# Basic structure of try-except blocks:
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")

# Handling specific exceptions:
try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
except Exception as e:
    # Code to handle any other exception
    print(f"An unexpected error occurred: {e}")

# Catching multiple exceptions:
try:
    # Code that may raise an exception
    result = int("not a number")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    # Code to handle multiple exceptions
    print(f"An error occurred: {e}")
# Using finally block:
try:
    # Code that may raise an exception
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    # Code to handle the exception
    print(f"File not found: {e}")
finally:
    # Code that will always execute, regardless of whether an exception occurred
    print("Closing the file.")
    file.close() if "file" in locals() else None

# Using else block:
try:
    # Code that may raise an exception
    result = 10 / 2  # This will not raise an exception
except ZeroDivisionError as e:
    # Code to handle the exception
    print(f"An error occurred: {e}")
else:
    # Code that will execute if no exception was raised
    print(f"Result is: {result}")


# Raising exceptions manually:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


try:
    result = divide(10, 0)  # This will raise a ValueError
except ValueError as e:
    print(f"An error occurred: {e}")


# Custom exception classes:
class CustomError(Exception):
    """Custom exception class for specific error handling."""

    pass


def risky_operation():
    raise CustomError("Something went wrong in the risky operation.")


try:
    risky_operation()  # This will raise CustomError
except CustomError as e:
    print(f"Custom error occurred: {e}")


# Using context managers with try-except blocks:
class FileHandler:
    """Context manager for file handling."""

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_value}")


try:
    with FileHandler("example.txt") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found: {e}")
# Using try-except blocks to handle exceptions in file operations
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found: {e}")
