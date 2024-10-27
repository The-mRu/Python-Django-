
# Defining the factorial function using recursion
def factorial(n):
    if n == 0:
        return 1      # Base case: if n is 0, the factorial is 1

    else:
        return n * factorial(n - 1) # Recursive case: n * factorial of (n-1)
    
# Prompt the user to input a number
num = int(input("Enter your number: "))

# Print the result: the factorial of the entered number
print(f"Factorial of {num} is {factorial(num)}")
