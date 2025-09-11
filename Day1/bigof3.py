# check big in 3 numbers
def big(a,b,c):
    if a>b:
        if a>c:
            print("a is bigger")
        else:
            print("c is bigger")
    else:
        if b>c:
            print("b is bigger")
        else:
            print("c is bigger")
a=int(input("Enter values of a"))
b=int(input("Enter values of b"))
c=int(input("Enter values of c"))

big(a,b,c)