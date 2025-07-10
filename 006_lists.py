# In python, a list is a versatile data structure that can hold a collection of items. Lists are mutable meaning they can be modified after creation.

# Example 1

my_list = [1, 2, 3, 4, 5]

# Accessing elements in a list
print(my_list[0])  # Output: 1
print(my_list[2:4])  # Output: 3:4

for item in my_list:
    print(item)


# Modifying a list

# Example 2
my_list.append(6)  # Adding an element to the end of the list
my_list.extend([7, 8])  # Adding multiple elements to the end of the list
my_list.insert(2, 10)  # Inserting an element at a specific position
my_list[3] = 15  # Replacing an element at a specific position
del my_list[1]  # Deleting an element at a specific position
my_list.remove(10)  # Removing the first occurrence of a specific value
print(my_list)


# List operations
# lists support various operations such as concatenation(+), repetition(*), and membership testing(in).
# Example 3

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2  # Concatenation
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
repeated_list = list1 * 3  # Repetition
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
length = len(list1)  # Length of the list
print(length)  # Output: 3
print(2 in list1)  # Membership testing


# list methods
# Python provides several built-in methods for lists that allow you to manipulate them easily. Here are some commonly used methods:
# - `append()`: Adds an element to the end of the list.
# - `extend()`: Adds multiple elements to the end of the list.
# - `insert()`: Inserts an element at a specific position.
# - `remove()`: Removes the first occurrence of a specific value.
# - `pop()`: Removes and returns the element at a specific position (default is the last element).
# - `index()`: Returns the index of the first occurrence of a specific value.
# - `count()`: Returns the number of occurrences of a specific value.
# - `sort()`: Sorts the list in ascending order.
# - `reverse()`: Reverses the order of the elements in the list.

# Example 4
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list.append(11)  # Adds 11 to the end of the list
my_list.extend([12, 13])  # Adds 12 and 13 to the end of the list
my_list.insert(0, 0)  # Inserts 0 at the beginning of the list
my_list.remove(5)  # Removes the first occurrence of 5 from the list
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]
my_list.pop()  # Removes and returns the last element (13)
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
index_of_6 = my_list.index(6)  # Returns the index of the first occurrence of 6
print(index_of_6)  # Output: 5
count_of_2 = my_list.count(2)  # Returns the number of occurrences of 2
print(count_of_2)  # Output: 1
my_list.sort()  # Sorts the list in ascending order
print(my_list)  # Output: [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
my_list.reverse()  # Reverses the order of the elements in the list
print(my_list)  # Output: [12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0]

# lists are incredibly versatile and widely used in python for various purposes, such as storing collections of data, implementing stacks and queues, and more. They are a fundamental part of the language and provide a powerful way to work with ordered collections of items.

# Example 5: List Comprehensions
# List comprehensions provide a concise way to create lists in Python. They consist of brackets containing an expression followed by a `for` clause, and can also include optional `if` clauses.
squared_numbers = [
    x**2 for x in range(10)
]  # Creates a list of squared numbers from 0 to 9
print(squared_numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Example 6: Nested Lists
# Lists can contain other lists, allowing for the creation of multi-dimensional data structures.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1])  # Output: [4, 5, 6]
print(nested_list[1][2])  # Output: 6 (accessing an element in a nested list)

# Example 7: List Slicing
# Slicing allows you to access a portion of a list by specifying a start and end index.
sliced_list = my_list[2:5]  # Gets elements from index 2to 4 (exclusive)
print(sliced_list)  # Output: [2, 3, 4]


# Example 8: List Copying
# You can create a shallow copy of a list using the `copy()` method or slicing.
copied_list = my_list.copy()  # Creates a shallow copy of the list
print(copied_list)  # Output: [12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0]


# Example 9: List Sorting with Custom Key
# You can sort a list using a custom key function.
def custom_sort(x):
    return -x  # Sort in descending order


my_list.sort(key=custom_sort)  # Sorts the list in descending order
print(my_list)  # Output: [12, 11, 10, 9, 8, 7, 6, 4, 3, 2, 1, 0]


# Example 10: List Filtering
# You can filter a list using a list comprehension with a condition.
filtered_list = [
    x for x in my_list if x % 2 == 0
]  # Gets only even numbers from the list
print(filtered_list)  # Output: [12, 10, 8, 6, 4, 2, 0]


# Example 11: List Unpacking
# You can unpack a list into variables.
a, b, c, *rest = (
    my_list  # Unpacks the first three elements into a, b, c and the rest into a list
)
print(a, b, c)  # Output: 12 11 10
print(rest)  # Output: [9, 8, 7, 6, 4, 3, 2, 1, 0] (the rest of the elements)


# Example 12: List as a Stack
# Lists can be used as stacks, where you can add elements to the end and remove them from the end.
stack = []
stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.append(3)  # Push 3 onto the stack
print(stack)  # Output: [1, 2, 3]
print(stack.pop())  # Pop the last element (3) from the stack
print(stack)  # Output: [1, 2] (the stack after popping)


# Example 13: List as a Queue
# Lists can also be used as queues, where you can add elements to the end and remove them from the front.
queue = []
queue.append(1)  # Enqueue 1
queue.append(2)  # Enqueue 2
queue.append(3)  # Enqueue 3
print(queue)  # Output: [1, 2, 3]
print(queue.pop(0))  # Dequeue the first element (1)
print(queue)  # Output: [2, 3] (the queue after dequeuing)


# Example 14: List with Mixed Data Types
# Lists in Python can hold elements of different data types.
mixed_list = [1, "two", 3.0, True, None]
print(mixed_list)  # Output: [1, 'two', 3.0, True, None]


# Example 15: List with Duplicates
# Lists can contain duplicate elements.
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
print(duplicate_list)  # Output: [1, 2, 2, 3, 4, 4, 5]


# Example 16: List with Different Data Structures
# Lists can contain different data structures, such as tuples and dictionaries.
tuple_in_list = [(1, 2), (3, 4), (5, 6)]
print(tuple_in_list)  # Output: [(1, 2), (3, 4), (5, 6)]
dict_in_list = [{"name": "Alice"}, {"name": "Bob"}]
print(dict_in_list)  # Output: [{'name': 'Alice'}, {'name': 'Bob'}]


# Example 17: List with List Comprehensions
# You can use list comprehensions to create lists based on existing lists.
squared_list = [x**2 for x in range(5)]  # Creates a list of squared numbers from 0 to 4
print(squared_list)  # Output: [0, 1, 4, 9, 16, 25]


# Example 18: List with Conditional Logic
# You can use conditional logic within list comprehensions to filter elements.
filtered_squared_list = [
    x**2 for x in range(10) if x % 2 == 0
]  # Squares only even numbers
print(filtered_squared_list)  # Output: [0, 4, 16, 36, 64]


# Example 19: List with Enumerate
# You can use the `enumerate()` function to get both the index and value of elements in a list.
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 12
# Index: 1, Value: 11
# Index: 2, Value: 10
# Index: 3, Value: 9
# Index: 4, Value: 8
# Index: 5, Value: 7
# Index: 6, Value: 6
# Index: 7, Value: 4
# Index: 8, Value: 3
# Index: 9, Value: 2
# Index: 10, Value: 1
# Index: 11, Value: 0


# Example 20: List with Zip
# You can use the `zip()` function to combine multiple lists into a list of tuples.
list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
zipped_list = list(zip(list_a, list_b))  # Combines the two lists into a list of tuples
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
