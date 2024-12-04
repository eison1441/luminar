class Cusine:
    Cusine_name:str
    def __init__(self,cusine_name):
        self.Cusine_name=cusine_name
    def display_Cusine_name(self):
        print(self.Cusine_name)
class Meal_Type:
    Meal_type=str
    def __init__(self,Meal_type):
        self.Meal_type=Meal_type
    def display_Meal_type(self):
        print(self.Meal_type)

class Dish(Cusine,Meal_Type):
    def __init__(self,Cusine_name,Meal_type,Dish_name):
        Cusine.__init__(self,Cusine_name)
        Meal_Type.__init__(self,Meal_type)
        self.Dish_name=Dish_name
    def display_Dish(self):
        self.display_Cusine_name()
        self.display_Meal_type()
        print(self.Dish_name)


dish_instance=Dish("indian","break fast","dosa")
dish_instance.display_Dish()