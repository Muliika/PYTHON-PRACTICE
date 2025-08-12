# Creating iterators and generators in python allows you to define custom iterable objects that can be used with for loops and other iterable contexts.
# This is useful for managing memory efficiently and creating complex data structures.
# Example of creating a custom iterator using the iterator protocol
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
for num in my_iterator:
    print(num)  # Output: 4, 5, 6


# Example of an iterable that can be looped over multiple times
class MyIterableExample:
    def __iter__(self):
        return iter([7, 8, 9])


print("\nIterable vs Iterator example:")
my_iterable_example = MyIterableExample()
for num in my_iterable_example:
    print(num)  # Output: 7, 8, 9
# After the first loop, we can loop again
for num in my_iterable_example:
    print(num)  # Output: 7, 8, 9
# Example of an iterator that cannot be reused
my_iterator_example = iter([10, 11, 12])
for num in my_iterator_example:
    print(num)  # Output: 10, 11, 12
# After the first loop, the iterator is exhausted and cannot be reused
try:
    for num in my_iterator_example:
        print(num)  # This will not print anything, as the iterator is exhausted
except StopIteration:
    print("Iterator is exhausted and cannot be reused.")


# Output: Iterator is exhausted and cannot be reused.
# Summary:
# - An iterable is an object that can return an iterator using the `__iter__()` method.
# - An iterator is an object that implements the `__next__()` method and can be used to traverse through the elements of an iterable.
# - Iterables can be looped over multiple times, while iterators can only be traversed once.
# - After an iterator is exhausted, it cannot be reused unless a new iterator is created from the iterable.
# - Understanding these protocols is essential for creating custom iterable objects and for using built-in data structures effectively.
# This lesson provides a foundation for working with iterators and generators in Python, which are powerful tools for managing data flow and memory usage in applications.
# Generators are a simpler way to create iterators using the `yield` keyword.
# Example of a generator function
def my_generator():
    yield 10
    yield 11
    yield 12


print("\nGenerator example:")
for num in my_generator():
    print(num)  # Output: 10, 11, 12
    # The generator function creates a generator object, which can be iterated over multiple times using a for loop.
# Generators are more memory-efficient than creating a list of values, as they yield one value at a time.
# They are particularly useful for processing large datasets or streams of data where you don't need to store all values in memory at once.
# This lesson provides a foundation for working with iterators and generators in Python, which are powerful tools for managing data flow and memory usage in applications.
# Understanding these concepts is essential for creating custom iterable objects and for using built-in data structures effectively.
