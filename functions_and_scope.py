# Functions in python are blocks of reuseable code that perform a specific task. They allow you to break your code into smaller manageable tasks.


def greet(name):
    """Function to greet a person."""
    return "Hello, " + name + "!"


print(greet("Alice"))


# Scope refers to the visibility and accessibility of variables within different parts of your code

global_var = 10


def my_func():
    local_var = 20
    print("Inside function ", local_var)


my_func()
print("Outside function ", global_var)
