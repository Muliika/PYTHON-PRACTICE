# sets in python are unordered collections of unique elements. They are mutable, meaning you can change their content after creation. Sets are often used to store collections of items where duplicates are not allowed.
# Sets are useful for various operations such as membership testing, intersection, union, and difference. They are commonly used in scenarios where you need to ensure that a collection contains only unique items.

# Example 1: Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Accessing elements in a set
print(1 in my_set)  # Output: True

# Modifying elements in a set
my_set.add(6)  # Adding an element
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.remove(2)  # Removing an element
print(my_set)  # Output: {1, 3, 4, 5, 6}
my_set.discard(3)  # Discarding an element (no error if not found)
my_set.clear()  # Clearing the set  # Output: set()
my_set.update({7, 8, 9})  # Adding multiple elements
print(my_set)  # Output: {7, 8, 9}
my_set.pop()  # Removing and returning an arbitrary element

# set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
print(set_a.difference(set_b))  # Output: {1, 2}

# Sets are handy in scenarios involving data analysis, database operations or algorithmic problem-solving.
