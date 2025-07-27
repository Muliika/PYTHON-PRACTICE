# Decorators allow you to modify the behavior of a function or class method.
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result

    return wrapper


@decorator
def say_hello(name):
    print(f"Hello, {name}!")


# Using the decorated function
say_hello("Alice")


# Output:
# Before the function call
# Hello, Alice!
# After the function call
# Decorators can also take arguments
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return decorator_repeat


@repeat(3)
def greet(name):
    print(f"Greetings, {name}!")


# Using the decorated function
greet("Bob")


# Output:
# Greetings, Bob!
# Greetings, Bob!
# Greetings, Bob!
# Decorators can be used with class methods as well
class MyClass:
    def __init__(self, value):
        self.value = value

    @decorator
    def display_value(self):
        print(f"The value is: {self.value}")


# Using the decorated class method
obj = MyClass(42)
obj.display_value()


# Output:
# Before the function call
# The value is: 42
# After the function call
# Decorators can also be used to modify class methods
def class_decorator(cls):
    class Wrapped(cls):
        def new_method(self):
            print("This is a new method added by the decorator.")

    return Wrapped


@class_decorator
class AnotherClass:
    def original_method(self):
        print("This is the original method.")


# Using the decorated class
another_obj = AnotherClass()
another_obj.original_method()
another_obj.new_method()


# Output:
# This is the original method.
# This is a new method added by the decorator.
# Decorators can also be used to cache results
def cache(func):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Using the cached Fibonacci function
print(fibonacci(10))  # Output: 55
# Using the cached Fibonacci function again
print(fibonacci(10))  # Output: 55 (cached result)


# Decorators can also be used to enforce access control
def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_admin:
            raise PermissionError("You must be an admin to perform this action.")
        return func(user, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

    @require_admin
    def delete_account(self):
        print(f"Account {self.name} deleted.")


# Using the decorated method
admin_user = User("Alice", is_admin=True)
admin_user.delete_account()  # Output: Account Alice deleted.
# Using the decorated method with a non-admin user
non_admin_user = User("Bob", is_admin=False)
try:
    non_admin_user.delete_account()  # Raises PermissionError
except PermissionError as e:
    print(e)


# Output: You must be an admin to perform this action.
# Decorators can also be used to log function calls
def log(func):
    def wrapper(*args, **kwargs):
        print(
            f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result

    return wrapper


@log
def add(a, b):
    return a + b


# Using the decorated function
result = add(3, 5)


# Output:
# Calling function 'add' with arguments: (3, 5) and keyword arguments: {}
# Function 'add' returned: 8
# Decorators can also be used to enforce type checking
def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument {arg} is not of type {expected_type.__name__}"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(int)
def multiply(a, b):
    return a * b


# Using the decorated function
result = multiply(4, 5)  # Output: 20
# Using the decorated function with a type error
try:
    result = multiply("4", 5)  # Raises TypeError
    print(result)
except TypeError as e:
    print(e)


# Output: Argument 4 is not of type int
# Decorators can also be used to enforce preconditions
def precondition(condition, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not condition(*args, **kwargs):
                raise ValueError(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@precondition(lambda x: x > 0, "x must be greater than 0")
def square(x):
    return x * x


# Using the decorated function
try:
    result = square(5)  # Output: 25
    print(result)
    result = square(-3)  # Raises ValueError
    print(result)
except ValueError as e:
    print(e)


    # Output: x must be greater than 0
# Decorators can also be used to enforce postconditions
def postcondition(condition, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not condition(result):
                raise ValueError(message)
            return result

        return wrapper

    return decorator


@postcondition(lambda x: x % 2 == 0, "x must be even")
def multiply_by_two(x):
    return x * 2


# Using the decorated function
try:
    result = multiply_by_two(3)  # Raises ValueError
    print(result)
except ValueError as e:
    print(e)


    # Output: x must be even
# Decorators can also be used to enforce invariants
def invariant(condition, message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not condition():
                raise ValueError(message)
            return func(*args, **kwargs)

        return wrapper

    return decorator


@invariant(lambda: True, "Invariant condition failed")
def always_pass():
    return "This function always passes."


# Using the decorated function
result = always_pass()  # Output: This function always passes.
print(result)
# Decorators can also be used to enforce resource management
import contextlib


@contextlib.contextmanager
def managed_resource(resource):
    try:
        print(f"Acquiring resource: {resource}")
        yield resource
    finally:
        print(f"Releasing resource: {resource}")


# Using the context manager
with managed_resource("Database Connection") as resource:
    print(f"Working with resource: {resource}")


# Output:
# Acquiring resource: Database Connection
# Working with resource: Database Connection
# Releasing resource: Database Connection
# Decorators can also be used to enforce cleanup actions
def cleanup(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            print("Cleaning up resources...")

    return wrapper


@cleanup
def create_file(filename):
    print(f"Creating file: {filename}")
    # Simulate file creation
    return f"File {filename} created."


# Using the decorated function
result = create_file("example.txt")
# Output:
# Creating file: example.txt
# File example.txt created.
# Cleaning up resources...
