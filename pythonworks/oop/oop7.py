class Editor:

    name:str

    vendor:str

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def __str__(self):

        return self.name
    


Editor_instance1=Editor("visual studio","Microsoft")
print(Editor_instance1)

Editor_instance2=Editor("pycharm","jebrains")
print(Editor_instance2)

Editor_instance3=Editor("intellij","jebrains")
print(Editor_instance3)    