# factors of  number
def perfectnumber(n):
    

    for i in range(1,n):
      
        if n%i==0:
            print(i)
        

 
n=int(input("Enter a number"))
perfectnumber(n)