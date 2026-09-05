"""
for i in range(1,10):
    if i ==5:
        break
    print(i)
else:
    print("end of the loop") 
    """   
    #REMEMBER ONE THING IF YOUR BREAK STATMENT END IN FOR LOOP YOU WONT BE ABLE TO EXEQUE THE ELSE LOOP
    #IF THE BREAK STATMENT IS IN, "IF I == 15 :" THEN BREAK ,THE ELSE STATMENT WILL  EXECUTE 
"""
pin = 1234
for i in range(5):
    epin = int(input("ENTER YOUR PIN : "))
    if pin == epin :
        print("phone Unlocked")
        break
    else:
        print(" Invalid Password  ")
else:
    print("TRY AGAIN AFTER 30 SECONDS")
    """
#FIND FACTORIAL OF NUMBERS:
"""
n = int(input("Enter Your Number :"))
print("factor : " , end =" ")  
for i in range(1,n+1):
    if n%i==0:
        print(i,end =" ")  
        """

n = int(input("Enter Your Number :"))
for i in range(2,n //2+1):
    if n%i==0:
        print("It Is not A Prime Number ") 
        break
else:
    print("It is  a prime number:")               
