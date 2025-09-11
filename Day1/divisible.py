# check given number is divisible by 5 and 11 or not
def div(n):
    if n%5==0 and n%11==0:
        print("it is divisble")
    else:
        print("not")
a=int(input("Enter a value"))
div(a)
