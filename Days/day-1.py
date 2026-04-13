#Using # can commentout a whole sentence
"""
using double 
Quote three times commentouts
a paragraph""" #this is not actually a comment but string but untill we assin this paragraph in variable python ignores it
#using command_key + / can commentout whole sentence

#syntax
#print("aditya") #using function print("") we can print anything

# datatype (7)
"""
1. sequence type (3)
.   string(str):- text data and can be represent by writing any data in double quotes, exampe => "aditya", "19", etc.
.   list:- list is a function which helps to keep collaction of same information simultaneously and can be change later and can be represent by writing data in [], example => name = [aditya, yash, chetanaya, divyansh]
.   tuple:- tuple is a function which helps to keep collaction of same information simultaneously and cannot br change later and can be represent by writing data in (), example => name (aditya, yash,chetanaya, divyansh)
2. Numeric Types (3)
.   intiger(int):- any number without decimal, example => 1,2,3
.   float:- any number with decimal, example => 1.0,2.3,4.7
.   complex:- real number + imaginary number, example 2 + 3i
3. Set Types (2)
.   set
.   frozonset
4. Mapping Type (1)
.   dictionary(dict)
5. Boolean Type (1)
.   bool:- true or fase
6. Binary Types (3)
.   bytes
.   bytearray
.   memoryview
7. None Type (1)
.   none:- data whose value is none
"""
#we can check types by using function       print(type())
#we can change type of function using name of function and (), example:- str(), int(), float(), etc

# basic oprations
"""
string can only be added into string, example => "aditya" + "yash" will give adityayash but "aditya" + 19 will give error
intiger can be added into intiger and float, example => 10 + 22.44 will give 32.44
"""


#practice
"""
price_of_apple = 0.99
a = price_of_apple
price_of_banana = 1
b = price_of_banana
price_of_mangoes = 2
c = price_of_mangoes
name = "aditya"
age = 19
list_of_shoping = ["apple", "banana", "mangoes"]
total_bill = a + b + c
print( name + " " + str(age) + " " +  str(total_bill))
"""

#string 
"""
* all text data is string type data
* string can be represented by writing data in single quote and double quotes example =>
'aditya is 19 year old'
"aditya is 19 year old"
* string is immutable after creating a string you cannot change it
* by using function len() we can find length of a string

* basic functions of string

.   print(a.lower()) 
.   print(a.upper())
using this function we can all cap and uncap string
.   print(a.strip)
.   print(a.lstrip())
.   print(a.rstrip())
using this function we can remove extra space from anyside in string
.   print(a * 3)
using this function we can decide how many times string should be repeat
.  print(a.replace("data we want to change", "data we want to change into"))
using this function we can change spefic data from string into result
.   print(len())
using this function we can find length of a string
.   print(a.find())
using this function we can find location of any data in string
.   print("data we need to find" in str)
using this function we can find if that data is present in str
.   a = ''' multi
line 
string'''

using thriple quotes we can assin multi line string into a variable
"""

#list
"""
* list is collection of multiple data to make it organized
* by using []we can make list of data, example => [1, 2, 3, 4] and [adi, yash, chetan, divu] and [aditya, 19]
* all data gets stored in form of index value of list 
* indexing starts from 0 to n number
* list are mutable 
.   list_1 =[aditya, yash, divu, chetu]
.   len(list_1)
by using this function we can know length of list
.   len(list_1) -1
by using this function we can find max index number
.   print(list_1[index value])
by using this function we can take data of spefic place from list
.   list_1[2] = sumit
by using this function we can mutate data of spefic place in list
* there is negative indexing too in python
* negative indexing starts from -1 where normal indexing starts from 0
* negative indexing means position od data in list from last to start

#slicing in list
* selecting multiple data from list
example list => list_2 = [10, 20, 30, 50, 50, 60, 70, 80, 90, 100]
.   print(list_2[start:end])
.   print(list_2[:end])
.   print(list_2[start:])
.   print(list_2[start:end:size of step])
.   print(list_2[-7:-2])
.   print(list_2[])
"""
# list_1 =['aditya ', 'yash ', 'divu ', 'chetu ']
# print(len(list_1) -1)
# list_2 = [10, 20, 30, 50, 50, 60, 70, 80, 90, 100]
# print(list_2[-1:-11:-1])

print(int(5.9))
