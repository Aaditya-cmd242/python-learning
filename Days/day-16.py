'''
🟢 LEVEL 1: VERY EASY (1-15)

Print numbers from 1 to 10

Print numbers from 10 to 1

Print even numbers from 1 to 20

Print odd numbers from 1 to 20

Print multiplication table of 5

Print sum of numbers from 1 to 10

Count how many numbers from 1 to 50 are divisible by 3

Print all numbers divisible by 5 between 1 and 100

Print squares of numbers from 1 to 10

Print cubes of numbers from 1 to 10

Print first 10 natural numbers using while loop

Print numbers from 1 to n (user input)

Print sum of first n numbers

Print numbers from n to 1

Print all numbers between two given numbers

🟡 LEVEL 2: EASY (16-30)

Find sum of even numbers from 1 to n

Find sum of odd numbers from 1 to n

Count digits in a number

Reverse a number

Find sum of digits of a number

Check if a number is palindrome

Print factorial of a number

Print Fibonacci series up to n terms

Find largest digit in a number

Count number of zeros in a number

Print multiplication tables from 1 to 10

Print numbers divisible by both 3 and 5

Find product of digits of a number

Check if number is Armstrong (basic level)

Print all factors of a number

🟠 LEVEL 3: MEDIUM (31-50)

Count how many factors a number has

Check if number is prime

Print all prime numbers from 1 to n

Print reverse of a string using loop

Count vowels in a string

Count consonants in a string

Find largest number in a list using loop

Find smallest number in a list

Count even numbers in a list

Count odd numbers in a list

Remove duplicates from list using loop

Find second largest number in list

Print common elements in two lists

Merge two lists without using built-in functions

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
'''

# Print numbers from 1 to 10
# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# Print numbers from 10 to 1
# a = 10
# while a >= 1:
#     print(a)
#     a -= 1

# Print even numbers from 1 to 20
# a = 1
# while a <= 20:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# Print odd numbers from 1 to 20
# a = 1
# while a <= 20:
#     if a % 2 == 1:
#         print(a)
#     a += 1


# Print multiplication table of x
# num =int(input('num:'))
# a = 1
# while a <= 10:
#     print(num,' x ',a,' = ',num * a)
#     a += 1

# Print sum of numbers from 1 to n
# n = int(input('n:'))
# a = 1
# sum = 0
# while a <= n:
#     sum += a
#     a += 1
# print(sum)

# Count how many numbers from 1 to 50 are divisible by 3
# a = 1
# count = 0
# while a <= 50:
#     if a % 3 == 0:
#         count += 1
#     a += 1
# print(count)

# Print all numbers divisible by 5 between 1 and 100
# a = 1
# while a <= 100:
#     if a % 5 == 0:
#         print(a)
#     a += 1

# Print squares of numbers from 1 to 10
# a = 1
# while a <= 10:
#     print(a ** 2)
#     a += 1

# Print cubes of numbers from 1 to 10
# a = 1
# while a <= 10:
#     print(a ** 3)
#     a += 1

# Print first 10 natural numbers using while loop
# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# Print sum of first n numbers
# n = int(input('n:'))
# a = 1
# sum = 0
# while a <= n:
#     sum += a
#     a += 1
# print(sum)

# Print numbers from n to 1
# n = int(input('n:'))
# while n >= 1:
#     print(n)
#     n -= 1

# Print all numbers between two given numbers
# num1 = int(input('num1:'))
# num2 = int(input('num2:'))
# for a in range(num1,num2 + 1):
#     print(a)

# Print all numbers between two given numbers
# n = int(input('n:'))
# a = 1
# sum = 0
# while a <= n:
#     if a % 2 == 0:
#         sum += a
#     a += 1
# print(sum)

# Find sum of odd numbers from 1 to n
# n = int(input('n:'))
# a = 1
# sum = 0
# while a <= n:
#     if a % 2 == 1:
#         sum += a
#     a += 1
# print(sum)

# Count digits in a number
# num = int(input('num:'))
# count = 0
# while num > 0:
#     count += 1
#     num = num // 10
# print(count)

# Reverse a number
# num = int(input('num:'))
# rev = ''
# a = 0
# while num > 0:
#     a = num % 10
#     rev += str(a)
#     num = num // 10
# print(rev)

# Find sum of digits of a number
# num = int(input('num:'))
# sum_of_digit = 0
# while num > 0:
#     sum_of_digit += num % 10
#     num = num // 10
# print(sum_of_digit)

# Check if a number is palindrome
# num = int(input('num:'))
# rev = ''
# num_new = num
# while num > 0:
#     rev += str(num % 10)
#     num = num // 10
# if str(num_new) == rev:
#     print('palindrome')
# else:
#     print('not palindrome')

# Print factorial of a number
# num = int(input('num:'))
# fact = 1
# a = 1
# while a <= num:
#     fact *= a
#     a += 1
# print(fact)

# Find largest digit in a number
# num = int(input('num:'))
# largest = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest:
#         largest = digit
#     num = num // 10
# print(largest)

# Count number of zeros in a number
# num = int(input('num:'))
# count = 0
# a = 0
# while num > 0:
#     a = num % 10
#     if a == 0:
#         count += 1
#     num = num // 10
# print(count)

# Print multiplication tables from 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,' x ',j,' = ',i * j,end='.  ')
#     print()

# # Print numbers divisible by both 3 and 5
# n = int(input('n:'))
# a = 1
# while a <= n:
#     if a % 3 == 0 and a % 5 == 0:
#         print(a)
#     a += 1

# Find product of digits of a number
# num = int(input('num:'))
# product = 1
# while num > 0:
#     product *= num % 10
#     num = num // 10
# print(product)

# Check if number is Armstrong (basic level)
# num = int(input('num:'))
# amst = 0
# newnum = num
# while num > 0:
#     digit = num % 10
#     amst += digit ** 3
#     num = num // 10
# if amst == newnum:
#     print('its armstrom')
# else:
#     print('its not armstrom')

# Print all factors of a number
# num = int(input('num:'))
# a = 1
# while a <= num :
#     if num % a == 0:
#         print(a)
#     a += 1

# Count how many factors a number has
# num = int(input('num:'))
# a = 1
# count = 0
# while a <= num:
#     if num % a == 0:
#         count += 1
#     a += 1
# print(count)

# Check if number is prime
# num = int(input('num:'))
# for a in range(2,num + 1):
#     prime = True
#     for b in range(2,a):
#         if a % b == 0:
#             prime = False
# if prime:
#     print('prime')
# else:
#     print('not prime')

# Print all prime numbers from 1 to n
# n = int(input('n:'))
# for i in range(2,n + 1):
#     prime = True
#     for j in range(2,i):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         print(i)

# Print reverse of a string using loop
# string = input('string:').lower()
# newstring = ''
# index = len(string)
# while index > 0:
#     newstring += string[index - 1]
#     index -= 1
# print(newstring)

# Count vowels in a string
# string = input('string:')
# vowel = 'aeiou'
# count = 0
# for i in string:
#     if i in vowel:
#         count += 1
# print(count)

# Count consonants in a string
# string = input('string').lower()
# vowel = ' aeiou'
# count = 0
# for i in string:
#     if i.isalpha()  not in vowel:
#         count += 1
# print(count)

# Find largest number in a list using loop
# lst = [19,24,523,114,53,13,1]
# largest = -999999999999999
# for i in lst:
#     if i > largest:
#         largest = i
# print(largest)

# Find smallest number in a list
# lst = [19,24,523,114,53,13,1]
# smallest = 99999999
# for i in lst:
#     if i < smallest:
#         smallest = i
# print(smallest)

# Count even numbers in a list
# lst = [19,24,523,114,53,13,1]
# count = 0
# for i in lst:
#     if i % 2 == 0:
#         count += 1
# print(count)

# Count odd numbers in a list
# lst = [19,24,523,114,53,13,1]
# count = 0
# for i in lst:
#     if i % 2 == 1:
#         count += 1
# print(count)

# Remove duplicates from list using loop
# lst = [1,4,2,1,3,5,3,1,3,5,3,2]
# nlst = []
# for i in lst:
#     if i not in nlst:
#         nlst.append(i)
# print(nlst)

# Find second largest number in list
# lst = [19,24,523,114,53,13,1]
# largest = 1
# second_largest = 0
# for i in lst:
#     if i > largest > second_largest:
#         largest = i
#     elif second_largest < i < largest:
#         second_largest = i
# print(second_largest)

# Print common elements in two lists
# lst1 = [1,2,3,4]
# lst2 = [3,4,5,6]
# lst3 = []
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             lst3.append(i)
# print(lst3)

# Merge two lists without using built-in functions
# lst1 = [1,2,3,4]
# lst2 = [3,4,5,6]
# lst3 = []
# for i in lst1:
#     lst3.append(i)
# for j in lst2:
#     lst3.append(j)
# print(lst3)

