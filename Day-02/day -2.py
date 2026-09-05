Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = " sajid"
>>> b = " is "
>>> c = " good"
>>> d = "boy"
>>> print(a + b + c + d)
 sajid is  goodboy
>>> print(a + d)
 sajidboy
>>> print( a ,end " " , b)
SyntaxError: invalid syntax
>>> a=b=c= 10
>>> print(a)
10
>>> print(C=b)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(C=b)
TypeError: 'C' is an invalid keyword argument for print()
