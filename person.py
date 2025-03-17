class Person:
    def __init__(self, name: str, country: str, birth_date: int):
        self.name = name
        self.country = country
        self.birth_date = birth_date
    
    def current_age(self):
        return 2025 - self.birth_date

zach = Person("Zach", "Philippines", 2005)
print(zach.current_age())