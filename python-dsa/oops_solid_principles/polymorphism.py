# Base class 
class Vehicle:
    def accelerate(self):
        print("Vehicle is accelerating")

# Subclass overriding the method
class Car(Vehicle):
    def accelerate(self):
        print("Car is accelerating")

class Bike(Vehicle):
    def accelerate(self):
        print("Bike is accelerating")

class Truck(Vehicle):
    def accelerate(self):
        print("Truck is accelerating")

from typing import List

vehicles: List[Vehicle] = [Car(), Bike(), Truck()]



for vehicle in vehicles:
    vehicle.accelerate()