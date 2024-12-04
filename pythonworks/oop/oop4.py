class Mobile:

    name:str

    brand:str

    price:int

    def __init__(self,name,brand,price):

        self.name=name

        self.brand=brand

        self.price=price

    def display(self):

        print(self.name,self.brand,self.price)

Mobile_instance1=Mobile("iqoo z9x","vivo",18500)
Mobile_instance1.display()