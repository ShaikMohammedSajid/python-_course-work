"""
f =open("txt2.py")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)

s = "ssajid is a boy"
f= open("txt3.py","w")
f.write(s)
f.close()

f = open("txt3.py")
f.read()

f.close()
"""
def greet(name,ending= "Thanks"):
    print("sajid")
    print(ending)
greet("sajid",)    