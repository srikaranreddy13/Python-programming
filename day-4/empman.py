class Emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Employee details:\nName:{self.name}\nSalary:{self.salary}")
class manager(Emp):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print(f"Employee details:\nName:{self.name}\nSalary:{self.salary}\nDepartment:{self.dept}")
m1=manager("karan",100000000,"cse")
m1.display()

        