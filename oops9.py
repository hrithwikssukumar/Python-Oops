class Product:
    def __init__(self, product_id, name, price, stock=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            print(f"Added {quantity} units to {self.name}. New stock: {self.stock}")
        else:
            print("Quantity to add must be positive.")

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            print(f"Cannot reduce {quantity} units from {self.name}. Only {self.stock} units available.")
        elif quantity <= 0:
            print("Quantity to reduce must be positive.")
        else:
            self.stock -= quantity
            print(f"Reduced {quantity} units from {self.name}. New stock: {self.stock}")

    def display_details(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product with ID {product.product_id} already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Added product {product.name} to inventory.")

    
    def display_inventory(self):
        if self.products:
            print("Inventory Details:")
            for product in self.products.values():
                product.display_details()
        else:
            print("No products in inventory.")

    def find_product(self, product_id):
        return self.products.get(product_id, None)


inventory = Inventory()


product1 = Product(101, "Laptop", 1200.0, 10)
product2 = Product(102, "Smartphone", 800.0, 20)
product3 = Product(103, "Headphones", 150.0, 50)


inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)


inventory.display_inventory()


product1.add_stock(5)


product2.reduce_stock(10)


product3.reduce_stock(60)

inventory.display_inventory()
