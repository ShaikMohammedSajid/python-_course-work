"""
n = int(input("enter number of stars :"))
m =n//2
for i in range (n):
    for j in range(n):
        if (j==0) or (j==n-1) or (i==n and i<=m) or (i+j==n-1 and i>=m):
            print("*",end =" ")
        else:    
            print(" ",end =" ")
    print()

greater = lambda a,b : a if a>b else b
print(greater(12,13))
print(greater(12,14))
print(greater(15,18))
print(greater(19,30))


wish = lambda name : f"welcome to the course {name}"
print(wish("sajid"))
print(wish("zaib"))
print(wish("mukesh"))

iseven = lambda n : "even" if n%2==0 else "odd"
print(iseven(45))
print(iseven(18))
print(iseven(25))


avg = lambda a,b,c : (a+b+c)/3
print(avg(4,5,6))
print(avg(10,20,30))


domain = lambda mail: (mail.split("@")[-1].split(" ")[0])   
print(domain("sajid@codegyan.com"))     
print(domain("sajid@gmail.com"))     
print(domain("sajid@yahooh.com"))     
print(domain("sajid@kingofpirates.com"))     

gst = lambda price : price + price* 0.18
print(gst(1000))
print(gst(2000))
print(gst(4000))

# "MAP" FUNCTION IS USED WHEN WE WANT TO USE ALL THE INPUT VALUSES WE USE MAP()

price =[123,345,678,900,1234,432,410]
result=list(map(lambda price: price+ price*0.18,price))
print(result)

names = ["sajid","zaib","dheeraj","sathvik","ruhan"]
res = list(map(lambda names : names.title(),names))
print(res)

names =[123,345,678,900,1234,432,410]
res = list(map(lambda names : names -names*0.3,names))
print(res)


# "FILTER IS USED TO FILTER ALL ELEMENTS AND SHOW THE RESULTS ACCORDING TO THE STATEMENT"
names = [123,345,678,900,1234,432,410]
res = list(filter(lambda names : names>500,names))
print(res)# ITS SHOW ALL THE GREATER VALUES ,WE AHAVE USED FILTER

names = [123,345,678,900,1234,432,410]
res = list(filter(lambda names : names<500,names))
print(res)# IT SHOWS ALL THE LESSSER VALEUES BECAUSE ,WE HAVE USE FILTER IT FILTERS THE INPUT AND SHOW THE VALUS IN OUTPUT

names = [123,345,678,900,1234,432,410]
res = list(filter(lambda names : names%2==0,names))
print(res)

names = ["sajid","zaib","dheeraj","sathvik","ruhan"]
res = list(filter(lambda names : len(names)>5 ,names))
print(res)

# "REDUCE" IS USED TO COMBINE ALL THE INPUT VALUES PRESENT
from functools import reduce
names = ["sajid","zaib","dheeraj","sathvik","ruhan"]
res = reduce(lambda res,i : res + i,names)
print(res)

names = ["sajid","zaib","dheeraj","sathvik","ruhan"]
res = reduce(lambda res ,i : res + i,names)
print(res)
"""
product = {"sugar" : 60,
           "salt" :50,
            "eggs":90,
            "dal":120,
            "bread":54
          }
print(dict(sorted(product.items())))  
print(dict(sorted(product.items(),reserve = True))) 

print(dict(sorted(product.tems(),key=lambda i:i[1])))
print(dict(sorted(product.tems(),key=lambda i:i[1],reverse = True)))