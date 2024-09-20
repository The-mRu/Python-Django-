# Create a list of even numbers from 1 to 100 using list comprehension
even_numbers = [x for x in range(1, 101) if x % 2 == 0]

# Print the list of even numbers
print("\nEven numbers from 1 to 100:", even_numbers)

# Use a lambda function to multiply each even number by 3
multiplied_even_numbers = list(map(lambda x: x * 3, even_numbers))

# Print the multiplied list
print("\nEven numbers multiplied by 3:", multiplied_even_numbers)
