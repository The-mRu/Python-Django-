# Function to calculate the sum of all numbers in a tuple
def sum_of_tuple(tup):
    total_sum = sum(tup)  # Calculate the sum using the built-in sum function
    return total_sum

# Create a tuple of five numbers
numbers = (5, 10, 15, 20, 25)

# Call the function to get the sum
total = sum_of_tuple(numbers)
print(f"The sum of the tuple is: {total}")

# Trying to modify an element in the tuple (this will raise an error)
try:
    numbers[0] = 100  # Attempt to change the first element
except TypeError as e:
    print(f"Error: {e}")
