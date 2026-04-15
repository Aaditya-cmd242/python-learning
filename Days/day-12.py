'''
SEQUENCE TYPES (Strings, Lists, Tuples) - 10 Questions

Reverse a string without using built-in functions
Count how many vowels are in a string
Find the largest number in a list
Find the second largest number in a list
Check if a string is a palindrome
Merge two lists into one
Count how many times a value appears in a list
Convert a tuple into a list and add an element

x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

🔹 CONDITIONS (if/else) - 10 Questions

Check if a number is positive, negative, or zero
Check if a number is even or odd
Find the greatest of 3 numbers
Check if a year is a leap year
Check if a number is divisible by both 3 and 5
Assign grades based on marks (90+ A, 80+ B, etc.)
Check if a character is vowel or consonant
Check if a number is a multiple of 7
Find smallest of 3 numbers
Check if a number is between 10 and 50

x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

🔹 LOOPS - 10 Questions
Print numbers from 1 to 50
Print all even numbers from 1 to 100
Find sum of numbers from 1 to n
Print multiplication table of a number
Count digits in a number
Reverse a number (e.g., 123 → 321)
Find factorial of a number
Print all numbers divisible by 3 between 1-100
Find sum of digits of a number
Print Fibonacci series up to n terms

x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

🔹 SETS - 10 Questions
Create a set and add 5 elements
Remove an element from a set
Find union of two sets
Find intersection of two sets
Find difference between two sets
Check if an element exists in a set
Remove duplicates from a list using set
Count unique elements in a list
Convert set to list and print it
Find common elements between two lists using set
'''

# SEQUENCE TYPES (Strings, Lists, Tuples) - 8 Questions
# 1-->
# str = input('str:')
# print(str[len(str):0:-1])
# 2-->
# s = input('s:')

# count = (s.lower().count('a') +
#          s.lower().count('e') +
#          s.lower().count('i') +
#          s.lower().count('o') +
#          s.lower().count('u'))

# print(count)
# 3-->
# l = [12,34,56,78,98,2,456,22,46,35,74]
# print(max(l))
# 4-->
# l = [12,34,56,78,98,2,456,22,46,35,74]
# l.sort()
# print(l[-2])
# 5-->
# string = input('string:')
# b = string[::-1]
# if string == b:
#     print('palindrome')
# else:
#     print('not a palindrome')
# 6-->
# list1 = [1,2,3,4]
# list2 = [5,6,3,8]
# print(list1 + list2)
# 7-->
# list = [1,2,3,4,2,1,3,4,5,3,2,3,4,7,5,2,3,5,6,5,3,2,4,65,4,3,4,5]
# count = 0
# a = int(input('value:'))
# for i in list:
#     if i == a:
#         count += 1
# print(count)
# 8-->
# tup = (12,34,56,78,98,2,456,22,46,35,74)
# list = list(tup)
# list.append(1000)
# print(list)
# CONDITIONS (if/else) - 10 Questions
# 1-->
# a = int(input('a:'))
# if a < 0:
#     print('negative')
# elif a > 0:
#     print('positive')
# else:
#     print('neither positive nor negative')
# 2-->
# num = int(input('num:'))
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')
# 3-->
# a = int(input('a:'))
# b = int(input('b:'))
# c = int(input('c:'))
# if a < b and b > c:
#     print(b,' is greatest')
# elif a > b and a > c:
#     print(a,' is greatest')
# else:
#     print(c,' is greatest')
# 4-->
# year = int(input('enter_year:'))
# if year % 4 == 0:
#     print('leap_year')
# else:
#     print('normal_year')
# 5-->
# num = int(input('enter num:'))
# if num % 3 == 0 and num % 5 == 0:
#     print('divisible')
# else:
#     print('not divisible')
# 6-->
# Assign grades based on marks (90+ A, 80+ B, etc.)
# marks = int(input('enter_marks:'))
# if marks >= 90:
#     print('grade = A')
# elif 90 > marks >= 80:
#     print('grade = B')
# elif 80 > marks >= 70:
#     print('grade = C')
# elif 70 > marks >= 60:
#     print('grade = D')
# else:
#     print('grade = FAIL')
# 7-->
# word = input('word:')
# if word[0] == 'a' or word[0] == 'A':
#     print('vowel')
# elif word[0] == 'e' or word[0] == 'E':
#     print('vowel')
# elif word[0] == 'i' or word[0] == 'I':
#     print('vowel')
# elif word[0] == 'o' or word[0] == 'O':
#     print('vowel')
# elif word[0] == 'u' or word[0] == 'U':
#     print('vowel')
# 8-->
# num = int(input('num'))
# if num % 7 == 0:
#     print('multiple of 7')
# else:
#     print('not multiple of 7')
# # 9-->
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# num3 = int(input('num3:'))
# if num1 > num2 < num3:
#     print(num2,' is smallest')
# elif num2 > num1 < num3:
#     print(num1,' is smallest')
# else:
#     print(num3,'smallest')
# 10-->
# num = int(input('num:'))
# if 10 <= num >= 50:
#     print('yes it is')
# else:
#     print('no it is not')
# LOOPS - 10 Questions
# 1-->
# a = 1
# while a <= 50:
#     print(a,)
#     a += 1
# 2-->
# a = 1
# while a <= 100:
#     if a % 2 == 0:
#         print(a)
#     a += 1
# 3-->
# n = int(input('n:'))
# sum = 0
# for i in range (1,n + 1):
#     sum += i
# print(sum)
# 4-->
# num = int(input('num:'))
# for i in range(1,11):
#     print(num,' X ',i,' = ', num * i)
# # 5-->
# num = int(input('num:'))
# digit = 0
# while num > 0:
#     digit += 1
#     num = num // 10 
# print(digit)
# 6-->
# num = int(input('num:'))
# rev = 0
# while num > 0:
#     dig = num % 10
#     rev = rev * 10 + dig
#     num //= 10
# print(rev)
# 7-->
# num = int(input('num:'))
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)
# 8-->
# a = 1
# while a <= 100:
#     if a % 2 == 0:
#         print(a)
#     a += 1
# 9-->
num = int(input('num:'))
sum = 0
while num > 0:
    dig = num % 10
    sum += dig
    num = num // 10
print(sum)