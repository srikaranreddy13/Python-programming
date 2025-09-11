# find number of notes in a given number
def find(n):
    c=0
    if n>=2000:
              a=n//2000
              n=n%2000
              c=c+a
    if n>=500:
              a=n//500
              n=n%500
              c=c+a
    if n>=100:
              a=n//100
              n=n%100
              c=c+a
    if n>=50:
              a=n//50
              n=n%50
              c=c+a
    if n>=10:
              a=n//10
              c=c+a
    return c;
n=int(input("Enter total amt :"))
a=find(n)
print("Total no.of notes are :",a)

        