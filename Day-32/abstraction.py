from abc import ABC,abstractmethod
#ABC = ABSTRACT BASE CLASS METHOD
class phonepay(ABC):
    def senderinfo(self):
        print("you can enter their mobile number or scanner")
    def amount(self):
        print("you caan enter amount")
    def pin(self):
        print("you need to enter the pin")
    @abstractmethod
    def trasnscation(self):
        pass 
class HDFC(phonepay):
    def trasnscation(self):
        print("payment using HDFC bank")
class UNION(phonepay):
    def trasnscation(self):
        print("payment using union bank")
class CANARA(phonepay):
    def trasnscation(self):
        print("you can make transaction using canara bank")
class ICIC(phonepay):
    def trasnscation(self):
        print("you may do transaction using icic bank")      
sajid = HDFC() 
sajid.senderinfo()
sajid.amount()
sajid.pin()        
sajid.trasnscation()                                       