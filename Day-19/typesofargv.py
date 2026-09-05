
def displya(name,gmail,password):
    print(f"your name is {name}")
    print(f"your mail is {gmail} ")
    print(f"your password is {password}")
displya("sajid","shaiksajid@gmail.com","sajid@123")
displya("taha@123","taha@gmail.com","Nayab Taha")
displya("zaib12@gmail.com","zaib12","zaib")  

def displya(name,gmail,password):
    print(f"your name is {name}")
    print(f"your mail is {gmail} ")
    print(f"your password is {password}")
displya(name="sajid",gmail="shaiksajid@gmail.com",password="sajid@123")
displya(password="taha@123",gmail="taha@gmail.com",name="Nayab Taha")
displya(gmail="zaib12@gmail.com",password="zaib12",name="zaib") 
"""

#________________________DEFAULT ARGUMENTS_______________________________

"""
def display(name,gmail="gmail.com",password=""):
    print(f"your name is {name}")
    print(f"your mail is {gmail} ")
    print(f"your password is {password}")
display("sajid","sajid@gmail.com","sajid@123")
display("taha","taha@123gmail.com")
display("zaib") 
"""  

#__________________________POSTIONAL ARGUMENTS_____________________________
"""
def display(*names):
      # * WE TAKE * so THAT THE OUTPUT COMES IN TUPEL
      print(names)
display("sajid")
display("sajid","zaib")
display("sajid","zaib","dheeraj")
display("sajid","zaib","dheeraj","vikas")

"""
def display(**product):
    # WE USE ** TO PRINT OUTPUT IN  DICT
    print(product)
display(bag=5000)    
display(bag=5000,book=30)    
display(bag=5000,book=30,bottel=300)    
