class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

my_calculator = Calculator()

x = float(input("1st Number: "))
y = float(input("2nd Number: "))

print(f"Sum of {x} and {y} is {my_calculator.add(x, y)}")
print(f"Difference of {x} and {y} is {my_calculator.subtract(x, y)}")