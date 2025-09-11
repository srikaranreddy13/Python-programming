# strong number

def strongnumber(n):

    for i in range (1,n):
      c=0
      k=i
      while(i>0):
        a=i%10
        s=1
        for j in range(1,a+1):
            s=s*j

        i=i//10
        c=c+s
      if c==k:
        print(k)
  
n=int(input("Enter a number"))
strongnumber(n)