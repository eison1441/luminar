class Animal:
    def __init__(self,name,Species):
        self.name=name
        self.Species=Species
    
    def __str__(self):
        return self.name

    
class lion(Animal):
    def __init__(self,name,Species):
        super().__init__(name,Species)

    def sound(self):
        print("grrrr")


class Cat(Animal):
    def __init__(self,name,Species):
        super().__init__(name,Species)
        

    def sound(self):
        print("meow")


lion_instance=lion("lion","Panthera leo")
lion_instance.sound()

cat_instance=Cat("Cat","Felis catus")

cat_instance.sound()
print(cat_instance)