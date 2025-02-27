
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)  
        self.num_of_doors = num_of_doors

    def display_car_details(self):
        self.display_details()  
        print(f"Number of Doors: {self.num_of_doors}")



vehicle = Vehicle("Toyota", "Corolla")
vehicle.display_details()

print("---")

car = Car("Honda", "Civic", 4)
car.display_car_details()
