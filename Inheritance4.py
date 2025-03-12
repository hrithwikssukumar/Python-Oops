class Grandparent:
    def family_name(self):
        print("Family Name: Smith")

class Parent(Grandparent):
    def profession(self):
        print("Profession: Engineer")

class Child(Parent):
    def hobby(self):
        print("Hobby: Painting")


child = Child()

child.family_name()  
child.profession()   
child.hobby()        
