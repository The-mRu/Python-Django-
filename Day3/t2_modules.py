# t2_modules.py

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: (Celsius * 9/5) + 32
    """
    return (celsius * 9/5) + 32

# Function to calculate the area of a circle given its radius
def circle_area(radius):
    """
    Calculates the area of a circle.
    Formula: π * radius^2
    """
    pi = 3.14159  # Approximate value of π
    return pi * (radius ** 2)
