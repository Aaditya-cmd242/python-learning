'''
SET METHODS

.add() :- used to add a single element in set. element must be hashable (immutable)
example:
s = {1,2,3}
s.add(4)
output → {1,2,3,4}

s.add((2,3,4,5))
output → {1,2,3,(2,3,4,5)}
# whole tuple is added as one element


.update() :- used to add multiple elements from iterable
example:
s = {1,2,3}
s.update((2,3,4,5))
output → {1,2,3,4,5}

# string case
s.update("ab")
output → {'a','b',1,2,3,...}


.remove() :- removes specific element, gives error if element not present
example:
s = {1,3,5}
s.remove(3) → removes 3
s.remove(2) → error


.discard() :- removes element, no error if element not present
example:
s = {1,3,5}
s.discard(3) → removes 3
s.discard(2) → does nothing


.pop() :- removes random element from set


.clear() :- removes all elements
example:
s = {1,2,3}
s.clear()
s = set()


.copy() :- creates copy of set
example:
s = {1,2,3}
a = s.copy()
a.add(4)

a = {1,2,3,4}
s = {1,2,3}
# original unchanged


--------------------------------------------------

IMPORTANT CONCEPTS

- elements must be hashable
- no duplicates allowed
- add() → adds whole object
- update() → breaks iterable into elements
  "ab" → 'a','b'

--------------------------------------------------

MEMBERSHIP

in → checks element present (True/False)
not in → checks element not present

--------------------------------------------------

LOOP

we can iterate through set using loop
example:
s = {1,2,3}
for i in s:
    print(i)

# order is not fixed

--------------------------------------------------

LIMITATIONS

- no indexing
- no slicing
- reason → unordered (hashing)

--------------------------------------------------

SET OPERATIONS

a = {1,2,3,4}
b = {3,4,5,6}

a | b → {1,2,3,4,5,6}   (union)
a & b → {3,4}           (intersection)
a - b → {1,2}           (difference)
a ^ b → {1,2,5,6}       (symmetric difference)

--------------------------------------------------

SET COMPARISON

a <= b → subset
a >= b → superset
a < b → proper subset
a > b → proper superset

a.isdisjoint(b) → True if no common elements

--------------------------------------------------

IN-PLACE OPERATIONS

a |= b → union update
a &= b → intersection update
a -= b → difference update
a ^= b → symmetric difference update

# modifies original set

x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
SET METHODS (ALL)

--------------------------------------------------

ADDING ELEMENTS

.add(x) :- adds single element in set
example:
s = {1,2}
s.add(3)
→ {1,2,3}

.update(iterable) :- adds multiple elements from iterable
example:
s = {1,2}
s.update([2,3,4])
→ {1,2,3,4}

--------------------------------------------------

REMOVING ELEMENTS

.remove(x) :- removes element, gives error if not present
example:
s.remove(2)

.discard(x) :- removes element, no error if not present
example:
s.discard(2)

.pop() :- removes random element from set

.clear() :- removes all elements (empty set)
example:
s.clear()
s = set()

--------------------------------------------------

COPY

.copy() :- creates new independent copy of set
example:
a = s.copy()

--------------------------------------------------

SET OPERATIONS (METHOD FORM)

.union(set2) :- combines both sets
example:
a.union(b)

.intersection(set2) :- common elements
example:
a.intersection(b)

.difference(set2) :- removes elements of set2 from set1
example:
a.difference(b)

.symmetric_difference(set2) :- keeps non-common elements
example:
a.symmetric_difference(b)

--------------------------------------------------

IN-PLACE UPDATE METHODS

.update(iterable) :- adds elements (same as |=)

.intersection_update(set2) :- keeps only common elements (same as &=)

.difference_update(set2) :- removes common elements (same as -=)

.symmetric_difference_update(set2) :- keeps non-common (same as ^=)

--------------------------------------------------

COMPARISON METHODS

.issubset(set2) :- checks if set is inside another

.issuperset(set2) :- checks if set contains another

.isdisjoint(set2) :- checks no common elements

--------------------------------------------------

IMPORTANT POINTS

- elements must be hashable (immutable)
- no duplicates allowed
- unordered → no indexing, no slicing
- add() → adds whole object
- update() → breaks iterable into elements

x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
'''
