Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [1,2,3,45,]
a.append(410)
a
[1, 2, 3, 45, 410]
>>> 
>>> 
>>> 
>>> a.insert(3,4)
>>> a
[1, 2, 3, 4, 45, 410]
>>> 
>>> 
>>> 
>>> a.extend([555,666])
>>> a
[1, 2, 3, 4, 45, 410, 555, 666]
>>> 
>>> 
>>> 
>>> a.pop(2)
3
>>>  #IT REMOVES FROM INDEX VALUE .POP()
>>> 
>>> 
>>> a.id(1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.id(1)
AttributeError: 'list' object has no attribute 'id'
>>> a.pop()
666
>>> # IF WE KEEP .POP() WITH OUT GIVING ANY VALUE IT RINTS LAST VALUE
>>> 
>>> 
>>> a.remove(3)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.remove(3)
ValueError: list.remove(x): x not in list
>>> a.remove(4)
>>> a
[1, 2, 45, 410, 555]
>>> 
>>> 
>>> a.clear()
>>> 
>>> a
[]
>>>  # IT CLEARS ALL THE VALUE AND GIVE US ONLYB BRAKECTS
...  
>>> 
>>> l = [1, 2, 3, 4, 45, 410]
>>> max(l)
410


min(l)
1


sorted(l)
[1, 2, 3, 4, 45, 410]


#SORTED IS USED AS A TEMPORAY FOR ASSENDING ORDER

l.sort()
l
[1, 2, 3, 4, 45, 410]
#SORT() IS USED FOR ARANGING IN ASSENDING ORDER PERMENANTLY


l.sort(reverse=True)
l
[410, 45, 4, 3, 2, 1]
#.SORT(REVERSE=TURE) IS UESD FOR REVERSE ORDER


sum(l)
465

#SUM() IS USED TO PLUS ALL THE VALUES


l = [1,2,3,4]
m = [1,3,4,5]
n = l
n.apppend(4)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    n.apppend(4)
AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
n.append(4)
n
[1, 2, 3, 4, 4]
m
[1, 3, 4, 5]

m = l.copy()
m
[1, 2, 3, 4, 4]
m.append(10)
m
[1, 2, 3, 4, 4, 10]
l
[1, 2, 3, 4, 4]

all([0,"",[],(),set(),{},True])
False
#ALL MEANS ALL THE VALUES SHOULD BER TURE

any([0,"",[],(),set(),{},True])
True

#ANY MEANS ANY VALUE CAN TRUE SO IT PRINT TRUE

l
[1, 2, 3, 4, 4]
l.index(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l.index(5)
ValueError: 5 is not in list
# because 5 is not in the index so IT IS COMING ERROR
l.index(4)
3


l.count(4)
2

#COUNT() IS USED TO COUNT THE VALUES OR THE CODE


NESTED LOOP MEANS LIST INSIDE THE LIST
SyntaxError: invalid syntax

3

l = [1, 2, 3, 4, 5],[6,7,8,89]
l
([1, 2, 3, 4, 5], [6, 7, 8, 89])
l[0]
[1, 2, 3, 4, 5]
#WE HAVE PRINTED O THE INDEX IS O

l[1]
[6, 7, 8, 89]

l[0][3]
4
# WE HAVE TAKEN THE INSIDE "O" INDEX THE SELECTED A PARTICULAR INDEX

l[1][3]
89

l[-1][-1]
89

#---------------> TUPEL <--------------------------------

