# Tuples in python are similar to lists but are immutable, meaning they cannot be modified after creation. They are often used to group related data together.

# Creating a tuple
# Example 1
my_tuple = (1, 2, 3, 4, 5, "a", "b", "c")

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2:5])  # Output: (3, 4, 5)
for item in my_tuple:
    print(item)

# Tuples cannot be modified, so we cannot add, remove, or change elements.
# However, we can perform some operations similar to lists.
# Tuple packing and unpacking

# Tuple packing is the process of creating a tuple by grouping multiple values together.
# Tuple unpacking is the process of extracting values from a tuple into separate variables.

# Example 2
packed_tuple = (1, 2, 3)
a, b, c = packed_tuple  # Unpacking the tuple into variables
print(a, b, c)  # Output: 1 2 3

# use cases of tuples
# Tuples are commonly used for returning multiple values from a function.
# They are also used to represent fixed collections of items where immutability is desired, such as coordinates, RGB values, or database records.


# Example 3
def get_coordinates():
    return (10.0, 20.0)  # Returning a tuple of coordinates


x, y = get_coordinates()  # Unpacking the coordinates into variables

print(x, y)  # Output: 10.0 20.0

# Example 4: Tuple with Mixed Data Types
mixed_tuple = (1, "two", 3.0, True, None)
print(mixed_tuple)  # Output: (1, 'two', 3.0, True, None)

# Example 5: Tuple with Nested Structures
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(nested_tuple)  # Output: ((1, 2), (3, 4), (5, 6))

# Example 6: Tuple with Single Element
# To create a tuple with a single element, you need to include a comma after the element
single_element_tuple = (42,)  # Note the comma
print(single_element_tuple)  # Output: (42,)

# Example 7: Tuple with Multiple Data Types
multi_type_tuple = (1, "hello", 3.14, [1, 2, 3], (4, 5))
print(multi_type_tuple)  # Output: (1, 'hello', 3.14, [1, 2, 3], (4, 5))

# Example 8: Tuple with Duplicates
duplicate_tuple = (1, 2, 2, 3, 4, 4, 5)
print(duplicate_tuple)  # Output: (1, 2, 2, 3, 4, 4, 5)

# Example 9: Tuple with Different Data Structures
tuple_with_list = (1, 2, [3, 4], (5, 6))
print(tuple_with_list)  # Output: (1, 2, [3, 4], (5, 6))

# Example 10: Tuple with List Comprehensions
# You can use tuple comprehensions to create tuples based on existing data.
squared_tuple = tuple(
    x**2 for x in range(5)
)  # Creates a tuple of squared numbers from 0 to 4
print(squared_tuple)  # Output: (0, 1, 4, 9, 16, 25)
