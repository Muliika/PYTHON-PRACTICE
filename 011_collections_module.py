# The collections module in Python provides additional data structures like Counter, defaultdict, and OrderedDict that are extensions of built-in data types.
# These data structures provide additional functionalities and improve the performance of certain operations.

# Example 1: Counter
from collections import Counter

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
counter = Counter(my_list)
print(counter)  # Output: Counter({4: 5, 3: 3, 2: 2, 1: 1, 5: 1})
# The Counter class counts the occurrences of each element in the list and returns a dictionary-like object.

# Example 2: defaultdict
from collections import defaultdict

my_dict = defaultdict(int)  # Default value is 0 for int
my_dict["a"] += 1
my_dict["b"] += 2
print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
# The defaultdict class allows you to specify a default value for keys that do not exist in the dictionary.

# Example 3: OrderedDict
from collections import OrderedDict

my_dict = (
    OrderedDict()
)  # An OrderedDict maintains the order of elements as they are added
my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3
print(my_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# The OrderedDict class remembers the order in which keys were first inserted, unlike a regular dictionary

# Example 4: namedtuple
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)  # Output: Point(x=10, y=20)
# The namedtuple function creates a tuple subclass with named fields, making the code more readable and self-documenting.

# Example 5: deque
from collections import deque

my_deque = deque([1, 2, 3])
my_deque.append(4)
my_deque.appendleft(0)
print(my_deque)  # Output: deque([0, 1, 2, 3, 4])
# The deque class provides a double-ended queue that allows for fast appends and pops from both ends of the queue.

# Example 6: ChainMap
from collections import ChainMap

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain = ChainMap(dict1, dict2)
print(chain)  # Output: ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
# The ChainMap class groups multiple dictionaries together, allowing you to treat them as a single mapping.

# Example 7: UserDict
from collections import UserDict


class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)


my_dict = MyDict()
my_dict["a"] = 1  # Output: Setting a to 1
my_dict["b"] = 2  # Output: Setting b to 2
print(my_dict)  # Output: {'a': 1, 'b': 2}
# The UserDict class is a wrapper around the built-in dictionary that allows you to create custom dictionary-like objects with additional functionality.

# Example 8: UserList
from collections import UserList


class MyList(UserList):
    def append(self, item):
        print(f"Appending {item}")
        super().append(item)


my_list = MyList([1, 2, 3])
my_list.append(4)  # Output: Appending 4
print(my_list)  # Output: [1, 2, 3, 4]
# The UserList class is a wrapper around the built-in list that allows you to create custom list-like objects with additional functionality.

# Example 9: UserString
from collections import UserString


class MyString(UserString):
    def __add__(self, other):
        print(f"Concatenating {self.data} and {other}")
        return super().__add__(other)


my_string = MyString("Hello")
result = my_string + " World"  # Output: Concatenating Hello and  World
print(result)  # Output: Hello World
# The UserString class is a wrapper around the built-in string that allows you to create custom string-like objects with additional functionality.

# Example 10: OrderedDict with move_to_end
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict.move_to_end("b")  # Move 'b' to the end
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('c', 3), ('b', 2)])
# The move_to_end method allows you to move an existing key to either end of the OrderedDict, maintaining the order of elements.

# Example 11: Counter with most_common
from collections import Counter

my_counter = Counter("abracadabra")
most_common = my_counter.most_common(2)  # Get the two most common elements
print(most_common)  # Output: [('a', 5), ('b', 2)]
# The most_common method returns a list of the n most common elements and their counts from the Counter object.

# Example 12: defaultdict with a custom default factory
from collections import defaultdict


def factory():
    return "default_value"


my_defaultdict = defaultdict(factory)
my_defaultdict["a"] = 1
print(my_defaultdict["a"])  # Output: 1

# Example 13: deque with a maxlen
my_deque = deque(maxlen=3)  # Set a maximum length of 3
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
my_deque.append(4)  # This will remove the oldest element (1)
print(my_deque)  # Output: deque([2, 3, 4], maxlen=3)

# Example 14: ChainMap with multiple dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain = ChainMap(dict1, dict2)
chain["b"] = 5  # Update the value of 'b' in both dictionaries
print(chain)  # Output: ChainMap({'a': 1, 'b': 5}, {'b': 3, 'c': 4})
# The ChainMap allows you to update keys in the first dictionary, affecting all dictionaries in the chain.

# Example 15: UserDict with custom methods
from collections import UserDict


class MyDict(UserDict):
    def get_keys(self):
        return list(self.data.keys())

    def get_values(self):
        return list(self.data.values())


my_dict = MyDict({"a": 1, "b": 2})
print(my_dict.get_keys())  # Output: ['a', 'b']
print(my_dict.get_values())  # Output: [1, 2]

# Example 16: UserList with custom methods
from collections import UserList


class MyList(UserList):
    def get_length(self):
        return len(self.data)

    def get_first(self):
        return self.data[0] if self.data else None


my_list = MyList([1, 2, 3])
print(my_list.get_length())  # Output: 3
print(my_list.get_first())  # Output: 1

# Example 17: UserString with custom methods
from collections import UserString


class MyString(UserString):
    def to_upper(self):
        return self.data.upper()

    def to_lower(self):
        return self.data.lower()

    def reverse(self):
        return self.data[::-1]


my_string = MyString("Hello")
print(my_string.to_upper())  # Output: HELLO
print(my_string.to_lower())  # Output: hello
print(my_string.reverse())  # Output: olleH
# The UserString class allows you to create custom string-like objects with additional methods for string manipulation.

# Example 18: Using deque as a stack
from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)  # Using deque as a stack
print(stack.pop())  # Output: 3

# Example 19: Using deque as a queue
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)  # Using deque as a queue
print(queue.popleft())  # Output: 1

# Example 20: Using deque as a priority queue
from collections import deque

priority_queue = deque()
priority_queue.append((1, "low"))
priority_queue.append((3, "high"))
priority_queue.append((2, "medium"))  # Using deque as a priority queue
priority_queue = sorted(priority_queue)  # Sort by priority
print(priority_queue)  # Output: [(1, 'low'), (2, 'medium'), (3, 'high')]
# The collections module provides a variety of data structures that can be used to improve the performance and readability of your code.
# Each of these data structures has its own unique features and use cases, making them powerful tools for Python developers.
# They can be used to solve a wide range of problems, from counting occurrences of elements to managing ordered collections and custom data types.
# Understanding and utilizing these data structures can greatly enhance your programming skills and efficiency in Python.
