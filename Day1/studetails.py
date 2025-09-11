#student details
sno=eval(input("Enter the student number"))
sname=input("Enter the student name")
s1=int(input("Enter the maths marks "))
s2=int(input("Enter the science marks "))
s3=int(input("Enter the social marks "))
tot=s1+s2+s3
avg=(tot/3)
print("Student Name is:",sname)
print("Student Number is:",sno)
print("Student Maths marks is:",s1)
print("Student Science is:",s2)
print("Student Social marks is:",s3)
print("total marks are :",tot)
print("average marks :",round(avg,2))


