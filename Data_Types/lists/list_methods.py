# This file demonstrates commonly used list methods in Python

# Creating a list
numbers = [3, 1, 4, 1, 5, 9]

# append(): Add an element to the end of the list
numbers.append(2)
print("After append:", numbers)

# insert(): Insert an element at a specific index
numbers.insert(2, 6)
print("After insert:", numbers)

# remove(): Remove the first occurrence of a value from the list
numbers.remove(1)
print("After remove:", numbers)

# pop(): Remove and return the last element of the list
popped_element = numbers.pop()
print("Popped element:", popped_element)
print("After pop:", numbers)

# sort(): Sort the elements of the list in ascending order
numbers.sort()
print("Sorted list:", numbers)

# reverse(): Reverse the order of the elements in the list
numbers.reverse()
print("Reversed list:", numbers)

# count(): Count the occurrences of a value in the list
count_of_1 = numbers.count(1)
print("Count of 1:", count_of_1)

# index(): Return the index of the first occurrence of a value
index_of_5 = numbers.index(5)
print("Index of 5:", index_of_5)
