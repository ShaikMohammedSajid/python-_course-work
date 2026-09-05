Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,,12,324,9876,1234}
SyntaxError: invalid syntax

s = {1,2,3,4,12,324,9876,1234}
s
{1, 2, 3, 324, 4, 12, 1234, 9876}
s.add(1)
s.add(12.3)
s.add(2+3j)
s
{1, 2, 3, 324, 4, (2+3j), 12, 12.3, 1234, 9876}
s= {1,1,1,1,1,1}
s
{1}
1 = {10,20,30}
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a = {10,20,30}
b = {{1,2,3,4}
     a
     
SyntaxError: incomplete input
a
     
{10, 20, 30}
b
     
a = {10,20,30}
     
b = {1,2,3,4}
     
a
     
{10, 20, 30}
b
     
{1, 2, 3, 4}
a | b#union
     
{1, 2, 3, 20, 4, 10, 30}
a&b#intersection
     
set()
a & b #intersection
     
set()
a - b # IT WILL MINUS ALL THE VALUE FROM B
     
{10, 20, 30}

b - a #IT WILL MINUS ALL THE VALUE FROM A
     
{1, 2, 3, 4}

a ^ b # SYMETRIC DIFERENCE MEANS IT DOES NOT GIVE COMMON VALUES
     
{1, 2, 3, 4, 10, 20, 30}

{1}<=a # 1 VALUES ARE THERE IN A ARE NOT IF ITS THERE IT PRINTS TRUE
     
False

a = {1,2,3,4,5}
     
b = {3,5,7,9}
     
a.isdisjoint(b)
     
False
a.isdisjoint{9,10}
     
SyntaxError: invalid syntax
a.disjoint({9,10})
     
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.disjoint({9,10})
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint{9,10}
     
SyntaxError: invalid syntax
a.issuperset(b)
     
False
# A VALUE THERE IN A IF ITS NOT IT PRINTS FALSE
     
5 in a
     
True
7 in a
     
False
8 not in a
     
True
a
     
{1, 2, 3, 4, 5}
max(a)
     
5
min(a)
     
1
sum(a)
     
15
sorted(a)# REMBER WHEN WE USE SORTED IT GIVES VALUE IN "LIST".
     
[1, 2, 3, 4, 5]
a
     
{1, 2, 3, 4, 5}
b = a
     
b
     
{1, 2, 3, 4, 5}
b.add(12)
     
b
     
{1, 2, 3, 4, 5, 12}
a
     
{1, 2, 3, 4, 5, 12}
c = a.copy()
     
c.add(13)
     
c
     
{1, 2, 3, 4, 5, 12, 13}
a
     
{1, 2, 3, 4, 5, 12}
a.update({10,20,30})
     
a
     
{1, 2, 3, 4, 5, 10, 12, 20, 30}
#UPDATE IS USED TO ADD MANY VALUES
     
a.pop()
     
1
# POP IS USED TO RMOVE A PARTICULAR RANDOM VALUE
     
a.remove(12)
     
a
     
{2, 3, 4, 5, 10, 20, 30}
#REMOVE IS USED TO REMOVE A VALUE
     
a.discard(40)
     
a
     
{2, 3, 4, 5, 10, 20, 30}
a.discard(30)
     
a
     
{2, 3, 4, 5, 10, 20}
# DISCARD ALSO REMOVE VALUES BUT IF WE WANT TO REMOVE A VALUE THAT IS NOT IN LIST IT DOES NOT GIVE ERROE LIKE REMOVE
     
#SO WE MOSTLY PREFERB A.DISCARD()
     
a.clear()
     
a
     
set()
len(a)
     
0
a = {2, 3, 4, 5, 10, 20}
     
all(a)
     
True
any(a)
     
True

a = frozenset({1,2,3,4,15,20,410})
     
a
     
frozenset({1, 2, 3, 4, 20, 410, 15})
# FROZEN SET IN WE CANT ADD OR REMOVE ELEMENTS
     

#----------------------------> DICTONARY <---------------------------------------------------
     
d = {}
     
d = dict()
     
type(d)
     
<class 'dict'>

d = {"k1" : "v1" , "k2" : "v2" , "k3" : "v3"}
     
d
     
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
     
1366278421504
d["k4"] = "v4"
     
d
     
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}



#WE ADD VALUS LIKE ABOVE
     
d = ["k1"] = v11"
     
SyntaxError: unterminated string literal (detected at line 1)
d = ["k1"] = "v11"
     
SyntaxError: cannot assign to literal
d["k1"] = "v11"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# WE UPADTE THE VALUES LIKE ABOVE BUT THE KEY VALUE MUST BE SAME
     
d[1] = "int"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int'}
d[12.3] = "float"
     
d [12+4j] = "complex"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex'}
d["str"] = "string"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string'}
d(1,2,3,4) = "tuple"
     
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d[(1,2,3,4)] = "tuple"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d[froozenset({1,2,3,4})] = "fset"
     
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    d[froozenset({1,2,3,4})] = "fset"
NameError: name 'froozenset' is not defined. Did you mean: 'frozenset'?
d[frozenset({1,2,3,4,5})] = "fset"
     
d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple', frozenset({1, 2, 3, 4, 5}): 'fset'}


d
     
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple', frozenset({1, 2, 3, 4, 5}): 'fset'}
"str" in d
     
True
"list" in d
...      
False
>>> 
>>> d["float"]
...      
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    d["float"]
KeyError: 'float'
>>> #SEE THE ABOVE ERROR BECAUSE WE HAVE TAKEN ABOVE IS VLUE NOT KEY O ITS WHY IT IS SHOWING ERROR
...      
>>> d["int"]
...      
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d["int"]
KeyError: 'int'
>>> d[1]
...      
'int'
>>> # INSTED OF THE ABOVE METHOD WE USE ".GET()" IT WONT SHOW ERRORS LIKE ABOVE SO WE USE .GET() METHOD
...      
>>> 
>>> d.get("k1"0
...       
SyntaxError: incomplete input
>>> d.get(1)
...       
'int'
>>> d.get("k2")
...       
'v2'
>>> # USE .GET() SO I WONT SHOW ERRORS()
...       
>>> #IF WE WANT TO UPDATE ANY OF THE VALUE WE HAVE TO ACCES WITH  THE " KEYS "
...       
>>> d["k1"] = 12
...       
>>> d
...       
{'k1': 12, 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple', frozenset({1, 2, 3, 4, 5}): 'fset'}
>>> # JUST LIKE THAT WE CAN UPDATE THE VALUE BY USIG ONLY "KEYS"
...       
>>> 
>>> d["int"] = 1234
...       
>>> d
...       
{'k1': 12, 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 12.3: 'float', (12+4j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple', frozenset({1, 2, 3, 4, 5}): 'fset', 'int': 1234}
