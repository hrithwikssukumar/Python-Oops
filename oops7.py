class Dog:
    def sound(self):
        return "Woof! Woof!"

class Cat:
    def sound(self):
        return "Meow! Meow!"

class Cow:
    def sound(self):
        return "Moo! Moo!"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__} says: {animal.sound()}")
