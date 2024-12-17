from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shape(ABC):
    # Abstract method to calculate the area
    @abstractmethod
    def calculate_area(self):
        pass

# Derived class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Implementation of the abstract method
    def calculate_area(self):
        return math.pi * self.radius ** 2

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementation of the abstract method
    def calculate_area(self):
        return self.length * self.width


# Example usage
circle = Circle(5)  # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with length 4 and width 6

# Display the area of Circle
print(f"Area of Circle with radius {circle.radius}: {circle.calculate_area():.2f}")

# Display the area of Rectangle
print(f"Area of Rectangle with length {rectangle.length} and width {rectangle.width}: {rectangle.calculate_area():.2f}")
