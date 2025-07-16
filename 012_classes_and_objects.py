# classes and objects are fundamental concepts in object-oriented programming (OOP). They allow us to create custom data structures and define their behavior. They allow you model real-world entities as objects with attributes(data) and methods(behavior).

# A class is a blueprint/template for creating objects. It defines a set of attributes and methods that the objects created from the class will have. An object is an instance of a class, meaning it is created based on the class definition.


# Exmaple of a class and object in Python:
class Dog:
    # Attributes
    def __init__(self, name, breed):
        self.name = name  # instance variable for the dog's name
        self.breed = breed  # instance variable for the dog's breed

    # Method
    def bark(self):
        return f"{self.name} says Woof!"


# Creating an object (instance) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
# Accessing attributes and methods of the object
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Golden Retriever
print(my_dog.bark())  # Output: Buddy says Woof!
# In this example, we defined a class `Dog` with an `__init__` method that initializes the attributes `name` and `breed`. The `bark` method defines the behavior of the dog. We then created an instance of the `Dog` class called `my_dog`, which has its own unique attributes and can call its methods.
# Classes and objects allow for encapsulation, inheritance, and polymorphism, which are key principles of object-oriented programming. Encapsulation allows you to bundle data and methods together, inheritance allows you to create new classes based on existing ones, and polymorphism allows you to use objects of different classes interchangeably if they share a common interface.
# Classes and objects are essential for organizing code, promoting reusability, and modeling complex systems in a more intuitive way.
# the __init_ method is a special method in Python that is called when an object is created from a class. It allows you to initialize the attributes of the object with specific values. The `self` parameter refers to the instance of the class itself, allowing you to access its attributes and methods.
# The `__init__` method is often referred to as the constructor in other programming languages, and it is used to set up the initial state of an object when it is created. It can take additional parameters to customize the object's attributes during instantiation.
# The `self` parameter is a reference to the current instance of the class, allowing you to access its attributes and methods. It is a convention in Python to use `self` as the first parameter in instance methods, but you can technically use any name.
# The `__init__` method is not required in a class, but it is commonly used to ensure that objects are initialized with the necessary attributes when they are created. If you don't define an `__init__` method, Python will provide a default constructor that does nothing.
# The `__init__` method is a key part of object-oriented programming in Python, enabling you to create objects with specific attributes and behaviors right from the moment they are instantiated.
