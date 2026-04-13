# OPRATORS
'''
*   oprators(7)

.   Arithmetic Operators

| Operator | Meaning             | Example  | Output |
| -------- | ------------------- | -------- | ------ |
|  +       | Addition            |  5 + 3   | 8      |
|  -       | Subtraction         |  5 - 3   | 2      |
|  *       | Multiplication      |  5 * 3   | 15     |
|  /       | Division            |  5 / 2   | 2.5    |
|  //      | Floor Division      |  5 // 2  | 2      |
|  %       | Modulus (remainder) |  5 % 2   | 1      |
|  **      | Power               |  2 ** 3  | 8      |

.   Comparison (Relational) Operators

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
|  ==      | Equal to         |  5 == 5  |
|  !=      | Not equal        |  5 != 3  |
|  >       | Greater than     |  5 > 3   |
|  <       | Less than        |  5 < 3   |
|  >=      | Greater or equal |  5 >= 5  |
| <=       | Less or equal    |  5 <= 3  |

.   Logical Operators

| Operator | Meaning               |
| -------- | --------------------- |
|  and     | True if both are true |
|  or      | True if one is true   |
|  not     | Reverse the result    |

.   Assignment Operators

| Operator | Example   | Meaning      |
| -------- | --------- | ------------ |
|  =       |  a = 5    | Assign       |
|  +=      |  a += 2   | a = a + 2    |
|  -=      |  a -= 2   | a = a - 2    |
|  *=      |  a *= 2   | a = a * 2    |
|  /=      |  a /= 2   | a = a / 2    |
|  //=     |  a //= 2  | quotient     |
|  %=      |  a %= 2   | remainder    |
|  **=     |  a **= 2  | power        |

.   Bitwise Operators ⚡ (Advanced but important)

| Operator | Meaning     |       |
| -------- | ----------- | ----- |
|  &       | AND         |       |
| `        | `           |removed|
|  ^       | XOR         |       |
|  ~       | NOT         |       |
|  <<      | Left shift  |       |
|  >>      | Right shift |       |

.   Membership Operators

| Operator | Meaning     |
| -------- | ----------- |
|  in      | Present     |
|  not in  | Not present |

.   Identity Operators

| Operator | Meaning          |
| -------- | ---------------- |
|  is      | Same object      |
|  is not  | Different object |

'''

# CONDITIONS
'''
🔸 if only (no else)
a = 3

if a > 5:
    print("Yes")

👉 Output: Nothing (condition is False)

🔸 if-elif-else (Multiple Conditions)
a = 10

if a < 5:
    print("Small")
elif a == 10:
    print("Equal to 10")
else:
    print("Large")

✔️ Output: Equal to 10
'''

# PRACTICE PROBLEMS

'''
*   Easy (1-5)
1.  Take a number and print "Even" or "Odd"
2.  Take a number and print "Positive" or "Negative"
3.  Take a number and check if it is greater than 10 or not
4.  Take a number and print "Zero" if it is 0, otherwise print "Not Zero"
5.  Take a number and check if it is divisible by 5

1 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
else:
    print('odd')
2-->
number = float(input('number:'))
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('neither positive nor negative')  

3 -->
number = float(input('number:'))
if number > 10:
    print('greater')
elif number == 10:
    print('equal')
else:
    print('smaller')

4 -->
number = int(input('number:'))
if number == 0:
    print('zero')
else:
    print("not zero")

5 -->
number = int(input('number:'))
if number % 5 == 0:
    print('devisiable')
else:
    print('not devisiable')


🟡 Medium (6-12)
6.  take a number and check:
if > 0 → "Positive"
if < 0 → "Negative"
if = 0 → "Zero"
7.  Take a number and check:
if divisible by 2 and 3 → "Divisible by both"
otherwise → "Not divisible by both"
8.  Take a number and check if it is between 10 and 20
9.  Take a string and check if it contains "a"
10. Take a number and check:
if even → print "Even"
else → print "Odd"

(yes similar — repetition builds strength)

11. Take two numbers and print larger one
12. Take three numbers and print largest

6 -->
number = float(input('number:'))
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('zero')  

7 -->
number = int(input('number:'))
if number % 2 == 0 and number % 3 == 0:
    print("divisible")
else:
    print('not divisible')

8 -->
number = float(input('number:'))
if 10 < number < 20:
    print("yes")
else:
    print('no')

9 -->
str = str(input('str:'))
if str.count('a') == 0:
    print('it doesnot has any a')
else:
    print('it does has a')

10 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
else:
    print('odd')

11 -->
list = [float(input('num1:')), float(input('num2'))]
print(max(list))

12 -->
list = [float(input('num1:')), float(input('num2:')), float(input('num3:'))]
print(max(list))


🔴 Hard (13-20)
13. Take marks and print grade:
90+ → A
75-89 → B
50-74 → C
<50 → Fail
14. Take age and check:
<18 → "Minor"
18-60 → "Adult"

60 → "Senior"

15. Take a number:
if divisible by 2 → print "Even"
if divisible by 3 → print "Div by 3"
16. Take username:
if it contains "admin" → print "Admin access"
else → "User access"
17. Take a number:
if even AND >10 → "Valid"
else → "Invalid"
18. Take password:
if length ≥ 8 → "Strong"
else → "Weak"
19. Take two numbers:
if equal → "Same"
else → "Different"
20. Take a number:
if >0 → check if even or odd
if <0 → print "Negative number"


13 -->
student_marks = float(input('marks:'))
if student_marks >= 90:
    print('A')
elif 75 <= student_marks <=89:
    print('B')
elif 74>= student_marks >= 50:
    print('C')
else:
    print('FAIL')

14 -->
age = int(input('age'))
if age < 18:
    print('minor')
elif 60 >= age > 18:
    print('ault')
else:
    print('senior')

15 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
elif number % 3 == 0:
    print('divisible by 3')

16 -->
name = [str(input('name:'))]
if name.count('admin') > 0:
    print('admin excess')
else:
    print('user excess')

17 -->
number = int(input('number:'))
if number % 2 == 0 and number < 10:
    print('valid')
else:
    print('invilid')

18 -->
password = (input('pass:'))
if len(password) >= 8:
    print('strong')
else:
    print('weak')

19 -->
num1 = float(input('num1:'))
num2 = float(input('num2:'))
if num1 == num2:
    print('same')
else:
    print('not same')

20 -->
number = int(input('number:'))
if number > 0:
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
elif number <0:
    print('negative')
'''

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

# NESTED LOOP DETAILED
'''

'''