#OVERRIDING MEANS SAME THINGS ACTS AS MANY FORMS 
class Hotstar:
    def __init__(self,name):
        print(f"welcome to Hotstar {name} ")
    def login(self):
        print("yoy can login to hotstar")
    def dahboard(self):
        print("your can see dashboard")
    def search(self):
        print("you can search")
    def playpause(self):
        print("you can start,stop,pause")
    def history(self):
        print("you can see history")
    def ads(self):
        print("Ads will run")   
    def quality(self):
        print("Quality will be low")  
    def access(self):
        print("You have limited access")
    def downloads(self):
        print("you cant download viedoes")
class PremiumHotstar(Hotstar):
    def __init__(self,name):
        print(f"Welcome to Hotsar {name} We are blessed to have you")
    def ads(self):
        print("you dont get any ads")
    def quality(self):
        print("you are able to watch high quality")  
    def access(self):
        print("you habve unlimited access")
    def downloads(self):
        print("you can download viedoes")   
sajid = Hotstar("sajid")
sajid.login()                                              
sajid.dahboard()                      
sajid.search()                     
sajid.playpause()                       
sajid.history()                       
sajid.ads()                       
sajid.downloads()                       
sajid.quality()                       
sajid.access()  

zaib = Hotstar("zaib")
zaib.login()                       
zaib.dahboard()                     
zaib.search() 
zaib.playpause()                       
zaib.history()                       
zaib.ads()                       
zaib.downloads()                       
zaib.quality()                       
zaib.access()                    

