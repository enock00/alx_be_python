class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Laptop", 15000, 5)
print(f"Product's Name: {product1.name}")
print(f"Product'S Value: Ksh {product1.total_value():.2f}")