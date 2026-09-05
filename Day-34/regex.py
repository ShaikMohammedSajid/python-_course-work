import re
pattern = r'code'
text = "codegnan"
res = re.match(pattern,text)# match() just check it is  satring  is matching or not
print(res.group()if res else "pattern not found" )


import re
pattern = r'[0-9]'
text = "codegnan2026"
res = re.search(pattern,text)# search() is used to give only starting word 
print(res.group()if res else "pattern not found" )

import re
pattern = r'[0-9]'
text = "codegnan 2026 python version 3.14"
res = re.findall(pattern,text)# findall() finds all give us in this format ['2', '0', '2', '6', '3', '1', '4']
print(res)

import re 
patter = r"[0-9]"
text = "codegnan 2026 python version 3.14"
res = re.finditer(patter,text)#find iter() is used when u want to find out the output with index
for i in res:
    print(i.group(),i.start())

import re 
patter = r"[0-9] {10}"
text   = "987654321"
res = re.fullmatch(patter,text)#re.fullmatch() is used when you want to check whether the entire string matches a given pattern.

import re 
pattern = r"[,(#]"
text = "java,python,(htmal#css" 
res = re.split(pattern,text)# split() is used to split multiple patterns
print(res)

import re
text = "codegnan 2026 python version 3.14"
pattern = r"[0-9]"
res = re.sub(pattern,"*",text) #sub() is used to rpalce the values in text
print(res)

import re 
pattern = r"e.t"# here we have put "." we can add anything betwwen that "." like eat,ect
text = "e@t eaat eat eet ect ejndjd edmdkjkd"
res = re.findall(pattern,text)
print(res)

import re
pattern = r"^(91)"# ^ is used to check the starting values
text = "9198765432"
res = re.findall(pattern,text)
print(res)

import re
pattern = r"0$"# $ is used to check the ending  values is excaxt or not
text = "9198765432"
res = re.findall(pattern,text)
print(res)

import re
pattern = r"to+"# to+ + means u want minimum one zero to strat 
text = "to msdmdmnjdw too tooo toooooooo"
res = re.findall(pattern,text)
print(res)

import re
pattern = r"to*"# to* * means u dont need any particlular o or anything to start
text = "to msdmdmnjdw too tooo toooooooo"
res = re.findall(pattern,text)
print(res)

import re
pattern = r"ab+"# 
text = "ab abb abbb abbbbbb a "
res = re.findall(pattern,text)
print(res)

import re
pattern = r"91|0"# #| is used used to either this or that valuesz are present
text = "09876"
res = re.findall(pattern,text)
print(res)

import re
pattern = r["aeiou AEIOU"] #[] is used TO CHECK THE VALUES LIKE WITH IN [] THEY DONT DONT NEED BE SAME OR EXCATLY
text = "09876"
res = re.findall(pattern,text)
print(res)






