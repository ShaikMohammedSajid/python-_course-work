"""
def display(name,email,password):
    print(f"hello {name}")
    print(f"your email :{name}")
    print(f"your password:{password}")
display("sajid","sajid523@gmail.com","sajid@123")
display("Zaib","zaib@mail.com","zaib123")
"""
"""
def leap_year(year):
    if(year%400==0)or(year%4==0 and year%100!=0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")    
for year in range(2001,2027):
    leap_year(year)
    
def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n=n//10    
    return sum
n = int(input("enter your number :"))
print(f"sum of {n} digits is {sumofdigits(n)}")  

def productofdigits(n):
    pro = 1
    while n>0:
        pro *= n%10
        n=n//10    
    return pro
n = int(input("enter your number :"))
print(f"product of {n} digits is {productofdigits(n)}")  

def checkpassword(password):
    if len(password)>8:
        check =set()
        for i in password:
            if i.isupper():
                check.add("u")
            elif i.islower():
                check.add("l")
            elif i.isdigit():
                check.add("d")
            else:
                check.add("s")
        if len(check)==4:
            return "strong password"
        else:
            return "weak password"
password =input("enter your password:")
print(f"your password is {checkpassword(password)}")            
"""
def tabel(n):
    print(f"______________Tabel_{n}________________")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
for i in range(1,21):
    tabel(i)        

