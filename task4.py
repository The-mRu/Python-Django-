# Define the first string
text1 = "Django Course in here "

# Define the second string
text2 = "IIUC "

# Extract a substring from text1 from index 7 to 16 (not inclusive)
SubStr_text1 = text1[7:16]  # Extracted substring

# Print the string with only the first letter capitalized
print("capitalize: ", text1.capitalize())

# Print the extracted substring
print("Sub string: ", SubStr_text1)

# Print the string converted to uppercase
print("upper", text1.upper())

# Print the string converted to lowercase
print("lower", text1.lower())

# Print the string with the first letter of each word capitalized
print("title", text1.title())

# Print the string converted to lowercase again (repeated operation)
print("lower", text1.lower())

# Replace "here" with "IIUC" in text1 and print the result
print("replace", text1.replace("here", "IIUC")) 

# Concatenate text1 and text2 and print the result
print("Concatenation:", text1 + text2)

# Repeat text2 three times and print the result
print("String Repetition:", text2 * 3)

# Print the first character of text1
print("Print 1st character of text1 :", text1[0])
