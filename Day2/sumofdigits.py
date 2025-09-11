# sum of digits
def sumofdigits(n):
    s=0
    while(n>0):
        a=n%10
        n=n//10
        s=s+a
    return s
n=int(input("Enter a number"))
print("Sum of digits:",sumofdigits(n))
