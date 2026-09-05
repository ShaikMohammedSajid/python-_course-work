Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#slicig

s = ""
s
''
s = "codegnan"
>>> s
'codegnan'
>>> s = "sajid" + "hyd"
>>> s
'sajidhyd'
>>> s*10
'sajidhydsajidhydsajidhydsajidhydsajidhydsajidhydsajidhydsajidhydsajidhydsajidhyd'
>>> 
...  
>>> #SLICING means EXTRACTING A PART OF SEQUENCE(SUCH AS STRING,LIST ,ARRAY)
>>> 
>>> s = "sajid and zaib are playing"
>>> s[0:6]
'sajid '
>>> s[0:]
'sajid and zaib are playing'
>>> s[0: : 2]
'sjdadzi r lyn'
>>> # AS WE TAKEN "STEP" AS 2 WE WILL GET ALL THE 2 WORD IN CODE
>>> #S = [START : END : STEP ]
>>> #THIS IS THE FORM OF SLICING
>>> 
>>> s [ : : -1]  # IF WE WANT TO DO IT IN REVERSE
'gniyalp era biaz dna dijas'
>>> s[-1:-10:-1]
'gniyalp e'
>>> s[-1:-10]
''
>>> s [ -1:-10:-1]
'gniyalp e'
>>> s[-8:-1]
' playin'
>>> s[-8:]
' playing'
>>> "sajid" in s
True
>>> zaib not in s
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    zaib not in s
NameError: name 'zaib' is not defined
>>> "zaib" not in s
False
>>> " saj " in s
False
>>> "saj" in s
True
>>> "taha" not in s
True
