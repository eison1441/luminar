class SuperHero:
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit

    def __str__(self):
        return self.name
    
class Spiderman(SuperHero):
    def __init__(self,name,suit):
        super(). __init__(name,suit)

    def  Superpower(self):
        print("spider sence,","stikey body,","web shooting")
class Minnalmurali(SuperHero):
    def __init__(self,name,suit):
        super(). __init__(name,suit)

    def  Superpower(self):
        print("reflex,","speed,","anti gtavitational force")

SuperHero_instance1=Spiderman("spiderman","iorn spider")
SuperHero_instance1.Superpower()
print(SuperHero_instance1)


SuperHero_instance2=Minnalmurali("Minnal murali","cloth suit")
SuperHero_instance2.Superpower()
print(SuperHero_instance2)