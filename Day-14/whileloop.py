"""
i = 1
while (i<=10):
    print(i)
    i=i+1
    
i =10
while(i>0):
    print(i)
    i = i-1
   

i = 2
while(i<=100):
    print(i ,end =", ")
    i = i+2  

    
s = "sajid programmer"
i = len(s)-1        # if we starts from 0 it will strtas from front
while(i>=0):
    print(s[i],end =" ") 
    i = i-1


#remove 0 from the list    
s = [1,0,0,0,0,2,3,4,5,6,7,0,10,0,220,41]
while 0 in s:
    s.remove(0)
print(s)
    """
"""
d = {}
total_bill = 0
while True:
    product= (input("enter the list(for exit) :"))
    if product == "exit":
        break
    price = (int(input("enther the price:")))
    d[product] = price
    total_bill += price
print(d)
print("total bill :",total_bill)   

data ={}
total_bill = 0
while True:
    product = input("enter prodct name (for exit press exit):")
    if product == "exit":
        break
    price = int(input("enter the price of product :"))
    data[product] = price
    total_bill += price
print(data)
print("total bill is  ",total_bill)    


i = 0
while (i<10):
    i=i+1
    if i == 5:
        break
    print(i)
else:#ELse get used when when the if  statement is not executed

    print("end of the loop")
    """  

for i in range (1,n):
    if (i%2==0):
        print("its is a even number" )
        break
    else:
        print("its a odd number")    


