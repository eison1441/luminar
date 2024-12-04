class Operations:
    def add(self,num1,num2):
        print(num1+num2)


    def add(self,num1,num2,num3):
        print(num1+num2+num3)

obj=Operations()
obj.add(10,20,30)
obj.add(100,200)

class Operations:
    def add(self,*args):
        print(sum(args))

obj=Operations()
obj.add(10,20,30)
obj.add(100,200)