class Car:

    name:str

    brand:str

    fuel_type:str

    def __init__(self,name,brand,fuel_type):

        self.name=name

        self.brand=brand

        self.fuel_type=fuel_type

    def display(self):

        print(self.name,self.brand,self.fuel_type)
    
    def __str__(self):

        return self.brand
    





car_instance1=Car("alto","suzuki","petrol")

car_instance1.display()

print(car_instance1)