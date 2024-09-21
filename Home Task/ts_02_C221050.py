"""_
ID C221050
Md Rayhan Uddain
Home Task #2 
Number Guessing Game with Constraints
Objective: Create a Python program where the user has to guess a randomly chosen number between 1 and 100 within 7 attempts.

Key Requirements:
* Use if-else to compare the guessed number with the correct one.
* Implement a for loop to manage 7 attempts.
* Use break to exit the loop if the user guesses correctly.
* Use continue to skip an attempt if the guess is out of the valid range (1-100).
* Provide feedback if the guess is too high or too low.
* Show a success message if guessed correctly, or display the correct number after 7 attempts if the user fails.

Each operation should be top commented properly.
Each print out should be with proper note.
You are free to use chat-gpt and other online resources.
"""

import random,os,platform


# Initialize the flag to check if the user guessed correctly
check = False

# Set the maximum number of attempts
max_attempts = 7

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

#name of the game
print("Number Guessing Game with Constraints\n")

# Loop to provide 7 attempts for guessing the number
for attempt in range(7):
    
    # Prompt the user to enter their guess
    guess = int(input("Enter your guessing number: "))
    
    # Check if the guess is within the valid range
    if guess < 1 or guess > 100:  
        print("Invalid guess. Please choose a number between 1 and 100.\n")
        continue  # Skip this attempt and move to the next one
    
    # Check if the guessed number is correct 
    if random_number == guess:
        check=True
        break  # Exit the loop if the guess is correct
    
    # Provide feedback if the guess is too high
    elif random_number < guess:
        print("-_-  Too High\n")
    
    # Provide feedback if the guess is too low
    else:
        print("-_-  Too Low\n")
    
    # Show the remaining attempts
    remaining_attempts = max_attempts - attempt-1  
    print(f"Remaining attempts: {remaining_attempts}")


        
# Clear the screen based on OS
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


# If the user did not guess correctly in 7 attempts
if not check:
    # Inform the user of the correct number
    print(f"Too many attempts and you failed\nThe correct number is {random_number}\n")
    print("Try again\nBest of Luck\n")
#If the user guess correctly 
else:   
    print("Well Done!\nYou guessed the correct one!")
    check = True  # Update flag as true