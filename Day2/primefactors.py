# prime factors of  number
def perfectnumber(n):
    for i in range(1,n+1):
        if n%i==0:
            c=0
            for j in range(1,i+1):
               if i%j==0:
                   c=c+1
            if c==2:
                print(i)
        
                   
            
        

 
n=int(input("Enter a number"))
perfectnumber(n)