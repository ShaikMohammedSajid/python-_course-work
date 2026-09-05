Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = " python programing"
>>> len(c)
18
>>> ord("p")
112
>>> ord("a")
97
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> min(C)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    min(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
>>> min(c)
' '
>>> max (c)
'y'
>>> sorted(c)
[' ', ' ', 'a', 'g', 'g', 'h', 'i', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
>>> # SORTED IS A TUPLE FORMAT
>>> c = " sajid is a good boy"
>>> c.uppere()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c.uppere()
AttributeError: 'str' object has no attribute 'uppere'. Did you mean: 'upper'?
>>> c.upper()
' SAJID IS A GOOD BOY'
>>> # .UPPER() IS USED FOR ALL UPER CASE
>>> 
>>> c.lower()
' sajid is a good boy'
>>> # .LOWER() IS USED FOR LOWER CASE
>>> 
>>> c.tittel()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    c.tittel()
AttributeError: 'str' object has no attribute 'tittel'. Did you mean: 'title'?
>>> c.title()
' Sajid Is A Good Boy'
>>> # TITLE IS USED FOR "STARTING LETTER" UPPER CASE
>>> 
>>> c.swapcase()
' SAJID IS A GOOD BOY'
# .SWAPECASE() IS USED FOR TRUING UPPER CASE TO LOWER & LOWER CASE TO UPPER


KeyboardInterrupt
"SVAVSHBDMBDZSHGVS".casefold()
'svavshbdmbdzshgvs'
# .CASEFOLD() IS USED FOR TRUNING SPECIAL CHARCTERS IN TO NORMAL

c.center(40,"*")
'********** sajid is a good boy**********'
c.center(60,"-")
'-------------------- sajid is a good boy--------------------'
# CENTER IS USED FOR  MAKING YOUR VARIABLE IN THE MIDDEL

c.ljust(60,"*")
' sajid is a good boy****************************************'
# ljust() is used to print from left

c.rjust(60,"_")
'________________________________________ sajid is a good boy'
# is to uesd to fiil from the right side

"12".zfill(4)
'0012'
#IF THE VALUE IS GREATER IT FILLS 0 ,OTHER WISE IT WONT FILL ANY ZERO LIKE THIS
"1,2,3,4" z.fill(4)
SyntaxError: invalid syntax
"1,2,3,4".zfill(4)
'1,2,3,4'

c.find("j")
3
#.FIND() IS USED TO FIND THE INDEX OF THE VALUE

c.rfind("d")
15
# .RFIND() IS USED TO FIND THE INDEX FROM THE REVERSR

c.index("i")
4
#.INDEX() IS USED FIND THE INDEX OF NUM BUT IF THE INDEX VALUE IS NOT PRESENT IT WILL SHOW U ERROR
#BUT IN .FIND()  IT SHOW U -1 VALUE IF VALUE INS NOT THERE

c.rindex("g")
12
#.rindex() means it start from reverse and give reverese index values

c.count("a")
2
#.COUNT() IS USED TO COUNT OF PARTICAL CHARACTER LIKE I HAVE TAKEN "A" IT SHOWED ME 2


c.replace("s","m")
' majid im a good boy'
# .REPLACE() IS USED TO REPLACE A [ARTICALR VARIABEL

c.replace("sajid " , " zaib")
'  zaibis a good boy'

c.maketrans("aeiou","1,2,3,4,5")
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    c.maketrans("aeiou","1,2,3,4,5")
ValueError: the first two maketrans arguments must have equal length
c.maketrans("aeiou", "12345")
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
#it gives us in decimal format and then it need to be converted

c.translate(c.maketrans("aeiou", "12345"))
' s1j3d 3s 1 g44d b4y'
# C.TRANSLATE() IS USED TO TRANSLATE THE" AEIOU" IN TO "12345"



c.split()
['sajid', 'is', 'a', 'good', 'boy']
#.split() is used to split all thhe parts

c.split("*")
[' sajid is a good boy']
# .SPLIT() IN () WHAT WE GIVE ITV SPLIT LIKE THAT

c.rsplit(" ," ,"1")
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    c.rsplit(" ," ,"1")
TypeError: 'str' object cannot be interpreted as an integer
c.rsplit(", " 1)
SyntaxError: invalid syntax. Perhaps you forgot a comma?


s = """ python
programing
language"""
s
' python\nprograming\nlanguage'
# if you printhout .splitline() the out will be like above.
s.splitline()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    s.splitline()
AttributeError: 'str' object has no attribute 'splitline'. Did you mean: 'splitlines'?
s.splitlines()
[' python', 'programing', 'language']



".join([' python', 'programing', 'language'])
SyntaxError: incomplete input
" ".join([' python', 'programing', 'language'])
' python programing language'
"".join([' python', 'programing', 'language'])
' pythonprograminglanguage'
# FISR WE GAVE ' ' IT PRINTED SPACE BETWEEN THEM AFTER THAT WE HAVE GIVEN "" NO SPAXCE IS PRINTED

c = "java , python, numpy"
c.partition(",")

# IS USED TFOR PARTATION ,PARTITION IS SPLIT IN ONLY 3 FORM


c.strip()
("     java       python        numpy"     )
# .strip() is used to give more space

c.rstrip()
("java    python      numpy"       )
#.rstip() IS USED TO REMOVE RIGHT EXTRA SPACE


c.lstrip()
("     java        python   numpy")
#.lstrip is used to remove the left extra space"



#Encoding & Decoding Methods

c  = text = "Hello नमस्ते 你好 café ".encode()
c'heelo"\xfo\x90\x99\x92"
#.encode() is used to form a separate code like format


c.decode()
"Hello नमस्ते 你好 café "
# .decode() is used to decode the uncode() that we used in encode()









