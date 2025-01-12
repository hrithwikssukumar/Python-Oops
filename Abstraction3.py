class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Subclass Dog
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Subclass Cat
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage
if __name__ == "__main__":
    circle = Circle(5)  # Radius = 5
    rectangle = Rectangle(4, 6)  # Width = 4, Height = 6

    print(f"Circle Area: {circle.area()}")
    print(f"Rectangle Area: {rectangle.area()}")

    dog = Dog()
    cat = Cat()

    print(f"Dog: {dog.speak()}")
    print(f"Cat: {cat.speak()}")