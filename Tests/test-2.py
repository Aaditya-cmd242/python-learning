'''
🧪 Python Test (Structured Evaluation)
⏱️ Time Limit: 60 minutes
📊 Total Marks: 100

Q1. (5 marks)
Create a list of 5 numbers and print the largest number using a loop.

Q2. (5 marks)
Check whether a number is even or odd.

Q3. (5 marks)
Create a tuple and print first and last element.

Q4. (5 marks)
Create a set with duplicate values and print only unique values.


Q5. (5 marks)
Count numbers greater than 10 in a list.

Q6. (5 marks)
Print multiplication table of a number (1–10).

Q7. (5 marks)
Find sum of elements in a list using loop.

Q8. (5 marks)
Find union and intersection of two sets.

Q9. (5 marks)
Check if a number exists in a list.

Q10. (5 marks)
Reverse a string without slicing.

Q11. (5 marks)
Count vowels in a string.

Q12. (5 marks)
Print all even numbers from a list.


Q13. (5 marks)
Remove duplicates from a list without using set().

Q14. (5 marks)
Find second largest number in a list.

Q15. (5 marks)
Check if a string is palindrome using loop.

Q16. (5 marks)
Find common elements between two lists without set.

Q17. (5 marks)
Print pattern:

*
**
***
****
*****

Q18. (5 marks)
Count frequency of each element without dictionary.


Q19. (5 marks)
Modify list:

even → square
odd → cube

Q20. (5 marks)
Check prime number

print all primes till that number
'''
# 1-->
# list = [4,2,1,3,5,9,7]
# list1 = [-9999999999999999999]
# for i in list:
#     for j in range(i):
#         if i > j and i not in list1:
#             list1[0] = i
# print(list1)

# 2-->
# num = int(input('num:'))
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 3-->
# tuple = (1,2,3,4,5,6,7,8,9)
# print(tuple[0], tuple[-1])

# 4-->
# set = {1,2,3,2,1,4,5,6,34,2,4,6,7,4,2,4,6,4}
# print(set)

# 5-->
# list = [1,2,21,3,4,544,34,543,29,9]
# count = 0
# for i in list:
#     if i > 10:
#         count += 1
# print(count)

# # 6-->
# num = int(input('num:'))
# for i in range (1,11):
#     print(num,' x ',i,' = ',num * i)

# 7-->
# list = [1,2,21,3,4,544,34,543,29,9]
# sum = 0
# for i in list:
#     sum += i
# print(sum)

# 8-->
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# set3 = set1 | set2
# set4 = set1 & set2
# print('uniun:-',set3,'intersection:-',set4)

# 9-->
# list = [1,2,21,3,4,544,34,543,29,9]
# print(3 in list)

# 10-->




# 11-->
# string = input('string:').lower
# count = 0
# for i in string:
#     print(i)



# 12-->
# list = [1,2,21,3,4,544,34,543,29,9]
# new_list = []
# for i in list:
#     if i % 2 == 0:
#         new_list.append(i)
# print(new_list,end=', ')

# # 13-->
# list = [1,2,3,21,2,3,4,43,2,1,2,43,4]
# result = []
# for i in list:
#     if i not in result:
#         result.append(i)
# print(result)

# 14-->
# list = [1,2,21,3,4,544,34,543,29,9]
# list1 = list.sort()
# print(list[-2])

# 15-->
# string = input('string:')
# result = ''




# 16-->
# list1 = [1,2,3,4]
# list2 = [3,4,5,6]
# list3 = []
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print(list3)

# # 17-->
# num = int(input('num'))
# for i in range(1,num + 1):
#     print('*' * i)

# 18-->
# dict is out of syllabus in this test

# 19-->
# list1 = [1,2,3,4]
# list2 = []
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i ** 2)
#     else:
#         list2.append(i ** 3)
# print(list2)

# 20-->
# num = int(input('num:'))
# list = []
# for i in range(2,num):
#     if num % i == 0:
#         continue
#     elif 
#         list.append(i)
# print(num,list)