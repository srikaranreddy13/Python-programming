# check the number is palindrome or not
def palindrome(n):
    s=0
    b=n
    while(n>0):
        a=n%10
        n=n//10
        s=s*10+a
    if s==b:
        print("palindrome")
    else:
        print("it is not a palindrome")  
n=int(input("Enter a number"))
palindrome(n)

