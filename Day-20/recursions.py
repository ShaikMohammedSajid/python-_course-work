
def display(n):
    if n >10:
        return
    print(n)
    display(n+1)
display(1)    

#revrerse function
def display(n):
    if n>10:
        return
    display(n+1) # after return we are doing n+1 so it goes in to reverse
    print(n)
display(1)        

def displaysum(n):
    if n==0 :
        return 0
    return n +displaysum(n-1)    
print(displaysum(8))

#product & factorial
def displya_product(n):
    if n==1:
        return 1
    return n * displya_product(n-1)
print(displya_product(5))    

def display(name):
    if name == len(s):
        return
    print(s[name])  # IF WE TAKE ONLY PRINT(NAME)IT WILL SHOW US IN INDEX VALUE,IF WE TAKE S[NAME] IT SHOW US WORDS
    display(name+1)
s = "python programing"
display(0) 
 
def display(n):
    if n == len(s):
        return
    print(s[:n]) 
    display(n+1)   
s = "python programing"
display(1)  

def display(inx,w):
    if inx>len(s)-w:
        return
    print(s[inx : inx+w])
    display(inx +1,w)   
s = "python progarming "
display(0,3) 

def display(n):
    if n ==0:
        return 
    display(n//10)
    print(n%10)
n = 987654
display(n) 

def display(n):
    if n == 0:
        return 0
    return n%10 + display(n//10)
n = 987654
print(display(n))   
"""
a = 0
b =1
n =10
for i in range(n-1):
    a,b = b,a+
     









    
