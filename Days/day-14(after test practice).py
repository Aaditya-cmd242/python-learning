# '''
# Find the largest number in a list using loop only
# (No max(), no sorting)
# Reverse a string without using slicing
# Count number of vowels in a string
# Find the second largest number in a list
# (No sort(), no set())
# Check if a string is a palindrome using loop
# Count frequency of each element in a list
# (No dictionary, no count())
# Write a program:
# Check if a number is prime
# If prime → print all prime numbers till that number
# '''
# # 1-->
# # list =[1,3,5,7,9,8,6,7,5,3,2]
# # largest = 0
# # for i in list:
# #     if i > largest:
# #         largest = i
# # print(largest)

# # 2-->
# # string = input('string:')
# # index = len(string)
# # new_string = ''
# # for i in range(index):
# #     new_string += string[index - 1]
# #     index -= 1
# # print(new_string)

# # 3-->
# # word = input('word').lower()
# # count = 0
# # for ch in word:
# #     if ch in 'aeiou':
# #         count += 1
# # print(count)

# # 4-->
# # list = [1,3,5,7,9,8,6,7,5,3,2]
# # largest = 1
# # second_largest = 0
# # list1 = [second_largest,largest]
# # for i in list:
# #     if i > largest:
# #         largest = i
# #     elif second_largest < i < largest:
# #         second_largest = i
# # print(second_largest)

# # 5-->
# # string = input('string').lower()
# # new_string = ''
# # index = len(string)
# # for i in range(len(string)):
# #     new_string += string[index - 1]
# #     index -= 1
# # if string == new_string:
# #     print('palindrome')
# # else:
# #     print('not a palindrome')

# # 6-->
# # list1 = [1,3,5,7,9,8,6,7,5,3,2]

# # unique = []

# # # Step 1: get unique elements
# # for i in list1:
# #     if i not in unique:
# #         unique.append(i)

# # # Step 2: count frequency
# # for el in unique:
# #     count = 0
# #     for j in list1:
# #         if el == j:
# #             count += 1
# #     print(el, "→", count)

# # 7-->
# num = int(input('num:'))
# prime = 2
# prime_number = []
# for i in range(2,num + 1):
#     if num % 2 == 0:
        
#     else:
#         prime_number.append(i)
# print(prime_number)

# # num = int(input('num:'))
# # prime = 2
# # for i in range(2,num + 1):
# #     for j in range(2,i):
# #         prime = True
# #         if i % j == 0:
# #             prime = False
# #         if prime:
# #             print(i)