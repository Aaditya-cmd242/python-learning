
# LOOPS (2)
'''
*   for loop(mostly used)

.   You know how many times to run

i here is just variable 
Example 1
for i in range(5):
    print(i)
Output: 0 1 2 3 4

.   range() explained

1. range(n)
range(5) → 0,1,2,3,4
2. range(start, end)
range(1, 5) → 1,2,3,4
3. range(start, end, step)
range(1, 10, 2) → 1,3,5,7,9

*   while loop

.   You don't know how many times → depends on condition
while condition:

    # code
Example
i = 1

while i <= 5:
    print(i)
    i += 1

.   infinite Loop (IMPORTANT)

while True:
    print("Hello")

👉 Runs forever ❌ (unless stopped)

.   Nested Loops

Loop inside loop:

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

Key Concepts
✔️ Loop runs until condition ends
✔️ for → fixed count
✔️ while → condition-based
✔️ Always update variable in while
'''

# PRACTICE PROBLEMS
'''
Easy (1-7)

👉 Basic loop understanding

1.  Print numbers from 1 to 10
2.  Print numbers from 1 to 20
3.  Print numbers from 10 to 1 (reverse)
4.  Print all even numbers from 1 to 20
5.  Print all odd numbers from 1 to 20
6.  Print numbers from 1 to n (take input)
7.  Print numbers from n to 1 (take input)
'''

# 1 -->
# for num in range (1,11):
#     print(num)

# 2 -->
# for num in range (1,21):
#     print(num)
# 3 -->
# for num in range(10,0,-1):
#     print(num)

# 4 -->
# for num in range(1,21,):
#     if num % 2 == 0:
#         print(num)

# 5 -->
# for num in range(1,21,2):
#     print(num)

# 6 -->
# for num in range(1,int(input('n:'))):
#     print(num)
# 7 -->
# for num in range(int(input('n:')),0,-1):
#     print(num)

'''
Medium (8-14)

👉 Logic + loops

8.  Print sum of numbers from 1 to 10
9.  Print sum of numbers from 1 to n
10. Print multiplication table of a number
11. Count how many numbers from 1 to 50 are divisible by 3
12. Print all numbers between 1-50 divisible by both 2 and 5
13. Print square of numbers from 1 to 10
👉 Output: 1, 4, 9, 16...
14. Print cube of numbers from 1 to 5
'''

# 8 -->
# list = [num for num in range(1,11,)]
# print(sum(list))
# or
# list = []
# for num in range (1,11):
#     list.append(num)
# print(sum(list))

# 9-->
# list = [num for num in range (1,int(input('num:')))]
# print(sum(list))

# 10-->
# num = int(input('num'))
# for a in range (1,11):
#     print(str(num) + "X" + str(a )+ "=" + str(num * a))

# 11-->
# count = 0
# for num in range (1,51):
#     if num % 3 == 0:
#         count += 1
# print(count)

# 12-->
# for num in range(1,51):
#     if num % 2 == 0 and num % 3 == 0:
#         print(num)

# 13-->
# for num in range (1,11):
    # print(num ** 2)

# 14-->
# for num in range (1,6):
    # print(num ** 3)

'''
Hard (15-20)

👉 Real logic + nested thinking

15. Print pattern:
*
**
***
****
*****
16. Print pattern:
*****
****
***
**
*
17. Print:
1
12
123
1234
18. Print:
1
22
333
4444
19. Take a number and check if it is prime
20. Take a number and print its factorial
'''

# 15-->
# Number of rows

# for i in range(1,6):
    # print('*' * i)

# 16-->
# for i in range(5,0,-1):
    # print("*" * i)

# 17-->
# for x in range(1,5):
#     for y in range(1, x + 1):
#         print(y, end=" ")
#     print()

# 18-->
# for x in range (1,5):
#     for y in range(x):
#         print(x, end=" ")
#     print()

# 19-->
# num = int(input('num:'))
# if num  num == 0:
#     print('prime')
# else:
#     print('not a prime')

