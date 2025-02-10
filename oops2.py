class Person:
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")



person1 = Person("Ajay", 28, "Male")
person2 = Person("Priya", 25, "Female")
person3 = Person("Rahul", 30, "Male")


person1.display_info()
person2.display_info()
person3.display_info()
