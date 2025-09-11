# sum find first and last digit of number
def firstnadlastdigits(n):
    a=0
    a=n%10
    
    b=0
    while n>0:
        b=n%10
        n=n//10
    print("sum of 1st and last digits",(a+b))
    
n=int(input("Enter a number"))
firstnadlastdigits(n)
