#_____________________________________MULTY LEVEL INHERITANCE______________________________________
class whatsappv1():
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and viedo calls")
class whatsappv3(whatsappv2)  :
    def status(self):
        print("you can add status for 24 hours")     
a = whatsappv1()
a.messaging()        
b = whatsappv2()
b.messaging()
b.calls()
c = whatsappv3()
c.messaging()
c.calls()
c.status()
#____________________________________MULTIPLE INHERITANCE___________________________________
class whatsappv1:
    def messaging(self):
        print("you can message")
class whatsappv2:# HERE WE ARE NOT TAKING PROPERTISE OF "WHATSAPPV1"
    def calls(self):
        print("you can audio and viedo calls")
class whatsappv3(whatsappv2,whatsappv1)  :
    def status(self):
        print("you can add status for 24 hours")     
a = whatsappv1()
a.messaging()        
b = whatsappv2()
#b.messaging() SO WE CANT USE WHTAPPPV1 ONE FEATURES
b.calls()
c = whatsappv3()
c.messaging()
c.calls()
c.status()
#_____________________________________HIERARCHIAL INHERITANCE___________________________________
class whatsappv1():
    def messaging(self):
        print("you can message")
class whatsappv2(whatsappv1):
    def calls(self):
        print("you can audio and viedo calls")
class whatsappv3(whatsappv1)  :
    def status(self):
        print("you can add status for 24 hours")     
a = whatsappv1()
a.messaging()        
b = whatsappv2()
b.messaging()
b.calls()
c = whatsappv3()
c.messaging()
#c.calls() BECAUSE WE HAVENT TAKEN WHATSAPPV2 FEATURES SO WE CANT USE WHATAPPV2 FETAURES
c.status()

#______________________________________HYBRID INHERITANCE_________________________________________
class whatappv1:
    def messaging(self):
        print("you can send messages")
class whatsappv2:
    def extramessages(self):
        print("you can send emojies,gifts,stickers")
class whatsappv3(whatappv1,whatsappv2):
    def call(self):
        print("you can do viedo call and audio call")
class whatappv4(whatsappv3):
    def status(self):
        print("yoyu can keep status for 24 hours")
a = whatappv1()
a.messaging()
b = whatsappv2()
b.extramessages()
c = whatsappv3()
c.messaging()
c.extramessages()
c.call()
d = whatappv4()
d.messaging()
d.call()
d.status()

#______________________________________SUPER() METHOD JUST______________________________________________
class whatappv1:
    def status(self):
        print("you can add images and viedoes")
class whatsappv2(whatappv1):
    def status(self):
        super().stat#IF WE USE SUPER()WE DONT NEED TO GIVE B = WHATAPPV2 IT PRINTS THE WHATAPPV2 VERSION
        print("you can add music and stickers") 
class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("you can like and add reactions")  
a = whatsappv3()
a.status()  
                          

#______________________________________CALLING FUNCTIONS USING CLASS_____________________________________________

class whatappv1:
    def statu(self):
        print("you can add images and viedeos")
class whatsappv2:
    def status(self):
        print("you can add music and stickers")
class whatsappv3(whatappv1,whatsappv2):
    def status(self):
         whatappv1.statu(self)# we have to use class like whatappv1 to call  function of whatappv1
         whatsappv2.status(self)# we have to use class like whatappv2 to call  function of whatappv2
         print("you can like and react")
a = whatsappv3()
a.status()                        

