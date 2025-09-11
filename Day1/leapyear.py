# leap year or not
def leapyear(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        print("it is a leap year")
    else:
        print("not a leap year")
a=int(input("Enter a value"))
leapyear(a)