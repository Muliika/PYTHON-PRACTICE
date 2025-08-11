# The concepts of iterable and iterator are fundamental for understanding how looping constructs like for loops work and how to create custom iterable objects. They define the behavior of objects when they are used in a context that requires iteration.
# iterable protocol:
# An iterable is an object that implements the `__iter__()` method, which returns an iterator object.
# An iterable can be a list, tuple, string, or any custom object that implements this method.
# Example
class MyIterable:
    def __iter__(self):
        self.data = [1, 2, 3]
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


print("Iterable example:")
my_iterable = MyIterable()
for item in my_iterable:
    print(item)  # Output: 1, 2, 3


# iterator protocol:
# An iterator is an object that implements the `__next__()` method and the `StopIteration` exception.
# An iterator can be created from an iterable by calling its `__iter__()` method.
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


print("\nIterator example:")
my_iterator = MyIterator([4, 5, 6])
for item in my_iterator:
    print(item)  # Output: 4, 5, 6


# iterable vs iterator:
# An iterable can be looped over multiple times, while an iterator can only be traversed once.
# After an iterator is exhausted, it cannot be reused unless a new iterator is created from the iterable.
# Example of iterable vs iterator
class MyIterableExample:
    def __iter__(self):
        return iter([7, 8, 9])


print("\nIterable vs Iterator example:")
my_iterable_example = MyIterableExample()
for item in my_iterable_example:
    print(item)  # Output: 7, 8, 9
# After the first loop, we can loop again
for item in my_iterable_example:
    print(item)  # Output: 7, 8, 9
# Example of iterator that cannot be reused
my_iterator_example = iter([10, 11, 12])
for item in my_iterator_example:
    print(item)  # Output: 10, 11, 12
# After the first loop, the iterator is exhausted and cannot be reused
try:
    for item in my_iterator_example:
        print(item)  # This will not print anything, as the iterator is exhausted
except StopIteration:
    print("Iterator is exhausted and cannot be reused.")
# Output: Iterator is exhausted and cannot be reused.
# Summary:
# - An iterable is an object that can return an iterator using the `__iter__()` method.
# - An iterator is an object that implements the `__next__()` method and can be used to traverse through the elements of an iterable.
# - Iterables can be looped over multiple times, while iterators can only be traversed once.
# - After an iterator is exhausted, it cannot be reused unless a new iterator is created from the iterable.
# - Understanding these protocols is essential for creating custom iterable objects and for using built-in data structures effectively.


# Lazy Evaluation
# Lazy evaluation is a programming technique where an expression is not evaluated until its value is actually needed. This can improve performance and reduce memory usage, especially when dealing with large datasets or expensive computations.
# In Python, lazy evaluation can be achieved using generators, which allow you to iterate over a sequence of values without storing them all in memory at once.
# Example of lazy evaluation using a generator
def lazy_evaluation_example():
    for i in range(10):
        yield i * 2  # This value is computed only when requested


print("\nLazy Evaluation example:")
lazy_gen = lazy_evaluation_example()
for item in lazy_gen:
    print(item)  # Output: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# Lazy evaluation is particularly useful when working with large datasets or when the computation of values is expensive.
# It allows you to generate values on-the-fly, reducing memory usage and improving performance.

# Built in iterables and iterators
# Python provides several built-in iterables and iterators, such as lists, tuples, strings, and dictionaries. These objects implement the iterable protocol and can be used in loops or with functions that require an iterable.
# Example of built-in iterables and iterators
built_in_iterables = [1, 2, 3, 4, 5]
print("\nBuilt-in Iterables example:")
for item in built_in_iterables:
    print(item)  # Output: 1, 2, 3, 4, 5
# You can also create iterators from these built-in iterables using the `iter()` function
built_in_iterator = iter(built_in_iterables)
print("\nBuilt-in Iterator example:")
for item in built_in_iterator:
    print(item)  # Output: 1, 2, 3, 4, 5


# Example of using built-in iterators with functions
def process_items(iterator):
    for item in iterator:
        print(f"Processing item: {item}")


process_items(built_in_iterator)  # Output: Processing item: 1, 2, 3, 4, 5
# Example of using built-in iterators with list comprehensions
squared_items = [x**2 for x in built_in_iterables]
print("\nBuilt-in Iterators with List Comprehension example:")
print(squared_items)  # Output: [1, 4, 9, 16, 25]
# Example of using built-in iterators with the `map` function
mapped_items = list(map(lambda x: x * 2, built_in_iterables))
print("\nBuilt-in Iterators with Map Function example:")
print(mapped_items)  # Output: [2, 4, 6, 8, 10]
# Example of using built-in iterators with the `filter` function
filtered_items = list(filter(lambda x: x > 2, built_in_iterables))
print("\nBuilt-in Iterators with Filter Function example:")
print(filtered_items)  # Output: [3, 4, 5]
