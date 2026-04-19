'''
Find frequency of each element in list

Print pattern:
*
**
***
****

Print reverse pattern:
****
***
**
*

Print number triangle:
1
12
123
1234

Sum of all elements in a list

Multiply all elements in a list

🔵 LEVEL 4: INTERMEDIATE (51-70)

Check if a string is palindrome using loop

Find first non-repeating character in string

Count frequency of each character in string

Find GCD of two numbers using loop

Find LCM of two numbers

Check if a number is perfect number

Generate all factors of numbers from 1 to n

Print all Armstrong numbers from 1 to n

Convert decimal to binary using loop

Convert binary to decimal

Find sum of series: 1 + 1/2 + 1/3 + ...

Find sum of squares of digits repeatedly until single digit

Count words in a sentence using loop

Reverse words in a sentence

Find longest word in a sentence

Find shortest word in a sentence

Check if two strings are anagrams

Rotate a list by k positions

Find missing number in list (1 to n)

Find duplicate elements in a list
'''

# Find frequency of each element in list
# lst = [1,4,2,1,3,5,3,1,3,5,3,2]
# nlst = []
# count = 0
# for el in lst:
#     if el not in nlst:
#         nlst.append(el)
# for element in nlst:
#     for freq in lst:
#         if element == freq:
#             count += 1
#     print(element,' = ',count)
#     count = 0

# Print pattern:
# # *
# # **
# # ***
# # ****
# a = 1
# while a <= 4:
#     print('*' * a)
#     a += 1

# Print reverse pattern:
# ****
# ***
# **
# *
# a = 4
# while a >= 1:
#     print('*' * a)
#     a -= 1

# Print number triangle:
# 1
# 12
# 123
# 1234
# for i in range(1,5):
#     for j in range(1,i + 1):
#         print(j,end='')
#     print()

# Sum of all elements in a list
# lst = [1,4,2,1,3,5,3,1,3,5,3,2]
# sum = 0
# for i in lst:
#     sum += i
# print(sum)

# Multiply all elements in a list
# lst = [1,4,2,1,3,5,3,1,3,5,3,2]
# ans = 1
# for i in lst:
#     ans *= i
# print(ans)

# Check if a string is palindrome using loop
# string = input('string:').lower()
# newstring = ''
# a = len(string)
# while a > 0:
#     a -= 1
#     newstring += string[a]
# if newstring == string:
#     print('is palindrome')
# else:
#     print('its not palindrome')

# Find first non-repeating character in string
# string = input('string:').lower()
# count = 0
# non_repeating  = ''
# for i in string:
#     for j in string:
#         if i == j:
#             count += 1
#     if count == 1:
#         non_repeating += i
#     count = 0
# print(non_repeating[0])

# Count frequency of each character in string
# string = input('string:')
# nstring = ''
# count = 0
# for el in string:
#     if el not in nstring:
#         nstring += el
# for element in nstring:
#     for freq in string:
#         if element == freq:
#             count +=1
#     print(element,' = ',count)
#     count = 0

# Find GCD of two numbers using loop
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# for i in range(min(num1,num2),0,-1):
#     if num1 % i == 0 and num2 % i == 0:
#         print('GDP = ', i)
#         break

# Find LCM of two numbers
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# for i in range(min(num1,num2),0,-1):
#     if num1 % i == 0 and num2 % i == 0:
#         gdp = i
#         break
# print('LCM = ', num1 * num2 // gdp)

# Check if a number is perfect number
# num = int(input('num:'))
# check = []
# for i in range(1,num + 1):
#     if num % i == 0:
#         check.append(i)
# check.pop()
# if sum(check) == num:
#     print(num,' is perfect number')
# else:
#     print(num,' is not a perfect number')

# # Generate all factors of numbers from 1 to n
# n = int(input('n:'))
# for i in range(1,n + 1):
#     for j in range(1,i + 1):
#         if i % j == 0:
#             print(j,end=' ')
#     print()

# Print all Armstrong numbers from 1 to n
# n = int(input('n:'))
# for i in range(1,n + 1):
#     temp = i
#     nn = 0
#     t =i
#     digits = 0
#     while t > 0:
#         digits += 1
#         t //= 10
#     while temp > 0:
#         digit = temp % 10
#         nn += digit ** digits
#         temp = temp // 10
#     if nn == i:
#         print(i)

# Convert binary to decimal
# num = int(input('num:'))
# a = 0
# decimal = 0
# while num > 0:
#     digit = num % 10
#     power = 2 ** a
#     value = digit * power
#     decimal += value
#     a += 1
#     num //= 10
# print(decimal)

# Find sum of series: 1 + 1/2 + 1/3 + ...
# n = int(input('n:'))
# a = 1
# sum_of_series = 0
# while a <= n:
#     sum_of_series += 1/a
#     a += 1
# print(sum_of_series)

# Find sum of squares of digits repeatedly until single digit
# num = int(input('num:'))
# newnum = 0
# while num > 9:
#     while num > 0:
#         digit = num % 10
#         newnum += digit ** 2
#         num //= 10
#     num = newnum
#     newnum = 0
# print(num)

# Count words in a sentence using loop
# string = input('string:').lower()
# words = True
# count = 0
# for i in string:
#     if i != ' ' and words:
#         count += 1
#         words = False
#     elif i == ' ':
#         words = True
# print(count)
