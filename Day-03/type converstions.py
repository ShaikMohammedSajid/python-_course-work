Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> print(float(a))
10.0
>>> print(complex(a))
(10+0j)
>>> print(str(a))
10
>>> print(list(a))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(list(a))
TypeError: 'int' object is not iterable
>>> print(tuple(a))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(tuple(a))
TypeError: 'int' object is not iterable
>>> print(set(a))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(set(a))
TypeError: 'int' object is not iterable
>>> print(dict(a))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(dict(a))
TypeError: 'int' object is not iterable
>>> print(bool(a))
True
>>> #FROM THE CONCEPT YOU SHOULD LEARN THAT
>>> # INT = FLOAT,COMPLEX,STR,BOOL.
>>> #COMPLEX = STR,FLOAT,INT,BOOL.
>>> #FLOAT   = STR,COMPLEX,BOOL,INT.
>>> #STR     = ALL ARE POOSIBEL IN THE STRING.
>>> #LIST    = STR,TUPLE,SET,BOOL.
>>> #TUPLE   = STR,LIST,SET,BOOL.
>>> #BOOL    = IF THE VALUE IS ABOVE 1 THEN IT IS TRUE , IF THE VALUE IS BELOW 0 THEN IT IS FALSE.
