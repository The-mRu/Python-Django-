import random
import os
import platform

# Initialize the flag to check if the user guessed correctly
check = False

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# Loop to provide 7 attempts for guessing the number
for i in range(7):
    try:
        # Prompt the user to enter their guess
        guess = int(input("Enter your guessing number: "))
        
        # Check if the guess is within the valid range
        if guess < 1 or guess > 100:
            print("Invalid guess. Please choose a number between 1 and 100.\n")
            continue  # Skip this attempt and move to the next one

        # Check if the guessed number is correct
        if random_number == guess:
            print("Well Done!\nYou guessed the correct number!")
            check = True  # Update flag as true
            break  # Exit the loop if the guess is correct
        
        # Provide feedback if the guess is too high
        elif random_number < guess:
            print("-_-  Too High\n")
        
        # Provide feedback if the guess is too low
        else:
            print("-_-  Too Low\n")
    
    except ValueError:
        # Handle cases where input is not a valid integer
        print("Please enter a valid integer.\n")

# If the user did not guess correctly in 7 attempts
if not check:
    # Clear the screen based on OS
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Inform the user of the correct number
    print(f"Too many attempts. The correct number was {random_number}.\n")
    print("Try again. Best of Luck!\n")
