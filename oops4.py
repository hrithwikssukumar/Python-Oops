# Base class
class Vehicle:
    # Constructor to initialize the attributes of the base class
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method to display details of the vehicle
    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")


# Derived class
class Car(Vehicle):
    # Constructor to initialize attributes of both the base and derived class
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)  # Call the constructor of the base class
        self.num_of_doors = num_of_doors

    # Method to display car-specific details
    def display_car_details(self):
        self.display_details()  # Call the method from the base class
        print(f"Number of Doors: {self.num_of_doors}")


# Example usage
vehicle = Vehicle("Toyota", "Corolla")
vehicle.display_details()

print("---")

car = Car("Honda", "Civic", 4)
car.display_car_details()
