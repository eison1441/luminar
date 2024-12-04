class Employee:
    id:int

    salary:int

    name:str

    department:str


    def set_Employee(self,id,salary,name,department):

        self.id=id

        self.salary=salary

        self.name=name

        self.department=department

    def display(self):
        print(self.id,self.salary,self.name,self.department)

Employee_instance1=Employee()

Employee_instance2=Employee()

Employee_instance1.set_Employee(1,23000,"EISON","hr")
        
Employee_instance1.display()



# reference name =class name   ==>empty object