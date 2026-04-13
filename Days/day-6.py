'''
1️⃣ Even/Odd

Input a number → print even or odd

2️⃣ Sum of n numbers

Input n → print sum from 1 to n

3️⃣ Reverse a number

Input: 123 → Output: 321

4️⃣ Count digits

Input: 12345 → Output: 5

5️⃣ Sum of digits

Input: 123 → Output: 6

6️⃣ Prime check

Check if a number is prime

7️⃣ List sum

Take a list → print sum using loop

8️⃣ Remove duplicates

Input list → remove duplicates using set

9️⃣ Dictionary loop

Create dictionary → print keys and values

🔟 Pattern
*
**
***
****
'''

# # 1-->
# number = int(input('number:'))
# if number % 2 == 1:
#     print('odd')
# else:
#     print('even')

# # 2-->
# a = 0
# n = int(input('n:'))
# for i in range(n + 1):
#     a += i
# print(a)

# 3-->
# # input is 1,2,3
# for i in range(3,0,-1):
#     print(i, end=",")
#   or eassy way 
# str = '1,2,3'
# print(str[::-1])

# 4-->
# str = '12345'
# print(len(str))

# 5-->
# a = 1,2,3
# print(sum(a))

# # 6-->
# num = int(input('number:'))
# prime = True
# if num == 1:
#     prime = False
# for i in range(3,num):
#     if num % i == 0:
#         prime = False
# if prime:
#     print('prime')
# else:
#     print('not prime')

# 7--> 
# combination of list and loop didnt studied yet but here is my try
# list =[23,45,76,23,43]
# for list in range(0,4):
#     print(list)
# tried but its not working 

# 8-->
# know nothing about sets

# 9-->
# know nothing about dict

# # 10-->
# n = int(input('n:'))
# for i in range(1,n + 1):
#     print("*" * i)

num = 4827
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
    print(num)
