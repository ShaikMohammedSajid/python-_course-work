Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = 0410
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> c =410
>>> print(type(c))
<class 'int'>
>>> s = 22.4
>>> print(type(s))
<class 'float'>
>>> s = 1+j
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s = 1+j
NameError: name 'j' is not defined
>>> s = 1j
>>> print(type(s))
<class 'complex'>
>>> s = "sajid"
>>> print(type(s))
<class 'str'>
>>> s = ["rdj",1,2,3,4,5,22.3,22.2,"true"]
>>> print(type(s))
<class 'list'>
>>> a = ("bhai",1,1,1,22,22,33,22.3,22.3,[1,2,3,],[1,23])
>>> print(type(a))
<class 'tuple'>
>>> j = {1,2,3,"zaib"," is","gandu",22.2}
>>> print(j)
{' is', 1, 2, 3, 'gandu', 22.2, 'zaib'}
>>> print(type(j))
<class 'set'>
>>> i = {"name" : "sajid" , "class" : "unemployed" }
>>> print(i)
{'name': 'sajid', 'class': 'unemployed'}
>>> print(type(i))
<class 'dict'>
>>> d = none
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d = none
NameError: name 'none' is not defined. Did you mean: 'None'?
