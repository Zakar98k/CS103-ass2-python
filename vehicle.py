from abc import ABC, abstractmethod

class Vehicle():
    def __init__(self, license_plate: str, color: str, speed: float):
        self.license_plate = license_plate
        self.color = color
        self.speed = speed # in kph
    
    @abstractmethod
    def print_info(self):
        print(f"This vehicle reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")

class Bus(Vehicle):
    def __init__(self, license_plate, color, speed, model: str):
        super().__init__(license_plate, color, speed)
        self.model = model
    
    def print_info(self):
        print(f"This {self.model} reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")

random_vehicle = Vehicle("123-456", "black", 90.34)
random_vehicle.print_info()

limbus = Bus("666-666", "dirty brown", 110.5, "Limbus")
limbus.print_info()