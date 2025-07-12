# Dictionaries in python are unordered collections of key-value pairs. They are mutable, meaning you can change their content after creation. Dictionaries are often used to store data that is associated with a unique key.
# They are useful for representing structured data, such as JSON objects or database records.

# Creating a dictionary
# Example 1
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
}

# Accessing elements in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])  # Output: 30

# Modifying elements in a dictionary

my_dict["age"] = 31  # Changing the age
print(my_dict["age"])  # Output: 31

# Adding a new key-value pair
my_dict["occupation"] = "Engineer"
print(
    my_dict
)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}


print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'occupation'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'Engineer'])
print(
    my_dict.items()
)  # Output: dict_items([('name', 'Alice'), ('age', 31), ('occupation', 'Engineer')])
print(my_dict.get("name"))  # Output: Alice
print(
    my_dict.pop("age")
)  # Output: 31 (removes 'age' from the dictionary and returns its value)
print(
    my_dict.update({"city": "Los Angeles", "country": "USA"})
)  # Adds new key-value pairs


# Dictionaries are normally used for representing structured data, such as user profiles, configuration settings, or any data that can be represented as key-value pairs.
# They are useful for mapping unique identifiers (keys) to associated values, allowing for efficient data retrieval and manipulation.
# Dictionaries are also handy for passing named arguments to functions or for storing intermediate results in computations.
# Dictionaries are versatile data structures that offer efficient key-based access to values. They are widely used for various purposes including data processing, configuration management, and more.

# Example 2: Dictionary with Mixed Data Types
mixed_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "friends": ["Bob", "Charlie"],
}
print(
    mixed_dict
)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_student': True, 'friends': ['Bob', 'Charlie']}


# Example 3: Nested Dictionaries
nested_dict = {
    "person": {
        "name": "Alice",
        "age": 30,
        "address": {"city": "New York", "zip": "10001"},
    },
    "job": {"title": "Engineer", "company": "Tech Corp"},
}

print(nested_dict["person"]["address"]["city"])  # Output: New York
# Example 4: Dictionary with List Comprehensions
# You can use dictionary comprehensions to create dictionaries based on existing data.
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# Example 5: Dictionary with Default Values
from collections import defaultdict

default_dict = defaultdict(int)  # Default value is 0 for missing keys
default_dict["a"] = 1
default_dict["b"] += 2  # Adds 2 to the default value of 'b'
print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# Example 6: Dictionary with Multiple Data Types
multi_type_dict = {
    "integer": 42,
    "string": "hello",
    "float": 3.14,
    "list": [1, 2, 3],
    "tuple": (4, 5),
}
print(
    multi_type_dict
)  # Output: {'integer': 42, 'string': 'hello', 'float': 3.14, 'list': [1, 2, 3], 'tuple': (4, 5)}
