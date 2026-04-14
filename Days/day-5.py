# in the name of day-5 took 2 week break for jee preap exam

# NESTED LOOPS PRACTICE

# EXAMPLE:-
# x = int(input('n:'))
# for i in range (1,x + 1): # runs n times
#     for j in range (1,x + 1): # runs n times for each i
#         for k in range (1, x+1): # runs n times for i and j 
#             print(i,j,k)
#Total iterations = outer loop × inner loop x inner loop x ....
# Example:
# outer = 3 times
# inner = 2 times
# 👉 total = 6 executions
# i = 0
# while i < 3:
#     j = 0
#     while j < 2:
#         print(i, j)
#         j += 1
#     i += 1
# n = int(input('n:'))
# for i in range (n,0,-1):
#     n -= 1
#     for j in range (i):
#         print(4,end='') # end='' prints whole loop in single line
#     print()
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     for value in row:
#         print(value, end=" ")
# n = 4

# for i in range(n):
#     # print spaces
#     for j in range(n - i - 1):
#         print(" ", end="")
    
#     # print stars
#     for k in range(2 * i + 1):
#         print("*", end="")
    
#     print()
# i = 1
# while i > 0:
#     print(i)
#     i += 1

'''
🔴 HARD LOOP QUESTIONS (20)
🧠 Logic + Patterns + Thinking
1️ Prime Numbers (Range)

Print all prime numbers from 1 to n

2️ Factorial Series

Print factorial of numbers from 1 to n
👉 Example: 1!, 2!, 3!, ...

3️ Reverse a Number

Input: 1234
Output: 4321

4️ Count Digits

Input: 12345
Output: 5

5️ Sum of Digits

Input: 123
Output: 6

6️ Armstrong Number

Check if a number is Armstrong
👉 Example: 153 → 1³ + 5³ + 3³ = 153

7️ Palindrome Number

Input: 121 → Palindrome
Input: 123 → Not

8️ Fibonacci Series

Print first n terms

9️ Multiplication Table (Nested)

Print tables from 1 to 5
 Diamond Pattern
   *
  ***
 *****
*******
 *****
  ***
   *
11️ Number Pyramid
1
121
12321
1234321
12️ Floyd’s Triangle
1
2 3
4 5 6
7 8 9 10
13️ Pascal Triangle (Basic)
1
1 1
1 2 1
1 3 3 1
14️ Hollow Square
*****
*   *
*   *
*****
15️ Right Aligned Triangle
    *
   **
  ***
 ****
16️ Find Largest Digit

Input: 59382 → Output: 9

17️ Count Even/Odd Digits

Input: 123456
Output: Even=3, Odd=3

18️ Strong Number

👉 Example: 145 → 1! + 4! + 5! = 145

19️ GCD (Greatest Common Divisor)

Input: 12, 18 → Output: 6

20️ Number Guessing (Loop + Condition)

👉 Keep asking user until correct number is guessed
'''

# 1-->
# n = int(input('n:'))
# for i in range(2,n + 1):
#     prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         print(i)

# 2-->
# n = int(input('n:'))
# f = 1
# for i in range (1,n):
#     f *= i
#     print(f)

# 3-->
# n = int(input('n:'))
# # for i in range(1,n + 1):
# #     print(' ' * (n - 1) + '*' * (2 * i - 1))

# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for j in range (n,1,-1):
#     print(" " * (n - j) + "*" * (2 * j - 1))
