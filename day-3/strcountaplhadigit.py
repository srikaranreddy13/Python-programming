def count():
    s=input("Enter a String:")
    ac=0
    dc=0
    sc=0
    for i in s:
        if(i.isalpha()):
            ac+=1
        elif(i.isdigit()):
            dc+=1
        else:
            sc+=1
    print(f"alpha count is {ac} digit count is {dc} special character count is {sc}")
count()
