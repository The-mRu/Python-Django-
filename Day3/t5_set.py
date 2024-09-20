# Create two sets of student names
set_a = {"Nahian", "Rafi", "Rayhan", "Mamun"}
set_b = {"Mamun", "Rayhan", "Mutasim", "Rafi"}

# Find students who are in both sets (intersection)
intersection_students = set_a & set_b
print("Students in both sets (Intersection):", intersection_students)

# Find students who are only in one set (symmetric difference)
unique_students = set_a ^ set_b
print("Students only in one set:", unique_students)
