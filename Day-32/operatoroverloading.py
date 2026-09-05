class numbers:
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n+num.n
    def __sub__(self,num):
        return self.n-num.n 
    def __mul__(self,num):
        return self.n * num.n        
    def __truediv__(self,num):
        return self.n /num.n  
    def __floordiv__(self,num):
        return self.n // num.n  
    def __mod__(self,num):
        return self.n % num.n  
    def __pow__(self,num):
        return self.n ** num.n  
    def __eq__(self,num):
        return self.n == num.n
    def __ne__(self,num):
        return self.n != num.n
    def __gt__(self,num):
        return self.n > num.n
    def __ge__(self,num):
        return self.n >= num.n
    def __lt__(self,num):
        return self.n < num.n
    def __le__(self,num):
        return self.n <= num.n
    def __str__(self):
        return str(self.n)


abc = numbers(12)
bcd = numbers(23)
print(abc,bcd)
print(abc + bcd)        
print(abc - bcd)        
print(abc * bcd)        
print(abc / bcd)        
print(abc//bcd)        
print(abc % bcd)        
print(abc ** bcd)        
print(abc == bcd)        
print(abc > bcd)  
print(abc >= bcd)  
print(abc < bcd)  
print(abc <= bcd)  


