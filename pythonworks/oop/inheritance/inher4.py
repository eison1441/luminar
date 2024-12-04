# 29/10/2024

# SINGLE INHERITANCE
class Grandparent:
    def m1(self):
        print("Grand parent class m1 method")
class Parent(Grandparent):
    def m2(self):
        print("parent class m2 method")

class Child(Parent):
    def m3(self):
        print("Child class m3 method")


# MULTILEVEL INHERITANCE
class Grandparent:
    def m1(self):
        print("Grand parent class m1 method")
class Parent:
    def m2(self):
        print("parent class m2 method")

class Child(Parent,Grandparent):
    def m3(self):
        print("Child class m3 method")


child_instance1=Child()
child_instance1.m1()
child_instance1.m2()
child_instance1.m3()




