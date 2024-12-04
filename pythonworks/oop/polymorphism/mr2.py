class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)

class StandardShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)

Shipping_cost=Shipping()
Shipping_cost.calculate_shipping_cost(100)

Shipping_cost1=ExpressShipping()
Shipping_cost1.calculate_shipping_cost(1000)

Shipping_cost2=StandardShipping()
Shipping_cost2.calculate_shipping_cost(1000)