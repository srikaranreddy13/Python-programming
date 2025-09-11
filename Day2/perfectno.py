# perfect number
def perfectnumber(n):

    for i in range(1,n):
        k=i
        c=0
        for j in range(1,i):
            if i%j==0:
                c=c+j
        if c==k:
            print(k)
        

 
n=int(input("Enter a number"))
perfectnumber(n)