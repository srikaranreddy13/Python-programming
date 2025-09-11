# find first and last digit of number
def firstnadlastdigits(n):
    a=0
    a=n%10
    print("last digit:",a)
    b=0
    while n>0:
        b=n%10
        n=n//10
    print("first digit:",b)
    
n=int(input("Enter a number"))
firstnadlastdigits(n)
