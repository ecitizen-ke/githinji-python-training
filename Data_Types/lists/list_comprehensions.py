# This file demonstrates list comprehensions in Python

# Creating a list of squares using a for loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Squares (using for loop):", squares)

# Using list comprehension to create a list of squares
squares = [i ** 2 for i in range(1, 6)]
print("Squares (using list comprehension):", squares)

# Creating a list of even numbers using a for loop
even_numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        even_numbers.append(i)
print("Even numbers (using for loop):", even_numbers)

# Using list comprehension to create a list of even numbers
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers (using list comprehension):", even_numbers)

# Creating a list of tuples using a for loop
pairs = []
for i in range(1, 4):
    for j in range(1, 4):
        pairs.append((i, j))
print("Pairs (using for loop):", pairs)

# Using list comprehension to create a list of tuples
pairs = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print("Pairs (using list comprehension):", pairs)
