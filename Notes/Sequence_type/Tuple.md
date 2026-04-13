# TUPLES

A tuple is a collection of items stored in a single variable.

Tuples are:
- Ordered
- Immutable (cannot be changed)
- Allow duplicate values

## Creating a Tuple

'''python
a = (1, 2, 3)
b = ("apple", "banana", "cherry")
c = (1, "aditya", 3.5)
Single Element Tuple
a = (5,) '''  # comma is imp to create tuple

# Note: Without comma, it is not a tuple.

# Accessing Elements
a = (10, 20, 30)

print(a[0])   # 10
print(a[-1])  # 30
Slicing
a = (1, 2, 3, 4, 5)

print(a[1:4])   # (2, 3, 4)

# Tuple Methods
a = (1, 2, 2, 3)

a.count(2)   # count occurrences
a.index(3)   # find index
Tuple Packing & Unpacking
# packing
a = (1, 2, 3)

# unpacking
x, y, z = a

# NESTED TUPLE

A nested tuple is a tuple inside another tuple.

## Example

'''python
a = (1, 2, (3, 4), 5)

Here, (3, 4) is a tuple inside the main tuple.

Accessing Elements
a = (1, 2, (3, 4), 5)

print(a[2])      # (3, 4)
print(a[2][0])   # 3
print(a[2][1])   # 4'''
