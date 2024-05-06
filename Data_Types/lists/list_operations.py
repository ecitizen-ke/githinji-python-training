# This file demonstrates basic list operations in Python

# Creating a list
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Slicing: Extracting a sublist
sublist = numbers[1:4]  # Extract elements from index 1 to 3
print("Sublist:", sublist)

# Modifying elements
numbers[2] = 10
print("Modified list:", numbers)

# Concatenation: Combining two lists
more_numbers = [6, 7, 8]
combined_list = numbers + more_numbers
print("Combined list:", combined_list)

# Repetition: Repeating a list
repeated_list = numbers * 2
print("Repeated list:", repeated_list)

# Length: Finding the length of a list
length_of_list = len(numbers)
print("Length of list:", length_of_list)
