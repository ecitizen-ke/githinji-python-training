# This file demonstrates commonly used string methods in Python

# capitalize(): Convert the first character of a string to uppercase
original_string = "python is fun"
capitalized_string = original_string.capitalize()
print("Capitalized String:", capitalized_string)

# upper(): Convert all characters of a string to uppercase
uppercase_string = original_string.upper()
print("Uppercase String:", uppercase_string)

# lower(): Convert all characters of a string to lowercase
lowercase_string = original_string.lower()
print("Lowercase String:", lowercase_string)

# split(): Split a string into a list of substrings based on a delimiter
sentence = "Python is awesome"
words = sentence.split()
print("Words in Sentence:", words)

# join(): Join elements of a list into a single string using a delimiter
joined_string = "-".join(words)
print("Joined String:", joined_string)

