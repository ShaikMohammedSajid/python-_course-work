#to ittrate a sequence we use foor loop
"""
s= "python programing"
for i in range(len(s)):
    if s[i] in "aeiouAEIOU":
        print(i,s[i])
        """
"""
l = [23,44,12,34,50,24,35,68,75,34,10]
sum = 0
for i in range(len(l)):
    if l[i]%2==0:
        sum = sum+i
        print(i,l[i]) 
print(sum)              
"""
"""
sum = 0
for i in range (1,51):
    sum = sum +i
    if i%2==0:
        print(i)
print(sum)
"""
"""
n= int(input("ENTER YOUR NUMBER :"))
fact = 1
for i in range (1,n+1):
    fact = fact * i #fact *= i
    print(i)
print(f"factoriaol of {n} is {fact}")    
"""
"""
data={}
n = int(input("enter number of students :"))
max_marks = 0
for i in range (1,n):
    name = (input("Enter student name :"))
    marks =(int(input("Enter your Marks :")))
    if marks > max_marks:
        max_marks = marks
    data[name]  = marks
print(data)
print(f"maximum marks are {max_marks}") 
"""
dict ={}
n = int(input("enter the number of products :"))
sum = 0
for i in range (1,n):
    name = input("enter the product name :")
    price = int(input("enter the price of the product :"))
    quantity = int(input("enter the quantity of product :"))
    total = price*quantity
    sum = sum + total
    dict[name] = [price, quantity]
print(f"These are the list {dict}")
print(f"Total biil is {sum}")    


