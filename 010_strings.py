# Strings in python are sequences of characters enclosed with single or double quotes. They can contain any printable ASCII characters. They can also include escape sequences for special characters. They are immutable, meaning once created, they cannot be changed.


# Creating strings
my_string = "Hello, World!"
print(my_string)
print(type(my_string))  # Output: <class 'str'>
print(len(my_string))  # Output: 13
# Accessing characters in a string
print(my_string[0])  # Output: H
print(my_string[2:5])  # Output: llo
# String concatenation
another_string = " How are you?"
concatenated_string = my_string + another_string
print(concatenated_string)  # Output: Hello, World! How are you?
# String repetition
repeated_string = my_string * 2
print(repeated_string)  # Output: Hello, World!Hello, World!
# String methods
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.replace("World", "Python"))  # Output: Hello, Python!
print(my_string.split(", "))  # Output: ['Hello', 'World!']
# Checking for substring
print("Hello" in my_string)  # Output: True
print("Python" in my_string)  # Output: False
# String formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Alice and I am 30 years old.
# Multiline strings
multiline_string = """This is a string
that spans multiple lines.
It can be useful for documentation."""
print(multiline_string)

# Escape sequences
# Escape sequences are used to include special characters in a string.
# Example:
escaped_string = (
    "This is a string with a newline character.\nAnd this is on a new line."
)
print(escaped_string)
# Common escape sequences
# \n - Newline
# \t - Tab
# \\ - Backslash
# \' - Single quote
# \" - Double quote
# Using escape sequences
escaped_string_with_quotes = 'He said, "Hello, World!"'
print(escaped_string_with_quotes)  # Output: He said, "Hello, World!"
escaped_string_with_tab = "Column1\tColumn2\tColumn3"
print(escaped_string_with_tab)  # Output: Column1    Column2    Column3
# String immutability
# Strings are immutable, meaning you cannot change a string in place.
try:
    my_string[0] = "h"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

# Instead, you can create a new string
new_string = "h" + my_string[1:]
print(new_string)  # Output: hello, World!
# String slicing
sliced_string = my_string[7:12]  # Slicing from index 7 to 12
print(sliced_string)  # Output: World
# String iteration
for char in my_string:
    print(char)

# String comparison
string1 = "apple"
string2 = "banana"
print(string1 < string2)  # Output: True (based on lexicographical order)
print(string1 > string2)  # Output: False

# String membership
print("H" in my_string)  # Output: True
print("h" in my_string)  # Output: False (case-sensitive)
# String join method
words = ["Python", "is", "fun"]
joined_string = " ".join(words)
print(joined_string)  # Output: Python is fun
# String find method
find_index = my_string.find("World")
print(find_index)  # Output: 7 (index of the first occurrence of "World")
# String count method
count = my_string.count("o")
print(count)  # Output: 3
# String startswith and endswith methods
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("World!"))  # Output: True
# String strip method
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: Hello, World!
# String isdigit method
print("12345".isdigit())  # Output: True
print("12345abc".isdigit())  # Output: False
# String isalpha method
print("Hello".isalpha())  # Output: True
print("Hello123".isalpha())  # Output: False
# String isalnum method
print("Hello123".isalnum())  # Output: True
print("Hello World!".isalnum())  # Output: False
# String isspace method
print("   ".isspace())  # Output: True
print("Hello, World!".isspace())  # Output: False
# String title method
print("hello world".title())  # Output: Hello World
