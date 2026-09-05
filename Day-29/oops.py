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
sajid.display()
sajid.displaydiscount()
zaib = flipkart()
zaib.userinfo("zaib",987654321,"bng")
zaib.display()
zaib.displaydiscount()
taha = flipkart()
taha.userinfo("taha",56378487537,"ndl")
taha.display()
taha.displaydiscount()
