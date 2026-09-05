
"""
class flipkart:
    product = {"shirts":2000,"pants":1000,"bags":1000}
    discount = 30
    @classmethod
    def display(cls):
        print(cls.product)


    def userinfo(self,name,phone,addres):
        self.name = name
        self.phone = phone
        self.addres = addres
        print(f"hello {name} welcome to flipkart")
    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on ,go grab your products")    


sajid = flipkart()
sajid.userinfo("sajid",89072567262,"hyd")
sajid.displaydiscount()
sajid.display()
print(sajid.product)
print(sajid.name)
flipkart.displaydiscount()
flipkart.display()
print(flipkart.product)


# USING OBJECT -> INS,CLS,STA,CLASATT,INSATT
# USING CLASS -> CLS,STA,CLSATT
# CONSTRCTOR IS A SPECIAL METHOD THAT IS GOING TO BE CALLED AUTOMATICALLY WHEN OBJECT IS CREATED

class flipkart:
    product = {"shirt":2000,"pant":3000,"skirt":4000}
    discount = 20
    def __init__(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"hello{self.name}, welcome to flipkart")
sajid = flipkart("sajid",98877666,"hyd")
zaib = flipkart(93234555,"bng","zaib")

class instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password #__ =private  IF WE WANT TO ACCESS PRIVATE(WE CANT JUST ACCES IT OUTSIDE IN UTPUT)
        self._post = []            # _ = protected IF WE WANT TO ACCESS PUBLIC(WE CANT JUST ACCES IT OUTSIDE IN OUTPUT )
    def getpassword(self):         # SO WE USE DEF() LIKE WE WROTE TO ACCES IT DOWN WE CANT ACESS PROCTED ONE DIRECTLY 
        return self.__password
    def getpost(self):
        return self._post
    
    def display(self):
        print(self.username,self.__password,self._post)
sajid = instagram("sajid","sajid@123")
sajid.display()
print(sajid.username)            
print(sajid.getpassword())
print(sajid.getpost())
"""
"""
class instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []            
    def getpassword(self):
        return self.__password
    def getpost(self):
        return self._post
    def setpassword(self,newpassword):
        self.__password = newpassword
    @property
    def display(self):
        print(self.username,self.__password,self._post)  
    @property
    def accesspost(self):
        return self._post
    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)    

sajid = instagram("sajid","sajid@123")
sajid.display
print(sajid.username)            
print(sajid.getpassword())
print(sajid.getpost())

sajid.username = "zaib"
sajid.setpassword("sajid@123")
sajid.accesspost = "sunrise.png"
sajid.accesspost = "beach.png"
sajid.accesspost = "forest.png"

print(sajid.username)
print(sajid.getpassword())
print(sajid.accesspost)
"""
#__________________________________INHETITANCE_________________________________________________________
#OBTANING FROM PARENT CLASS TO CHILD CLASS
class whatsappv1:
    def __init__(self,name):
        self.name = name
        print(f"welcome to the whatapp --v1 {self.name}!")
    def messaging(self):
        print("you can send messages")
class whatsappv2(whatsappv1):
    def __init__ (self,name):
        self.name = name
        print(f"welcome to whatsapp --v2 {self.name}!")
    def calls(self):
        print("you can audio and viedo calls")
sajid = whatsappv1("sajid") 
sajid.messaging()

zaib = whatsappv2("zaib")
zaib.messaging()
zaib.calls()




