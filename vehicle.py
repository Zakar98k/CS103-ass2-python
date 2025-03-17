from abc import ABC, abstractmethod

class Vehicle():
    def __init__(self, license_plate: str, color: str, speed: float, running=False):
        self.license_plate = license_plate
        self.color = color
        self.speed = speed # in kph
        self.running = running
    
    @abstractmethod
    def print_info(self):
        print(f"This vehicle reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")
        
    
    @abstractmethod
    def start(self):
        if self.running:
            print("Vehicle already running!")
        else:
            print("######## ! ! !\nVehicle is now on the move\n####### ! ! !")
            self.running = not self.running
            
            
    
    @abstractmethod
    def stop(self):
        if self.running:
            print("######## ! ! !\nVehicle is now stopped\n####### ! ! !")
            self.running = not self.running
        else:
             print("Vehicle is already stopped though!")

class Bus(Vehicle):
    def __init__(self, license_plate, color, speed, model: str, running = False):
        super().__init__(license_plate, color, speed, running)
        self.model = model
    
    def print_info(self):
        print(f"This {self.model} reaches speeds of {self.speed}kph. It has a {self.color} finish, and the license plate is {self.license_plate}")

random_vehicle = Vehicle("123-456", "black", 90.34)
random_vehicle.print_info()

limbus = Bus("666-666", "dirty brown", 110.5, "Limbus")
limbus.print_info()

limbus.stop()
limbus.start()
limbus.stop()