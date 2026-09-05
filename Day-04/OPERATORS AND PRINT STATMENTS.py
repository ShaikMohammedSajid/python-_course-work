Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
b = 20
print(a+b)
30
print(a-b)
-10
print(a*b)#multiplication
200
print(a/b)float point
SyntaxError: invalid syntax
print(a/b)#float
0.5
print(a//b)#no float point
0
print(a%b)#division
10
print(a**b)#square root
100000000000000000000
#THESE ALL ARE OPERATORS
__#
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    __#
NameError: name '__' is not defined
# COMPARISON OPERATOR
a = 20
b = 10
a<b
False
a>b
True
a<=b
False
a>=b
True
a<b
False
a==b
False
a!=b
True


#ASSINGMENT OPERATORS
a = 20
b = a + 10
b
30
b = a - 10
b
10
b = a ** 2
b
400
b%=2
b
0
b//2
0
b/3
0.0


#TRUE OR FALSE (RELATIONAL OPERATORS)
a = 10
a%2==0
True
a%3==0
False
a%2==0 and a%3==0#and TWO OF THEM SHOULD Be TRUE
False
a%2==0 and a%3==0#OR ETHIRE ONE OF THE SHOULD BE TRUE
False
not a%2==0      #not replace with TRUE = FALSE , FALSE = TRUE
False



#MEMBERSHIP OPERATORS:
a = [ 1,2,3,4,5]
2 in a
True
6 in a # 6 NOT THERE IN A SO THE ANSWER IS FALSE
False
4 in a
True
7 is not in a # IF WE ADD NUMBER THAT IS NOT IN VALUE,THEN WE ADD NOT IT WILL SHOE TRUE
SyntaxError: invalid syntax
7 not in a
True
b = ( 1,2 3,4) # TUPLE
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b = (1,2,3,4) # TUPLE
1 in b
True
2 not in b
False
c = { 1,2,3,4} # set
1 in c
True
5 not in c
True
d = {"name" : "sajid","age" : 21, "class" : 63}# HERE WE ONLY KEY FACTORS ARE TRUE AND THE VALUES BECOME FALSE
"name" in d
True
"sajid" in d # WE HAVE TAKEN VALUE SO IT BECOMES FALSE
False
#THE ABOVE ONE IS DICTONARY


#IDENTITY OPERATORS(IT CHECKS OBJECT REFERENCE OF BOTH ARE SAME OR NOT)
a = [1,2,3,4,5]
b = [1,2,3,4,5]
id(a)
2196633865088
id(b)
2196640756480
>>> a is b # IT COME FALSE BECAUSE BOTH IDS ARE NOT SAME
False
>>> a is not b # AS WE HAVE TAKEN NOT IT COMES TRUE
True
>>> # WE HAVE TO USE "IS" IN IDENTIFIC
>>> 
>>> 
>>> 
>>> 
>>> # MUTABLE = CHANGE IN SAME OBJECT REFERENCE
>>> #IMMUTABLE = CANT CHANGE IN SAME OBJECT REFERENCE/ EXPLATION : IF WE TAKE CODE LIKE L = (1,2,3,4) IF WE ADD ANOTHER NUMBER TO IT LIKE L =(1,2,3,4,5), THERE ALSO THE OBJECT REFERENCE NUM WILL BE SAME.
>>> # IN MUTABLE THE OBJECT NUM WIILL BE DIFFERET SO THEY ARE CALLED MUTABLE WHERE THE OBJECT REFERENCE NUM CAN BE CHANGE
>>> 
>>> 
>>> #"BIT WISE OPERATORS" ,MAIN ARE  LEFT SHIFT & RIGHT SHIFT
>>> 
>>> #RIGHTSHIFT = MEANS REMOVING VALUES
>>> 8>>2
2
>>> 8<<2
32
>>> #LEFTSHIOT = MEANS ADDING VALUES
>>> 8<<2
32
>>> 
>>> 
>>> #F STRING
>>> a = 210
>>> print(f"age of zaib is {a} old") #WE USE "F" FUNCTION WHEN WE WANT TO ADD NUM IN SENTENCE FORMAT
age of zaib is 210 old
>>> b = 21
>>> print(f"sajid is {a} years old")# we are using f string
sajid is 210 years old
>>> print(a,b,sep = "")
21021
>>> #up one is WONT GIVE SPACE
>>> print(a,b,sep = " ")
210 21
>>> print(a,b,sep = "\n")
210
21
>>> print(a,b,sep = "\t")
210	21
>>> #sep = "" (it WONT GIVE ANY SPACE)
>>> #SEP = " " (IT WILL GIVE YOU SPACE)
>>> #SEP = "\n"(IT WILL GIVE YOU DOWN )
>>> #SEP = "\T" (IT WILL GIVE YOU TAB SPACE)
