# Creating a list of numbers
numbers = [10, 25, 3, 8, 15, 42, 7]

# Initialize variables
total_sum = 0
largest_num = float('-inf')  # Start with the smallest possible number
smallest_num = float('inf')   # Start with the largest possible number

# 1. Calculate the sum, largest, and smallest using a for loop
for num in numbers:
    total_sum += num  # Summing all elements
    if num > largest_num:
        largest_num = num  # Update largest number
    if num < smallest_num:
        smallest_num = num  # Update smallest number

# 2. Calculate the average
average = total_sum / len(numbers) if numbers else 0  # Avoid division by zero

# Print results
print(f"The sum of all elements is: {total_sum}")
print(f"The largest number is: {largest_num}")
print(f"The smallest number is: {smallest_num}")
print(f"The average is: {average:.2f}")
