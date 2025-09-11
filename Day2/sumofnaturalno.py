# sum of n natural numbers
def  natural(n):
    i=1
    s=0
    while i<=n:
        s=s+i
        i=i+1
    return s
n=int(input("Enter no.of natural numbers: "))
print("sum of n natural numbers :",natural(n))