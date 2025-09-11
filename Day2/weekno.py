# find week name by using week number
def week(n):
    if n==1:
        print("Sunday")
    elif n==2:
        print("Monday")
    elif n==3:
        print("Tuesday")
    elif n==4:
        print("Wednesday")
    elif n==5:
        print("Thursday")
    elif n==6:
        print("Freiday")
    elif n==7:
        print("Saturday")
    else:
        print("Invalid number")

n=int(input("Enter a number"))
week(n)