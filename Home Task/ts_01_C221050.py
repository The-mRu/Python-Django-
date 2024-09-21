"""
ID C221050
Md Rayhan Uddain
Task: String Operations Script
 """
# 1. Assigning a string to a variable
my_string = "Hello, World!"
print("1. Original string:", my_string)

# 2. Convert the string to uppercase
print("2. Uppercase:", my_string.upper())

# 3. Convert the string to lowercase
print("3. Lowercase:", my_string.lower())

# 4. Capitalize the first letter of the string
print("4. Capitalized:", my_string.capitalize())

# 5. Count the occurrences of 'l'
print("5. Occurrences of 'l':", my_string.count('l'))

# 6. Find the position of the first 'l'
print("6. Position of first 'l':", my_string.find('l'))

# 7. Replace 'World' with 'Universe'
print("7. Replaced World with Universe:", my_string.replace('World', 'Universe'))

# 8. Check if the string is alphanumeric
print("8. Is the string alphanumeric?", my_string.isalnum())

# 9. Check if the string is alphabetic
print("9. Is the string alphabetic?", my_string.isalpha())

# 10. Check if the string is a digit
print("10. Is the string numeric?", my_string.isdigit())

# 11. Split the string on space
print("11. Split on space:", my_string.split())

# 12. Join the split string back with a dash
print("12. Join with dash:", "-".join(my_string.split()))

# 13. Strip leading and trailing whitespace (using a new example)
new_string = "   space around   "
print("13. Stripped string:", new_string.strip())

# 14. Use slicing to reverse the string
print("14. Reversed string:", my_string[::-1])

# 15. Check if the string starts with 'Hello'
print("15. Starts with 'Hello'?", my_string.startswith("Hello"))

# 16. Check if the string ends with 'World!'
print("16. Ends with 'World!'?", my_string.endswith('World!'))

# 17. Convert 'Hello, World!' to a list of characters
print("17. List of characters:", list(my_string))

# 18. Find length of the string
print("18. Length of string:", len(my_string))

# 19. Use slicing to get 'World' from 'Hello, World!'
print("19. Slice to get 'World':", my_string[7:12])

# 20. Check if all characters are lowercase
print("20. Is all lowercase?", my_string.islower())

# 21. Check if all characters are uppercase
print("21. Is all uppercase?", my_string.isupper())

# 22. Check if the string is title-cased
print("22. Is title cased?", my_string.istitle())

# 23. Find the position of 'o' using rfind
print("23. Position of last 'o' using rfind:", my_string.rfind('o'))

# 24. Split the string on 'e'
print("24. Split on 'e':", my_string.split('e'))

# 25. Replace 'l' with 'z'
print("25. Replace 'l' with 'z':", my_string.replace('l', 'z'))

# 26. Check if string contains only whitespace
space_string = "    "
print("26. Only whitespace?", space_string.isspace())

# 27. String concatenation
print("27. Concatenated string:", my_string + " It's nice to meet you!")

# 28. Multiplying string
print("28. String multiplied:", my_string * 3)

# 29. Use slicing to get 'Hello'
print("29. Slice to get 'Hello':", my_string[:5])

# 30. Use of format() method
name = "Alice"
print("30. Formatted string:", "Hello, {name}!".format(name=name))

# 31. f-string formatting (Python 3.6+)
print("31. f-string formatted: {my_string}")

# 32. Centering string with fill character
print("32. Centered string:", my_string.center(30, '*'))

# 33. Encoding a string
encoded_string = my_string.encode('utf-8')
print("33. Encoded string:", encoded_string)

# 34. Decoding a string
print("34. Decoded string:", encoded_string.decode('utf-8'))

# 35. String zfill
print("35. Zero filled string:", "42".zfill(5))

# 36. Swapcase method
print("36. Swapcase string:", my_string.swapcase())

# 37. rstrip method to remove trailing whitespace
trailing_space_string = "Hello, World!   "
print("37. String after rstrip:", trailing_space_string.rstrip())

# 38. lstrip method to remove leading whitespace
leading_space_string = "   Hello, World!"
print("38. String after lstrip:", leading_space_string.lstrip())

# 39. Partitioning a string
print("39. Partitioned string:", my_string.partition(" "))

# 40. rpartition method
print("40. Right partitioned string:", my_string.rpartition(" "))

# 41. Using expandtabs to set tab size
tabbed_string = "Hello\tWorld!"
print("41. Expandtabs:", tabbed_string.expandtabs(10))

# 42. Casefold for aggressive lowercasing
print("42. Casefolded string:", my_string.casefold())

# 43. Checking if string is printable
print("43. Is string printable?", my_string.isprintable())

# 44. Finding non-overlapping occurrences using 'count'
print("44. Non-overlapping 'l's:", my_string.count('l'))

# 45. Using title method to capitalize the first letter of each word
title_string = "hello, world!"
print("45. Title-cased string:", title_string.title())

# 46. Using istitle to check if properly title-cased
print("46. Is title-cased properly?", title_string.istitle())

# 47. Using splitlines to split a multi-line string
multi_line_string = "Hello\nWorld!"
print("47. Split lines:", multi_line_string.splitlines())

# 48. Using max to find highest alphabetical character
print("48. Max character:", max(my_string))

# 49. Using min to find lowest alphabetical character
print("49. Min character:", min(my_string))

# 50. Check if all characters in the string are decimal
decimal_string = "12345"
print("50. All characters are decimal?", decimal_string.isdecimal())
