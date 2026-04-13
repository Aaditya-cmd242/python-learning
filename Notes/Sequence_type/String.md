# STRINGS
string :- string is nothing but text data we uses in python such as name, word, sentence and even numbers. even this sentence is string we needs to use single and double quotes at starting and ending of 
our text to make it string 

# FOR EXAMPLE 
'aditya', 'play', 'aditya is learning','19'
"aditya", "play", "aditya is learning", "19"

# IMP NOTE
using quotes 3 times can make multi-line string

# FOR EXAMPLE
'''aditya
is
learning'''
and 
"""aditya 
is 
learning"""

# IMP NOTE
if string is not used then it will be ignored 

# STRING SLICING

String slicing is used to extract a part of a string.

## Syntax

python
string[start : end : step]
start → index where slicing begins
end → index where slicing stops (not included)
step → jump between characters
Example
s = "aditya"

print(s[0:3])   # adi
print(s[2:5])   # ity
Default Values
s = "aditya"

print(s[:3])   # adi  (start = 0)
print(s[2:])   # itya (end = last)
print(s[:])    # aditya (full string)
# Negative Indexing
s = "aditya"

print(s[-1])     # a
print(s[-4:-1])  # ity
Step (Skipping)
s = "aditya"

print(s[::2])   # adta

Reverse String
s = "aditya"

print(s[::-1])   # aytida

# STRING FUNCTIONS

s = "AdItYa"

s.lower()     # aditya
s.upper()     # ADITYA
s.title()     # Aditya
s.capitalize()# Aditya
s.swapcase()  # aDiTYA
len(s)   # 6
s.strip()   # "hello"
s.lstrip()  # "hello  "
s.rstrip()  # "  hello"
s.find("i")    # index of i
s.index("i")   # same but gives error if not found
s.count("a")   # 2

s = "I like Python"

s.replace("Python", "Java")

# split and join
s = "a b c"

s.split()   # ['a', 'b', 'c']

a = ["a", "b", "c"]

" ".join(a)  # "a b c"

# Check Functions
s = "aditya123"

s.isalpha()  # False
s.isdigit()  # False
s.isalnum()  # True

# Just remember:
- **case functions**
- **search (find, index, count)**
- **modify (replace, strip)**
- **split/join**
- **check functions**

That’s 90% of string usage in real coding.
