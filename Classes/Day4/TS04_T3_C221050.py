# Class focused solely on car properties and driving behavior
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} is being driven.")

# Class for handling fuel calculations
class FuelEfficiencyCalculator:
    def calculate(self, miles, fuel):
        return miles / fuel

# Example Usage:
car1 = Car("Toyota Camry")
car1.drive()

# Create a FuelEfficiencyCalculator object
calculator = FuelEfficiencyCalculator()

# Using the calculator to compute fuel efficiency
miles_driven = 100
gallons_used = 3.7
efficiency = calculator.calculate(miles_driven, gallons_used)
print(f"Fuel Efficiency: {efficiency:.2f} miles per gallon") 
