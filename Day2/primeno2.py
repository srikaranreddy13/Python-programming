def prime(n):
    count=0
    for i in range(2,n+1):
        c=0
        
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
            
        if c==2:
            count+=1
            print(i,end=" ")
    print("tot no.of prime numbers",count)
n=int(input("Enter a number"))
prime(n)

