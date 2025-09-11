def uniques():
    list=[1,2,2,2,30,4,5]
    unique=[]
    for i in list:
        if i not in unique:
            unique.append(i)
    print(unique)
uniques()
