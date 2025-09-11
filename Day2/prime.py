# find prime numbers
def prime(n):
    i=2
    while i<=n:
        j=1
        c=0
        while j<=i:
          if i%j==0:
            c=c+1
          j=j+1
        if c==2:
            print(i)
        i=i+1
n=int(input("Enter a number"))
prime(n)

