# Use context managers to handle file operations
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# Always close files to free up system resources
# Using 'with' automatically closes the file when done
# Handle exceptions when working with files
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
# Use 'with' statement for file operations to ensure proper resource management
# Avoid using hard-coded file paths; use relative paths or configuration files
# Use appropriate file modes ('r', 'w', 'a', 'b', etc.) based on the operation
# Use 'os' and 'pathlib' for file path manipulations
import os
from pathlib import Path

# Example of using pathlib for file operations
file_path = Path("example.txt")
if file_path.is_file():
    with file_path.open("r") as file:
        content = file.read()
        print(content)
# Use 'os' for file operations that require system-level access
import os

# Example of using os for file operations
if os.path.exists("example.txt"):
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
# Use 'json' module for handling JSON files
import json

# Example of reading a JSON file
try:
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data)
except json.JSONDecodeError:
    print("Error decoding JSON. Please check the file format.")
# Use 'csv' module for handling CSV files
import csv

# Example of reading a CSV file
try:
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except csv.Error:
    print("Error reading CSV file. Please check the file format.")
# Use 'pickle' module for serializing and deserializing Python objects
import pickle

# Example of writing and reading a pickle file
data = {"key": "value"}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
# Use 'shutil' for high-level file operations like copying and moving files
import shutil

# Example of copying a file
shutil.copy("source.txt", "destination.txt")
# Use 'tempfile' for creating temporary files and directories
import tempfile

# Example of creating a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"This is a temporary file.")
    print(f"Temporary file created: {temp_file.name}")
# Use 'os' for file system operations like listing files in a directory
import os

# Example of listing files in a directory
files = os.listdir(".")
for file in files:
    print(file)
# Use 'pathlib' for modern file path manipulations
from pathlib import Path

# Example of using pathlib to list files in a directory
directory = Path(".")
for file in directory.iterdir():
    if file.is_file():
        print(file.name)
# Use 'os.path' for checking file existence and properties
import os.path

# Example of checking if a file exists
if os.path.exists("example.txt"):
    print("File exists.")
else:
    print("File does not exist.")
# Use 'os' for environment variables and system information
import os

# Example of getting an environment variable
home_directory = os.getenv("HOME", "Default Home Directory")
print(f"Home Directory: {home_directory}")
# Use 'os' for executing system commands
import os

# Example of executing a system command
os.system("echo Hello, World!")
# Use 'os' for file permissions and ownership
import os

# Example of changing file permissions
import stat

file_path = "example.txt"
os.chmod(
    file_path, stat.S_IRUSR | stat.S_IWUSR
)  # Set read and write permissions for the owner
# Example of getting file modification time
# Use 'os' for file timestamps
import os

file_path = "example.txt"
modification_time = os.path.getmtime(file_path)
print(f"File modification time: {modification_time}")
# Use 'os' for file size
import os

# Example of getting file size
file_size = os.path.getsize("example.txt")
print(f"File size: {file_size} bytes")
