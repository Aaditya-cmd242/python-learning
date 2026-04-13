# LISTS

A list is a collection of items stored in a single variable.

Lists are:
- Ordered
- Mutable (can be changed)
- Allow duplicate values

## Creating a List

'''python
a = [1, 2, 3]
b = ["apple", "banana", "cherry"]
c = [1, "aditya", 3.5]'''

# Accessing Elements
a = [10, 20, 30]

print(a[0])   # 10
print(a[-1])  # 30
Slicing
a = [1, 2, 3, 4, 5]

print(a[1:4])   # [2, 3, 4]

# Changing Values
a = [1, 2, 3]
a[1] = 100

print(a)  # [1, 100, 3]

# List Methods
a = [1, 2, 3]

a.append(4)      # add at end
a.insert(1, 10)  # add at index
a.remove(2)      # remove value
a.pop()          # remove last item
a.sort()         # sort list
a.reverse()      # reverse list
Length of List
a = [1, 2, 3]
print(len(a))  # 3

# NESTED LIST

A nested list is a list inside another list.

## Example

```python
a = [1, 2, [3, 4], 5]

Here, [3, 4] is a list inside the main list.

Accessing Elements
a = [1, 2, [3, 4], 5]

print(a[2])      # [3, 4]
print(a[2][0])   # 3
print(a[2][1])   # 4
Changing Values
a = [1, 2, [3, 4]]

a[2][0] = 100

print(a)   # [1, 2, [100, 4]]
Looping Nested List
a = [1, 2, [3, 4]]

for i in a:
    print(i)

Output:
1
2
[3, 4]
