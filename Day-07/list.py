Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
c = "string.py"
c.startswith("str")
True
c.endswith("py")
True
c.islower()
True
c.isupper()
False
"SAJID" .isupper()
True
c.isalpha()
False
#.ISALPHA() MEANS ALPHABATICAL ORDER
c.isalnum()
False
>>> #ISALNUM MEANS ALPHATBATES & NUMBER
>>> "s123".isalnum()
True
>>> "sajd.123".isalnum()#IT IS FALSE BECAUSE IT HAS SPECIAL CHARACTER LIKE ".",:@","#" OR ANYB SPECIAL CHARACTER
False
>>> "    ".isspace()
True
>>> #.isspace() check the space
>>> "r     ".isspace() # IT COMES FALSE BECAUSE IT HAS LETTTER IN IT
False
>>> 
>>> " SAJID IS A GOOD BOY".istitle()
False
>>> "This Is Sajid" .istitle()
True
>>> #LIST IS A COLLECTION OF ELEMENT THAT ARE STORED IN SQUARE BRACKEST
>>> #THEY FOLLOW ORDER #THEY ARE MUTABEL # THEY ARE DYNAMIC # ALLOWS DUPLICATE # IT IS HETEROGENIUS(LIST CAN CONTAIN DIFFERENT DATA TYPES LIKE ("INT,FLOAT,STR")
>>> a = []
>>> a= list[]
SyntaxError: incomplete input
>>> a= [1,2,3,2.3,3.4,"str",false]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a= [1,2,3,2.3,3.4,"str",false]
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> a = [1,2,3,4,"str
...      
SyntaxError: incomplete input
>>> a = [1,2,3,4,"str","true"]
...      
>>> a
...      
[1, 2, 3, 4, 'str', 'true']
>>> type(a)
...      
<class 'list'>
>>> a = [1,2,3,4]
...      
>>> b = [3,4,5,5]
...      
>>> a+b
...      
[1, 2, 3, 4, 3, 4, 5, 5]
>>> a**b
...      
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a**b
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'list'
