# Create a dictionary to store student scores
student_scores = {
    "Rayhan": 85,
    "Rafi": 92,
    "Mamun": 100,
    "Nahian": 88,
    "Muhtasim": 91
}

# Calculate the average score
def calculate_average(scores):
    total_score = sum(scores.values())  # Sum of all scores
    avg_score = total_score / len(scores)  # Calculate average
    return avg_score

# Find highest and lowest scores
def find_high_low(scores):
    highest_score = max(scores.values())  # Highest score
    lowest_score = min(scores.values())    # Lowest score
    return highest_score, lowest_score

# Calculate average
average_score = calculate_average(student_scores)
print(f"The average score is: {average_score:.2f}")

# Find highest and lowest scores
highest_score, lowest_score = find_high_low(student_scores)
print(f"The highest score is: {highest_score}")
print(f"The lowest score is: {lowest_score}")
