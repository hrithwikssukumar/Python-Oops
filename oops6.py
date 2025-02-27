from abc import ABC, abstractmethod
import math


class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width



circle = Circle(5)  
rectangle = Rectangle(4, 6)  


print(f"Area of Circle with radius {circle.radius}: {circle.calculate_area():.2f}")

print(f"Area of Rectangle with length {rectangle.length} and width {rectangle.width}: {rectangle.calculate_area():.2f}")
