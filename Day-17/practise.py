"""
f= open("myfile.txt")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
f.close()

st = "sajid is good boy"
f = open("myfiles.py","w")
f.write(st)
f.close()

f = open("myfile.txt")
data = f.read()
print(data)
f.close()

import random
def game():
    print("You are playing a game")
    score = random.randint(1,62)
    with open("txt3.py")as f:
"""

word="bad"
with open("txt3.py","r") as f:
    content = f.read()
newcontent = content.replace(word, " good")   
with open("txt3.py","w") as f:
    f.write(newcontent) 
    



