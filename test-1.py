'''
🧠 SECTION A: THEORY (20 MARKS)

👉 2 marks each

1️⃣

Difference between == and is

2️⃣

What is mutable vs immutable?

3️⃣

Difference between list and tuple

4️⃣

What does break do?

5️⃣

What does continue do?

6️⃣

Why does range(1,5) not include 5?

7️⃣

What is a set?

8️⃣

What is a dictionary?

9️⃣

What is a nested loop?

🔟

What does end=" " do?

💻 SECTION B: BASIC CODING (30 MARKS)

👉 6 marks each

1️⃣ Even/Odd

Input number → print even or odd

2️⃣ Sum of n numbers

Input n → print sum from 1 to n

3️⃣ Reverse a number (IMPORTANT)

(No string method allowed)

4️⃣ Count digits

(No string method)

5️⃣ Sum of digits
🔥 SECTION C: INTERMEDIATE (30 MARKS)

👉 10 marks each

6️⃣ Prime Number

Check if number is prime

7️⃣ List Operations

Given list:

a = [10, 20, 30, 40, 50]

👉 Print:

sum
max
even numbers
8️⃣ Remove duplicates

Input list → remove duplicates using set

🚀 SECTION D: LOGIC + PATTERN (20 MARKS)

👉 10 marks each

9️⃣ Pattern
*
**
***
****
*****
🔟 Palindrome Number

Input: 121 → Palindrome
Input: 123 → Not

🎯 MARKING STRATEGY
Logic correct → full marks
Small mistake → partial
Wrong approach → low
'''


# section a
# 1.
# '==' states value is same 
# 'is' states variable is same

# 2.
# mutable :- database which can be changed like adding extra data,removing spefecic data, changing spefic data and this can be possiple in list functions
# immutable :- database which can not be changed means we cant add extra data remove data or change data and this is possiple in tuple string etc 
# in short we can make changes in mutable data base but we cant in immutable database

# 3.
# list :- list is nothing but a simple but one of the most usefull function of python helps us keeps collection of data together. we uses [] this brackets to make list and list has many functions and is mutable
# tuple :- tuple is nothing but a simple but one of the most usefull function of python helps us keeps collection of data together. we uses commas(,) to make tuple. tuple is immutable thats why bit faster and eassier than list and has less functions than list and has its unique functions too

# 4.
# break :- break is one of the most importent function in loops because it controls loop when to stop and continue. using break function we can stop any loop at matching condition and stop loop just before that condition runs on loop

# 5.
# continue :- continue is one of the most importent function in loops because it controls loop when to stop and continue. using continue we can skip the spefic loop from running in our program and continue also works on where condition mets

# 6.
# in for loop we uses range and there is rule saying the ending of that loop cant run like if i am runing a loop for 1-100 times then it will run 99 times and exclude 100th

# 7. didnt stared to study set this is out of syllabus question

# 8.didnt stared to study dict this is out of syllabus question

# 9.
# nested loop :- nested loop is nothing but same loop we we studied its just a new loop will be used in first one according to situtions new loop new collom. (first loop runs)*(second loop runs)*.... = (total nested loop ran)

# 10.
# end='' :- end="" functions elemanates new line genration and writes every thing in one line


# section-b

# 1.
# n = int(input('n:'))
# if n % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 2.
# n = int(input('n:'))
# a = 0
# for i in range(1,n + 1):
#     a += i
# print(a)

# 5. digits are not specified 

# 6.
# num = int(input('num:'))
# a = 1
# for i in range(2,num):
#     prime = True
#     a += 1
#     if num % a == 0:
#         prime = False
# if prime:
#     print('prime')

# 7.
# Given list:

# a = [10, 20, 30, 40, 50]

# print(sum(a))
# print(max(a))
# ind = 0
# for i in range(0,len(a) - 1):
#     ind += 1
#     if a[ind] % 2 == 0:
#         print('even')
#     else:
#         print('odd')

# # 9.
# a = 0
# for i in range(1,6):
#     a += 1
#     print('*' * a)

# 8. out of syllabus because we didnt even started sets and dict 

# 4.
# example 12345
