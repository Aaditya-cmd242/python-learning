# LOOP
# for loop is used  when Iteration is definite like,
# for loop in range(start,end,step): # ending dosent prints
# list = [1,2,3,4]
# for loop in list:

# while loop is used when Iteration is undefinite because its workd on condition like,
# a = 1
# while True:
#     print(a)
#     a += 1
# # this code will print numbers till infinity because condition will never be false
# a = 1
# while False:
#     print(a)
#     a +=1
# # this code will not print anything because false conditions wont let code run

# nested loop
# for i in range (5):  this loop runs on condition
#     for j in range (i):   this loop runs on condition and between first loops every run like if first loop ran once then this will run and after its completely end next cycle of first loop will run 
#         print(i,end=' ') using end='' will print every thing in single line
#     print() using empty prints gives new line for first loop 


# loop control
# a = 1
# while a <= 10:
#     if a == 5:
#         break.    using break we breaks that loop whenever we wants 
#     print(a)
#     a += 1

# a = 1
# while a <= 10:
#     if a == 5:
#         a += 1
#         continue
#     print(a)
#     a += 1

# tup = (1,4,9,16,25,36,49,64,81,100)
# data = int(input('num:'))
# for i in tup:
#     a = False
#     if data in tup:
#         if data == i:
#             print(tup.index(data))
#     else:
#         a = True
# if a:
#     print('data is not in list')

# for i in range(5):
#     print(i)
# 0
# 1
# 2
# 3
# 4

# i = 5
# while i > 0:
#     print(i)
#     i -= 2
# 5
# 3
# 1

# for i in range(1, 5):
#     if i % 2 == 0:
#         continue
#     print(i)
# 1
# 3

# for i in range(3):
#     for j in range(2):
#         print(i + j)
# 0
# 1
# 1
# 2
# 2
# 3

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i, j)
# 0 1
# 2 0
# 2 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(i, j)
#         j += 1
#     i += 1
# # 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# for i in range(1, 4):
#     for j in range(1, i+1):
#         print(i, end="")
#     print()
# # 1
# # 22
# # 333

# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             continue
#         print(j, end="")
#     print()
# 0 2
# 0 2
# 0 2
# for i in range(2):
#     for j in range(2):
#         print(i, j)
#         if i == 0:
#             continue
#         print("X")
# 0 0
# 0 1
# 1 0
# X
# 1 1
# X