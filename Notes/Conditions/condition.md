# CONDITIONS
'''
🔸 if only (no else)
a = 3

if a > 5:
    print("Yes")

👉 Output: Nothing (condition is False)

🔸 if-elif-else (Multiple Conditions)
a = 10

if a < 5:
    print("Small")
elif a == 10:
    print("Equal to 10")
else:
    print("Large")

✔️ Output: Equal to 10
'''

# PRACTICE PROBLEMS

'''
*   Easy (1-5)
1.  Take a number and print "Even" or "Odd"
2.  Take a number and print "Positive" or "Negative"
3.  Take a number and check if it is greater than 10 or not
4.  Take a number and print "Zero" if it is 0, otherwise print "Not Zero"
5.  Take a number and check if it is divisible by 5

1 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
else:
    print('odd')
2-->
number = float(input('number:'))
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('neither positive nor negative')  

3 -->
number = float(input('number:'))
if number > 10:
    print('greater')
elif number == 10:
    print('equal')
else:
    print('smaller')

4 -->
number = int(input('number:'))
if number == 0:
    print('zero')
else:
    print("not zero")

5 -->
number = int(input('number:'))
if number % 5 == 0:
    print('devisiable')
else:
    print('not devisiable')


🟡 Medium (6-12)
6.  take a number and check:
if > 0 → "Positive"
if < 0 → "Negative"
if = 0 → "Zero"
7.  Take a number and check:
if divisible by 2 and 3 → "Divisible by both"
otherwise → "Not divisible by both"
8.  Take a number and check if it is between 10 and 20
9.  Take a string and check if it contains "a"
10. Take a number and check:
if even → print "Even"
else → print "Odd"

(yes similar — repetition builds strength)

11. Take two numbers and print larger one
12. Take three numbers and print largest

6 -->
number = float(input('number:'))
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('zero')  

7 -->
number = int(input('number:'))
if number % 2 == 0 and number % 3 == 0:
    print("divisible")
else:
    print('not divisible')

8 -->
number = float(input('number:'))
if 10 < number < 20:
    print("yes")
else:
    print('no')

9 -->
str = str(input('str:'))
if str.count('a') == 0:
    print('it doesnot has any a')
else:
    print('it does has a')

10 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
else:
    print('odd')

11 -->
list = [float(input('num1:')), float(input('num2'))]
print(max(list))

12 -->
list = [float(input('num1:')), float(input('num2:')), float(input('num3:'))]
print(max(list))


🔴 Hard (13-20)
13. Take marks and print grade:
90+ → A
75-89 → B
50-74 → C
<50 → Fail
14. Take age and check:
<18 → "Minor"
18-60 → "Adult"

60 → "Senior"

15. Take a number:
if divisible by 2 → print "Even"
if divisible by 3 → print "Div by 3"
16. Take username:
if it contains "admin" → print "Admin access"
else → "User access"
17. Take a number:
if even AND >10 → "Valid"
else → "Invalid"
18. Take password:
if length ≥ 8 → "Strong"
else → "Weak"
19. Take two numbers:
if equal → "Same"
else → "Different"
20. Take a number:
if >0 → check if even or odd
if <0 → print "Negative number"


13 -->
student_marks = float(input('marks:'))
if student_marks >= 90:
    print('A')
elif 75 <= student_marks <=89:
    print('B')
elif 74>= student_marks >= 50:
    print('C')
else:
    print('FAIL')

14 -->
age = int(input('age'))
if age < 18:
    print('minor')
elif 60 >= age > 18:
    print('ault')
else:
    print('senior')

15 -->
number = int(input('number:'))
if number % 2 == 0:
    print('even')
elif number % 3 == 0:
    print('divisible by 3')

16 -->
name = [str(input('name:'))]
if name.count('admin') > 0:
    print('admin excess')
else:
    print('user excess')

17 -->
number = int(input('number:'))
if number % 2 == 0 and number < 10:
    print('valid')
else:
    print('invilid')

18 -->
password = (input('pass:'))
if len(password) >= 8:
    print('strong')
else:
    print('weak')

19 -->
num1 = float(input('num1:'))
num2 = float(input('num2:'))
if num1 == num2:
    print('same')
else:
    print('not same')

20 -->
number = int(input('number:'))
if number > 0:
    if number % 2 == 0:
        print('even')
    else:
        print('odd')
elif number <0:
    print('negative')
