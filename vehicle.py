class Vehicle():
    def __init__(self, license_plate: str, color: str, speed: float):
        self.license_plate = license_plate
        self.color = color
        self.speed = speed # in kph
    
    def print_info(self):
        print(f"This vehicle is so fast it reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")

class Bus(Vehicle):
    def __init__(self, license_plate, color, speed, model: str):
        super().__init__(license_plate, color, speed)
        self.model = model
        
    def print_info(self):
        print(f"This {self.model} is so fast it reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")



limbus = Bus("666-666", "dirty brown", 110.5, "Limbus")
limbus.print_info()