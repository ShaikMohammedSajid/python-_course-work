#_____________________LOCAL AND GLOBAL VARIABEL____________________________


def display(n):
    n=n+10
    print("inside",n)
n = 10
display(n)
print("outside:",n)

#____________same variabel_______________
def display():
    print("inside:",n)
n =10
display()
print("outside:",n)


def display():
    n =10
    print("inside",n)
display()
print("outside",n)    

#IT SHOWS ERROR BECAUSE WE CANT GIVE INSIDE VALUE TO OUTSIDE VALUE
#BUT OUTSIDE VALUE CAN BE GIVEN TO INSIDE VALUE

def display():
    global n
    n =n +10
    print("inside",n)
n=10
display()
print("outside",n)
#IF WE USE "GLOBAL N" WE GET THE SAME VALUE IN GLOABLA AND LOCAL VARIABEL 

def display():
    global n
    n = "PFS"
    print("update course :",n)
n = "JFS"
display()
print("final course :",n)


def display():
    n= "JFS"
    def update():
        nonlocal n
        n = "PFS"
        print("updated course :",n)
    update()
    print("Final course :",n)
display()        
#WE USE " NONLOCAL " SO THAT WHEN WE ARE IN NESTEDLOPP EVERY THING IS GLOABL S0 TO CHANGE INSIDE VARIABEL  WE "NONLOCAL"abs 

"""
l = [1,2,3,4,5]
max =20
sum =10
print(sum)

