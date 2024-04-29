#!/usr/bin/env python3
#Tuple challenge
"""
A buffest style restaurant offers five basic foods. Think of five simple foods 
and store them in a Tuple.

a.) Use a for loop to print each food the restaurant offers
b.) Try and modify/change the items
c.) The restaurant wants to change 2 items in the menu Write a line of code
    that rewrites the tuple and then use a for loop to print each item in the revised menu.
"""
# mylist 
# Is a collection of related items of the same data types
colleagues = ["Mesh","Max","Brian","Mesh","Brian"]
print("This is the original list")
print(colleagues)

colleagues[2] = "Naomi"
colleagues[3] = "Wendy"
colleagues[4] = "John"
print("\nThis is the new list after modification")
print(colleagues)

# This is a tuple 
# Tuples are immutable 
dimensions = (50,100)
print(f"Dimensions before modification: {dimensions}")




