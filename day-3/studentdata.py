def record():
    student=[]
    n=int(input("Enter the number of records"))
    for i in range(n):
        roll=input("enter roll no:")
        name=input("enter name:")
        marks=int(input("enter marks:"))
        student.append((roll,name,marks))
    print(student)
    highest=student[0][2]
    for i in range(n):
        if(highest<student[i][2]):
            highest=student[i][2]
    print(f"highest marks are {highest}")
record()
    