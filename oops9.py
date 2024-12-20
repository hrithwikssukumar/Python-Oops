class Product:
    def __init__(self, product_id, name, price, stock=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    # Method to add stock
    def add_stock(self, quantity):
        if quantity > 0:
            self.stock += quantity
            print(f"Added {quantity} units to {self.name}. New stock: {self.stock}")
        else:
            print("Quantity to add must be positive.")

    # Method to reduce stock
    def reduce_stock(self, quantity):
        if quantity > self.stock:
            print(f"Cannot reduce {quantity} units from {self.name}. Only {self.stock} units available.")
        elif quantity <= 0:
            print("Quantity to reduce must be positive.")
        else:
            self.stock -= quantity
            print(f"Reduced {quantity} units from {self.name}. New stock: {self.stock}")

    # Method to display product details
    def display_details(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}")


class Inventory:
    def __init__(self):
        self.products = {}

    # Add a product to the inventory
    def add_product(self, product):
        if product.product_id in self.products:
            print(f"Product with ID {product.product_id} already exists.")
        else:
            self.products[product.product_id] = product
            print(f"Added product {product.name} to inventory.")

    # Display details of all products
    def display_inventory(self):
        if self.products:
            print("Inventory Details:")
            for product in self.products.values():
                product.display_details()
        else:
            print("No products in inventory.")

    # Find a product by ID
    def find_product(self, product_id):
        return self.products.get(product_id, None)


# Example usage
inventory = Inventory()

# Create products
product1 = Product(101, "Laptop", 1200.0, 10)
product2 = Product(102, "Smartphone", 800.0, 20)
product3 = Product(103, "Headphones", 150.0, 50)

# Add products to inventory
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

# Display inventory
inventory.display_inventory()

# Add stock to a product
product1.add_stock(5)

# Reduce stock of a product
product2.reduce_stock(10)

# Try to reduce more stock than available
product3.reduce_stock(60)

# Display inventory after updates
inventory.display_inventory()
