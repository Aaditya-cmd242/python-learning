#tuple
"""
* tuple is mostly represented by collection of data divided by commas such as 1, 2, 3, 4 is tuple (1, 2, 3, 4) is also a tuple (1,) is also a tuple
* there are many rules and functions which are similar to list in tuple but tuple is far eassier than list it has its own rules too
* tuple is immutable
* tuple can also store collection of data 
* tuple has indexing system same as list such as starting index will be 0 and negative index will be from -1 and their functions too
* even slicing is same in tuple as list 
* since tuple is immutable so only printed data can be change but orignal cant be 
* addition and repatitation is valid in tuple and list where substration like oprations will give error
.   t_1 = (1, 2, 3)
    t_2 = (3, 4, 5)
    t_1 + t_2 = (1, 2, 3, 3, 4, 5)
    t_1 * 2 = (1, 2, 3, 1, 2, 3)
this function can be use in list as well as tuple and by using this function we can use selective oprations on tupple and list by respective rule
.   print(t_1.count)
this function can be use in list as well as tuple and by using this function we can count the data has been repeated in spefic tuple or list
.   print(t_1.index[])
this function can be use in list as well as tuple and by using this function we can find index value of spefic data

"""

# [a, b, c, d, e]= ('adi', ' yash', ' divu', ' chetu', ' sumit')
# z = [a, b, c, d, e]
# print(z[1])

# t_1 = (1, 2, 3)
# t_2 = (1, 2, 3)
# print(t_1 * 2)

#important rules for list and tuple
"""
example list and tuple =>
                        l1 = [1, 2, 3, 4, 5, 6, 7, 8]
                        l2 = [8, 5, 6, 4, 7, 2, 3, 1]
                        t2 = (a, b, c, d, e, f, h, i)
1.  l1.insert(index value,data)
by using this function we can add data into list on spefic location example =>
l1.insert(5,'adi')
print(l1)
2.  l1.append()
by using this function we can add data into list example =>
l1.append(9)
print(l1)
3.  l1.extend(data)
by using this function we can add multiple data into list exampl =>
l1.extend((9, 10, 11))
print(l1)
4.  l1.remove(data)
by using this function we can remove spefic data from list example =>
l1.remove(2)
print(l1)
5.  l1.pop(index value)  
by using this function we can remove data from spefic place example =>
l1.pop(3)
print(l1)
6.  l1.clear()
by using this function we can clear whole list example =>
l1.pop(3)
print(l1)
7.  l1.index()
by using this function we can find index value of spefic data example =>
print(l1.index(2))
8.  l1.sort()
by using this function we can sort list in accending order by defolt example =>
l2.sort()
print(l2)
9.  l1.count()
by using this function we can count number of times that data has repeated in list example =>
print(l2.count(3))
10. l1.reverse()
by using this function we can mirror the list in reverse form example =>
l1.reverse()
print(l1)
11. b = l1.copy()
by using this function we can copy data of l1 into l3 but when we make changes in l3 it will not affect l1,
unlike when we directly assin value of l1 into l3 and make changes in l3 it will happen in l1 too example =>
l1 = l3
print(l3) #it will give [1, 2, 3, 4, 5, 6, 7, 8]
l3.append(1000) # this change will stare in l1 too
print(l1) # this will give [1, 2, 3, 4, 5, 6, 7, 8, 1000]
but when we dont want l1 to change we can use .copy() function 
l3 = l1.copy()
print(l3)
l3.append(1000)
print(l3)
print(l1)

* this functions are exclusive to list except 2

1.  t2.index
by using this function we can find index of spefic data in tuple
2.  t2.count
by using this function we can find period of data in tuple
"""
# l1 = [1, 2, 3, 4, 5, 6, 7, 8]
# l2 = [8, 5, 6, 4, 7, 2, 3, 1]
# t2 = ('a ', 'b ', 'c ', 'd ', 'e ', 'f ', 'h ','i ')
# l3 = l1.copy()
# print(l3)
# l3.append(1000)
# print(l3)
# print(l1)

#x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
#sequence type is complete here
#x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x

#numeric type (3)
"""
1.  integer(int)
.   all types of number except imaginary number and number with decimal
2.  float
.   all number with decimal
3.  complex
.   all imaginary number
"""

#integer (mainly 4 types)
"""
* decimal number
natural number such as 7, 8, -2, -4, 0, etc
* binary number
binary number system uses two digits 0 and 1 
binary -> decimal

binary number has base 2 and position of number as power and we counts position of power from 0 to infinite and we starts by unit degit to higher digits
| Position  | Power of 2 | Value |
| --------- | ---------- | ----- |
| Rightmost | 2⁰         | 1     |
| Next      | 2¹         | 2     |
| Next      | 2²         | 4     |
| Next      | 2³         | 8     |
| Next      | 2⁴         | 16    |
question1 10 binary -> ? decimal

1 * 8   = 8
0 * 4   = 0
1 * 2   = 2
0 * 1   = 0
----------------
Total   = 10

question2 11001 binary -> ?decimal
| Digit | Position | Power of 2 | Value     |
| ----- | -------- | ---------- | --------- |
| 1     | 0        | 2⁰ = 1     | 1 * 1 = 1 |
| 0     | 1        | 2¹ = 2     | 0         |
| 0     | 2        | 2² = 4     | 0         |
| 1     | 3        | 2³ = 8     | 8         |
| 1     | 4        | 2⁴ = 16    | 16        |
16 + 8 + 1 = 25

decimal -> binary => for example [question1 convert 10 decimal into binary, question2 convert 25 decimal into binary ]

question1
10 % 2 = 0
5 % 2 = 1
2 % 2 = 0
1 % 1 = 1
ans. 1010 -> 0b1010

question2
25 % 2 = 1
12 % 2 = 0
6 % 2 = 0
3 % 2 = 1
1 % 1 = 1
ans. 11001 -> ob11001

* octalnumber
Octal = Base 8 number system

Uses digits: 0 to 7 only
Base = 8

👉 So numbers like:

0, 1, 2, 3, 4, 5, 6, 7 ✅
8, 9 ❌ (not allowed in octal)

| Position  | Power of 8 | Value |
| --------- | ---------- | ----- |
| Rightmost | 8⁰         | 1     |
| Next      | 8¹         | 8     |
| Next      | 8²         | 64    |
| Next      | 8³         | 512   |

octal -> decimal

Example: 12 (octal)
1 * 8¹ = 8
2 * 8⁰ = 2
👉 8 + 2 = 10 -> 0o10

decimal -> octal
10 decimal -> octal
10 ÷ 8 = 1 remainder 2
1 ÷ 8 = 0 remainder 1
and. 12 -> 0o12

* hexnumber

"""


# x-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-x
# practice
'''
1. String

Reverse a string
👉 Input: "python"
👉 Output: "nohtyp"
'''
# a = 'python'
# print(a[::-1])

'''
2. List

Find the largest number in a list

a = [3, 7, 2, 9, 5]
'''

# a = [3, 7, 2, 9, 5]
# a.sort()
# print(a[4])

'''
What will be the output?

t = (1, 2, 3)
print(t[1])
'''
# ans. 2

'''
4. Arithmetic

What is the output?

print(10 // 3)
print(10 % 3)
'''
# ans. 3 and 1

'''
5. String

Count vowels in a string
👉 "education"
'''
# a = (input("name:"))
# b = a.count('a')
# c = a.count('e')
# d = a.count('i')
# e = a.count('o')
# f = a.count('u')
# count_of_vowels = b + c + d + e + f
# print(count_of_vowels)

'''
7. Mixed

Convert binary to decimal manually:

👉 1011 = ?
'''

# ans. 11

'''
8. List + Logic

Find sum of all numbers:

a = [1, 2, 3, 4, 5]
'''
# a = [1, 2, 3, 4, 5]
# print(sum(a))

'''
10. Challenge 🔥

Write a small program:

👉 Take a list
👉 Print:

largest number
smallest number
sum
'''

# list = [111, 275, 4368, 326, 12, 852, 572, 25638, 2437, 1528 ,2639 , 162 , 162 , 1826]
# list.sort()
# # print(len(list) -1)
# largest_number = list[13]
# smallest_number = list[0]
# sum_of_list = sum(list)
# print(largest_number)
# print(smallest_number)
# print(sum_of_list)
