Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input()
sajid
name
'sajid'
name = input("enter your name :")
enter your name :sajid
age = int(input("enter your age:"))
enter your age:21
# ABOVE IS INT VALUE WHEN WE ARE TALKING NUMBER WE HAVE TO USE "INT"
price = float(input("enter the price:"))
enter the price:99.9
#ABOVE "FLOAT" IS USED FOR FLOATING POINT VALUES.

names = input("ENTER YOUR NAMES :").split()
ENTER YOUR NAMES :sajid zaib kareem
names
['sajid', 'zaib', 'kareem']
# "SPLIT" IS USED FOR SPLITING THE VALUES


map(int,names)
<map object at 0x000002ABE9376D70>
#MAP IS LAZY SO IT SHOW OBJECT WE HAVE CONVERT IT IN TO STR

values = list(map(int,input("Enter your names:").split()))
Enter your names:sajid sahl zaib
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    values = list(map(int,input("Enter your names:").split()))
ValueError: invalid literal for int() with base 10: 'sajid'
# ABOVE IS WRONG BECAUSE WE HAVE GIVEN "INT " AND HAVE PERFORMED "STR" FUNCTION

values = list(map(float,input().split()))



values = tuple(map(int,input().split()))
SyntaxError: multiple statements found while compiling a single statement
values = list(map(float,input().split()))



values = tuple(map(int,input().split()))
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax
email,password = input("Enter your mail and password").split()
Enter your mail and passwordsajid 12345
email
'sajid'
password
'12345'
>>> a,b,c = list(map(int,input().split()))
1,2,3,
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a,b,c = list(map(int,input().split()))
ValueError: invalid literal for int() with base 10: '1,2,3,'
>>> a,b,c = list(map(int,input().split()))
1 2 3 
>>> a
1
>>> b
2
>>> c
3
>>> 
>>> name,marks = input("enter your name and marks").split()
enter your name and markssajid 99
>>> name
'sajid'
>>> marks
'99'
>>> int(marks)
99
>>> # WE CANT ADD "INT" & "STR" AT THE SAME TIME SO WE HAVE USE AGAIN "INT" SO WE =CAN COVERT IT INTO "INT".
>>> 
>>> 
>>> #EVAL FUCTION
>>> e = eval(input())
123.4
>>> e
123.4
>>> e = eval(input())
2*4+3*8
>>> e
32
>>> e = eval(input("enter the data:"))
enter the data:{sajid,sajiz,gadda}
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    e = eval(input("enter the data:"))
  File "<string>", line 1, in <module>
NameError: name 'sajid' is not defined
>>> data = eval(input("Enter list: ")) 
... print(data)
SyntaxError: multiple statements found while compiling a single statement
>>> data = eval(input("Enter list: "))
Enter list: (1,2,3,4,)
>>> data = eval(input("Enter list: "))
Enter list: [1,2,3,4,]


