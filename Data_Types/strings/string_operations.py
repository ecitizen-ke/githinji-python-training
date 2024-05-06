# This file demonstrates basic string operations in Python

# Concatenation: Combining two strings
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print("Concatenated String:", concatenated_string)

# Repetition: Repeating a string multiple times
repeated_string = string1 * 3
print("Repeated String:", repeated_string)

# Slicing: Extracting a substring from a string
original_string = "Python is amazing"
substring = original_string[7:10]  # Extract "is"
print("Substring:", substring)

# Length: Finding the length of a string
length_of_string = len(original_string)
print("Length of String:", length_of_string)

# Checking Membership: Checking if a substring exists in a string
substring_to_check = "amazing"
if substring_to_check in original_string:
    print("Substring exists in the original string")
else:
    print("Substring does not exist in the original string")

