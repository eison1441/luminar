class Student:
    id=int

    rollnumber=int

    name=str

    cource=str


    def set_Student(self,id,rollnumber,name,cource):

        self.id=id

        self.rollnumber=rollnumber

        self.name=name

        self.cource=cource

    def display(self):
        print(self.id,self.rollnumber,self.name,self.cource)

student_instance1=Student()

student_instance2=Student()

student_instance1.set_Student(1,23,"EISON","PYTHON DJANGO")
        
student_instance1.display()