# INT,STR,FLOAT,LIST,TUPEL,SET,DEICT,BOOL

 # INT,FLOAT,STR,TUPEL,BOOL - ARE IMMUTABEL THE INSIDE VALUE CHANGE BUT NOT OUTSIDE VALUE
 # LIST ,SET,DICT - ARE MUTABEL THE INSIDE AND OUTSIDE VALUE CHANGES

"""
def display(n):
    n =10.5
    print("inside",n)
n =10.9
display(n)
print("outside",n)

"""
def display(n):
    n = "language"
    print("inside",n)
n ="python"
display(n)
print("outside",n)    