# Base class
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Price: {self.price}"
    
# Derived class
class Smartphone(Device):
    def __init__(self, brand, price, model, storage):
        super().__init__(brand, price)
        self.model = model
        self.storage = storage

    def smartphone_info(self):
        return f"{self.display_info()}, Model: {self.model}, Storage: {self.storage}GB"
    
# child class
class Prosmartphone(Smartphone):
    def __init__(self, brand, price, model, storage, camera_quality):
        super().__init__(brand, price, model, storage)
        self.camera_quality = camera_quality

    def pro_smartphone_info(self):
        return f"{self.smartphone_info()}, Camera Quality: {self.camera_quality}MP"
    
iphone = Prosmartphone("Apple", 999, "iPhone 14 Pro", 256, 48)
print(iphone.pro_smartphone_info())
print(iphone.smartphone_info())
print(iphone.display_info())