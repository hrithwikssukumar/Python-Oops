
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"


animals = [Dog(), Cat()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Square(4),  
    Triangle(5, 6)  
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area()}")







class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")


class Manager(Employee):
    def __init__(self, name, designation, num_team_members):
        super().__init__(name, designation)
        self.num_team_members = num_team_members

    def display_details(self):
        super().display_details()
        print(f"Number of Team Members: {self.num_team_members}")



employee = Employee("Hrithwik S Sukumar", "Software Engineer")
manager = Manager("Prashant Kumar", "Project Manager", 10)

print("Employee Details:")
employee.display_details()

print("\nManager Details:")
manager.display_details()





