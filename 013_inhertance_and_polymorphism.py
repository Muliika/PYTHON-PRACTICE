# Inheritance and polymorphism are two fundamental concepts in object-oriented programming (OOP) that allow for code reuse and flexibility in designing software systems. They enable you to create a hierarchy of classes and define relationships between them, making it easier to manage complexity and promote code organization.
# Inheritance allows a class (the child or derived class) to inherit attributes and methods from another class (the parent or base class). This means that the child class can reuse code from the parent class, reducing redundancy and promoting code reuse. The child class can also extend or override the behavior of the parent class by adding new attributes or methods or modifying existing ones.
# Polymorphism allows objects of different classes to be treated as instances of the same class through a common interface. This means that you can use methods or attributes defined in a parent class on objects of child classes, even if those child classes have their own specific implementations. Polymorphism promotes flexibility and allows for dynamic behavior in your code, enabling you to write more generic and reusable code.
# In Python, inheritance is implemented using class definitions, where a class can inherit from one or more parent classes. Polymorphism is achieved through method overriding and duck typing, where the behavior of an object is determined by its methods and attributes rather than its specific class type.
# Example of inheritance and polymorphism in Python:
class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creating instances of the Dog and Cat classes
my_dog = Dog()
my_cat = Cat()
# Using polymorphism to call the speak method on different animal objects
print(my_dog.speak())  # Output: Woof!
print(my_cat.speak())  # Output: Meow!
# In this example, we have a base class `Animal` with a method `speak`. The `Dog` and `Cat` classes inherit from `Animal` and override the `speak` method to provide their specific implementations. When we call the `speak` method on instances of `Dog` and `Cat`, we get different outputs based on the specific class implementation, demonstrating polymorphism.

# there are 2 main types of inheritance in Python: single inheritance and multiple inheritance. Single inheritance occurs when a class inherits from one parent class, while multiple inheritance occurs when a class inherits from multiple parent classes. Python supports both types of inheritance, allowing for flexible class hierarchies.
# Inheritance allows you to create a new class that is a modified version of an existing class, enabling you to build upon existing functionality without rewriting code. This promotes code reuse and helps maintain a clean and organized codebase.

# there are 2 main types of polymorphism in python: method overriding and method overloading. Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. This allows the child class to change or extend the behavior of the inherited method. Method overloading, on the other hand, allows a class to have multiple methods with the same name but different parameters, enabling different behaviors based on the arguments passed.


# Method overriding example:
class Parent:
    def greet(self):
        return "Hello from Parent"


class Child(Parent):
    def greet(self):
        return "Hello from Child"


# Creating instances of Parent and Child classes
parent = Parent()
child = Child()
# Using method overriding to call the greet method on different objects
print(parent.greet())  # Output: Hello from Parent
print(child.greet())  # Output: Hello from Child


# Method overloading example:
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


# Creating an instance of MathOperations class
math_ops = MathOperations()
# Using method overloading to call the add method with different parameters
print(
    math_ops.add(1, 2)
)  # Output: 3 (this will raise an error because the second add method overrides the first one)
print(math_ops.add(1, 2, 3))  # Output: 6
# In Python, method overloading is not supported in the same way as in some other languages. Instead, you can achieve similar functionality using default arguments or variable-length arguments (using `*args` and `**kwargs`). This allows you to define a single method that can handle different numbers of parameters.
# In this example, we have a base class `Parent` with a method `greet`. The `Child` class inherits from `Parent` and overrides the `greet` method to provide its own implementation. When we call the `greet` method on instances of `Parent` and `Child`, we get different outputs based on the specific class implementation, demonstrating method overriding.
