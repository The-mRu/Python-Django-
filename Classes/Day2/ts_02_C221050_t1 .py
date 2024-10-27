#enter a number
number = int(input("Enter a number: "))

# Check if the number is positive
if number > 0:
    print("Positive number")  # Print if the number is positive
# Check if the number is negative
elif number < 0:
    print("Negative number")  # Print if the number is negative
# If the number is neither positive nor negative, it must be zero
else:
    print("Number is Zero")   # Print if the number is zero
