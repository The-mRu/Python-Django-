
# Importing the custom module
import t2_modules as t2  # Import the t2_modules as t2 for easier usage

# Using the celsius_to_fahrenheit function
celsius_temp = int(input("Enter celsius temp : "))
fahrenheit_temp = t2.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")

# Using the circle_area function
radius = int(input("Enter radius : "))
area = t2.circle_area(radius)
print(f"The area of a circle with radius {radius} is {area:.2f}")
