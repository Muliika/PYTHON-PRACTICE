# Reading and writing files in Python is a fundamental skill that allows developers to interact with data stored on disk i.e handling data input and output. Python provides built-in functions and methods to read from and write to files, making it easy to work with text files, binary files, and more.


# Here's a brief overview of how to read and write files in Python:
# Opening a file:
# To read or write a file, you first need to open it using the built-in `open()` function. This function takes the file path and the mode as arguments. The mode can be 'r' for reading, 'w' for writing (which overwrites the file), 'a' for appending, and 'b' for binary mode.
def open_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content


# Example usage:
# content = open_file('example.txt')


# Reading from a file:
# You can read the entire content of a file using the `read()` method, or read line by line using the `readline()` or `readlines()` methods. The `readlines()` method returns a list of lines in the file.
def read_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


# Example usage:
# lines = read_file('example.txt')
# Writing to a file:
# To write to a file, you can use the `write()` method. If the file does not exist, it will be created. If it exists, the content will be overwritten unless you open the file in append mode ('a').
def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


# Example usage:
# write_file('example.txt', 'Hello, World!')
# Appending to a file:
# To append content to a file without overwriting the existing content, you can open the file in append mode ('a') and use the `write()` method.
def append_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)


# Example usage:
# append_to_file('example.txt', '\nAppended text.')
# Closing a file:
# When you are done with a file, it is a good practice to close it using the `close()` method. However, when using the `with` statement, the file is automatically closed when the block is exited, so you don't need to call `close()` explicitly.
# Example usage:
# file = open('example.txt', 'r')
# content = file.read()
# file.close()
# Error handling:
# When working with files, it's important to handle potential errors, such as file not found or permission denied. You can use try-except blocks to catch exceptions and handle them gracefully.
def read_file_with_error_handling(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
# content = read_file_with_error_handling('example.txt')
# The above functions provide a basic framework for reading and writing files in Python. You can expand upon these functions to handle specific use cases, such as reading and writing JSON or CSV files, or working with binary data. By mastering file I/O operations, you can effectively manage data in your Python applications.
