# find factorial of a number
def  factorial(n):
    i=1
    while n>0:
        i=i*n
        n=n-1
    return i
n=int(input("Enter a number: "))
print("factorial of a number :",factorial(n))