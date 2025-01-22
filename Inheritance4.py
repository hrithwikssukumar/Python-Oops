class Grandparent:
    def family_name(self):
        print("Family Name: Smith")

class Parent(Grandparent):
    def profession(self):
        print("Profession: Engineer")

class Child(Parent):
    def hobby(self):
        print("Hobby: Painting")

# Creating an object of the Child class
child = Child()

# Demonstrating all three methods
child.family_name()  # Method from Grandparent
child.profession()   # Method from Parent
child.hobby()        # Method from Child
