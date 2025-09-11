def Armstrong(n):
    s=0
    b=n
    while(n>0):
        a=n%10
        n=n//10
        s=s+a*a*a
    if s==b:
        print("Armstrong")
    else:
        print("it is not a Armstrong")  
n=int(input("Enter a number"))
Armstrong(n)