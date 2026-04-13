🔁 Nested Loops in Python
📌 Definition

A nested loop is a loop inside another loop.

The outer loop runs first.
For every iteration of the outer loop, the inner loop runs completely.
🧠 Basic Syntax
for outer_var in sequence1:
    for inner_var in sequence2:
        # code block

Or with while:

while condition1:
    while condition2:
        # code block
🔄 How It Works

Example:

for i in range(3):        # outer loop
    for j in range(2):    # inner loop
        print(i, j)
🧾 Output:
0 0
0 1
1 0
1 1
2 0
2 1
💡 Explanation:
Outer loop runs 3 times → i = 0,1,2
For each i, inner loop runs 2 times
Total iterations = 3 × 2 = 6
📊 Execution Flow
Outer (i)	Inner (j)
0	0, 1
1	0, 1
2	0, 1
🎯 Common Use Cases
1. Pattern Printing
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()

Output:

* * * *
* * * *
* * * *
* * * *
2. Triangle Pattern
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

Output:

*
* *
* * *
* * * *
3. Multiplication Table
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
4. Working with 2D Lists (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
⚙️ Nested while Loop Example
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1
⛔ Important Points
🔹 1. Time Complexity
If outer loop runs m times and inner loop runs n times:
👉 Total = O(m × n)
🔹 2. Independent vs Dependent Loops
Independent:
for i in range(3):
    for j in range(3):
        print(i, j)
Dependent:
for i in range(3):
    for j in range(i):
        print(i, j)
🔹 3. Using break and continue
break (only breaks inner loop):
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
continue:
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
🔁 Nested Loops with else
for i in range(2):
    for j in range(2):
        print(i, j)
    else:
        print("Inner loop finished")
🧩 Real-Life Analogy

Think of:

Outer loop = Days
Inner loop = Hours

For each day → all hours are completed.
