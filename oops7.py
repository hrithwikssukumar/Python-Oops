class Dog:
    def sound(self):
        return "Woof! Woof!"

class Cat:
    def sound(self):
        return "Meow! Meow!"

class Cow:
    def sound(self):
        return "Moo! Moo!"


# List of animal objects
animals = [Dog(), Cat(), Cow()]

# Using a loop to call the sound() method for each object
for animal in animals:
    print(f"{animal.__class__.__name__} says: {animal.sound()}")
