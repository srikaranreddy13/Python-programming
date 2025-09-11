class Student:
    def __init__(self,name,roll_no,age):
        self.name=name
        self.roll_no=roll_no
        self.age=age
        
    def display(self):
        print(f"Name of the student is {self.name}")
        print(f"Rollno of the student is {self.roll_no}")
        print(f"Age of the student is {self.age}")
s1=Student("karan",18,19)
s1.display()
s2=Student("visvan",10,20)
s2.display()