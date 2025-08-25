# Effective memory management is essential for writing efficient and reliable software:
# Here are some tips to help you manage memory effectively in your Python programs.
# Use built in data structures wisely:
# Python's built-in data structures (like lists, sets, and dictionaries) are optimized for performance and memory usage.
# Choose the right data structure for your needs to minimize memory overhead.
# Example: Use a set for membership testing instead of a list.
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # O(1) average time complexity
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # O(n) time complexity
# Avoid unnecessary data copies:
# Be mindful of operations that create copies of data, such as slicing lists or using certain functions.
# Use references instead of copies when possible to save memory.
original_list = [1, 2, 3, 4, 5]
sliced_list = original_list[:]  # Creates a copy
reference_list = original_list  # Creates a reference


# Use generators and iterators:
# Generators and iterators allow you to iterate over large datasets without loading everything into memory at once.
# Use generator expressions or the `yield` keyword to create memory-efficient iterators.
def generate_numbers(n):
    for i in range(n):
        yield i


for number in generate_numbers(1000000):
    if number < 5:
        print(number)
    else:
        break
# Close resources properly:
# Always close files, network connections, and other resources when you're done with them.
# Use context managers (the `with` statement) to ensure resources are released automatically.
with open("example.txt", "r") as file:
    data = file.read()
# File is automatically closed when the block is exited
# Avoid Circular References:
# Circular references occur when objects reference each other in a loop, preventing Python's garbage collector from reclaiming memory.
# Use weak references (from the `weakref` module) to break circular references when necessary.
import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node1.next = weakref.ref(node2)  # Use weak reference to avoid circular reference
node2.next = weakref.ref(node1)
# Be cautious when designing data structures or using caching mechanisms to avoid unintentional circular references as they can lead to memory leaks.
# Monitor memory usage:
# Use tools like `tracemalloc`, `memory_profiler`, or `objgraph` to monitor memory usage and identify memory leaks in your application.
import tracemalloc

tracemalloc.start()
# Your code here
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
tracemalloc.stop()
# Regularly profiling your code can help you identify memory-intensive operations and optimize them.
# Use built in functions and libraries:
# Python's standard library provides many functions and modules that are optimized for performance and memory usage.
# Leverage these built-in tools instead of reinventing the wheel to ensure efficient memory management.
import array

# Use array module for memory-efficient storage of basic data types instead of lists
int_array = array.array("i", [1, 2, 3, 4, 5])
print(int_array)
# By following these memory management tips, you can write more efficient Python programs that make better use of system resources and avoid common pitfalls related to memory usage.
