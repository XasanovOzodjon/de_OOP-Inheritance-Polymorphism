class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_delivery_method(self):
        raise Exception("Error")
    
    def download(self):
        raise Exception("Error")

class PhysicalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def get_delivery_method(self):
        return f"{self.name} is delivered by courier or mail."

    def download(self):
        return f"This is a physical product and cannot be downloaded."

class DigitalProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        
    def get_delivery_method(self):
        return f"{self.name} is delivered via download link."

    def download(self):
        return f"Downloading {self.name} starting..."

# Misol:
# pp = PhysicalProduct("Book", 25)
# print(pp.get_delivery_method())  # Book is delivered by courier or mail.
# dp = DigitalProduct("E-book", 10)
# print(dp.get_delivery_method())  # E-book is delivered via download link.
# print(dp.download())             # Downloading E-book...