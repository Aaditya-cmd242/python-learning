# LOOPS 
'''
*   LOOP CONTROL
.   What are Loop Control Statements?

👉 They change how a loop behaves
Instead of normal flow, you can:

stop it
skip parts
control execution

*  there are 3 Loop Control Statements
🔴 1. break (VERY IMPORTANT)
🧠 Meaning:

👉 Immediately stops the loop

📌 Example
for i in range(1, 6):
    if i == 3:
        break
    print(i)
Output:
1
2
🔍 How it works

Loop runs:

i = 1 → print
i = 2 → print
i = 3 → 💥 break → loop ends

Stop when:-
           condition met
           found element
           user input matches


🟡 2. continue (VERY IMPORTANT)
🧠 Meaning:

👉 Skip current iteration, go to next

📌 Example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
Output:
1
2
4
5
🔍 How it works
i = 3 → skipped
rest runs normally

Skip:
     unwanted values
     odd/even filtering
     invalid inputs


🧠 What is pass in loops?

👉 pass means:

“Do nothing, but don’t give error”

🔴 Why do we need pass?

In Python, you cannot leave a block empty

❌ This gives error:

for i in range(5):

👉 Python expects some code inside

✅ So we use pass
for i in range(5):
    pass

👉 Now:

loop runs ✔️
but does nothing ✔️
no error ✔️
'''

# LOOP PRACTICE PROBLEMS 

'''
1 Prime Numbers (Range)

Print all prime numbers from 1 to n

2 Factorial Series

Print factorial of numbers from 1 to n
👉 Example: 1!, 2!, 3!, ...

3 Reverse a Number

Input: 1234
Output: 4321

4 Count Digits

Input: 12345
Output: 5

5 Sum of Digits

Input: 123
Output: 6

6 Armstrong Number

Check if a number is Armstrong
👉 Example: 153 → 1³ + 5³ + 3³ = 153

7 Palindrome Number

Input: 121 → Palindrome
Input: 123 → Not

8 Fibonacci Series

Print first n terms

9 Multiplication Table (Nested)

Print tables from 1 to 5

10 Diamond Pattern
   *
  ***
 *****
*******
 *****
  ***
   *

11 Number Pyramid
1
121
12321
1234321

12 Floyd's Triangle
1
2 3
4 5 6
7 8 9 10

13 Pascal Triangle (Basic)
1
1 1
1 2 1
1 3 3 1

14 Hollow Square
*****
*   *
*   *
*****

15 Right Aligned Triangle
    *
   **
  ***
 ****

16 Find Largest Digit

Input: 59382 → Output: 9

17 Count Even/Odd Digits

Input: 123456
Output: Even=3, Odd=3

18 Strong Number

👉 Example: 145 → 1! + 4! + 5! = 145

19 GCD (Greatest Common Divisor)

Input: 12, 18 → Output: 6

20 Number Guessing (Loop + Condition)

👉 Keep asking user until correct number is guessed


'''

# 1 -->
# n = int(input("Enter a number: "))
# for num in range(2, n + 1):   
#     is_prime = True            
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

# 2-->
# n = int(input("Enter n: "))
# for num in range(2, n + 1):   
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
        
