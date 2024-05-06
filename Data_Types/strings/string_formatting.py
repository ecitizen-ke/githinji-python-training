# This file demonstrates different ways of string formatting in Python

# Using % Operator (Old Style Formatting)
name = "Alice"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print("Formatted String (Old Style):", formatted_string)

# Using str.format() Method (New Style Formatting)
formatted_string = "Name: {}, Age: {}".format(name, age)
print("Formatted String (New Style):", formatted_string)

# Using f-strings 
formatted_string = f"Name: {name}, Age: {age}"
print("Formatted String (f-strings):", formatted_string)

# f-strings provide a concise and readable way to format strings in Python.
# They allow you to embed expressions directly inside string literals by prefixing the string with 'f' or 'F'.
# Inside an f-string, you can include Python expressions enclosed in curly braces {}. 
# These expressions are evaluated at runtime, and their results are inserted into the string.
# f-strings offer a more intuitive and efficient alternative to the older formatting methods (% operator and str.format()).
# They are especially useful for complex string formatting where you need to include variables or expressions inline.

