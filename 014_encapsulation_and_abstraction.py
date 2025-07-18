# Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, known as a class. It restricts direct access to some of an object's components, which can prevent the accidental modification of data. Encapsulation helps in hiding the internal state of an object and only exposing a controlled interface for interaction.
# In Python, encapsulation is achieved through the use of classes and access modifiers. Attributes can be made private by prefixing them with an underscore (`_`) or double underscore (`__`), which indicates that they should not be accessed directly from outside the class. Instead, public methods (getters and setters) are provided to access or modify these attributes safely.
# Example of encapsulation in Python:


class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        self._color = None

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def display_info(self):
        return f"{self._year} {self._make} {self._model} in {self._color if self._color else 'unknown color'}"


# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)
# Setting the color using the setter method
my_car.set_color("Blue")
# Accessing the color using the getter method
print(my_car.get_color())  # Output: Blue
# Displaying car information
print(my_car.display_info())  # Output: 2020 Toyota Corolla in Blue

# In this example, the `Car` class encapsulates the attributes `_make`, `_model`, `_year`, and `_color`. The attributes are prefixed with an underscore to indicate that they are intended for internal use. The `set_color` and `get_color` methods provide a controlled way to modify and access the `_color` attribute, while the `display_info` method provides a way to display information about the car.
# Encapsulation promotes data hiding and abstraction, allowing you to change the internal implementation of a class without affecting the code that uses the class. It also helps in maintaining a clean and organized codebase by keeping related data and behavior together.

# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. It allows you to focus on what an object does rather than how it does it. In Python, abstraction can be achieved using abstract classes and interfaces.
# An abstract class is a class that cannot be instantiated and is meant to be subclassed.
# It can contain abstract methods (methods without implementation) that must be implemented by any subclass. This allows you to define a common interface for a group of related classes while leaving the implementation details to the subclasses.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# In this example, the `Shape` class is an abstract class that defines abstract methods `area` and `perimeter`. The `Circle` and `Rectangle` classes are subclasses of the `Shape` class, providing their own implementations for the abstract methods.
# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)
# Using the area and perimeter methods
print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 78.5
print(
    f"Circle Perimeter: {circle.perimeter()}"
)  # Output: Circle Perimeter: 31.400000000000002
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 24
print(
    f"Rectangle Perimeter: {rectangle.perimeter()}"
)  # Output: Rectangle Perimeter: 20
# In this example, the `Shape` class provides a common interface for all shapes, while the `Circle` and `Rectangle` classes implement the specific details of how to calculate the area and perimeter for those shapes. This allows you to work with different shapes through a common interface, promoting code reusability and flexibility.
# Abstraction helps in reducing complexity by allowing you to work with high-level concepts without needing to understand the intricate details of their implementation. It also enables you to create a clear separation between the interface and implementation, making your code more maintainable and easier to understand.
# Encapsulation and abstraction are key principles of object-oriented programming that help in organizing code, promoting reusability, and managing complexity. They allow you to create classes that encapsulate data and behavior while providing a clear interface for interaction, enabling you to build robust and maintainable software systems.
# Encapsulation and abstraction are two fundamental concepts in object-oriented programming (OOP) that help in organizing code, promoting reusability, and managing complexity. They allow you to create classes that encapsulate data and behavior while providing a clear interface for interaction, enabling you to build robust and maintainable software systems.
