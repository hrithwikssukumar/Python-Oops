# Encapsulation: Secure User Data
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password  # Private attribute

    def get_username(self):
        return self.__username

# Inheritance: Product & DigitalProduct
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product: {self.name}, Price: ₹{self.price}"

class DigitalProduct(Product):  # Inheriting Product
    def __init__(self, name, price, file_size):
        super().__init__(name, price)
        self.file_size = file_size

    def get_details(self):  # Overriding method
        return f"Digital Product: {self.name}, Price: ₹{self.price}, Size: {self.file_size}MB"

# Polymorphism: Common Checkout Method
def checkout(item):
    print(item.get_details())

# Creating objects
user = User("Hrithwik", "secure123")
laptop = Product("Laptop", 50000)
ebook = DigitalProduct("Python Guide", 299, 5)

checkout(laptop)  # Output: Product: Laptop, Price: ₹50000
checkout(ebook)  # Output: Digital Product: Python Guide, Price: ₹299, Size: 5MB
