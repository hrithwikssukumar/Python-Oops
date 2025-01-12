from abc import ABC, abstractmethod
import math

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example usage
if __name__ == "__main__":
    circle = Circle(5)  # Radius = 5
    rectangle = Rectangle(4, 6)  # Width = 4, Height = 6

    print(f"Circle Area: {circle.area()}")
    print(f"Rectangle Area: {rectangle.area()}")
