# Enter marks from the user
marks = int(input("Enter your marks: "))

# Check if marks are within valid range (0 to 100)
if 0 <= marks and marks <= 100:
    
    # If marks are 61 or above, assign grade A
    if marks > 60:
        print("A")
        
    # If marks are between 51 and 60, assign grade B
    elif marks > 50:
        print("B")
        
    # If marks are between 40 and 50, assign grade C
    elif marks >= 40:
        print("C")
        
    # If marks are below 40, print fail
    else:
        print("Fail")

# If marks are not between 0 and 100, it's an invalid input
else:
    print("Invalid input")
