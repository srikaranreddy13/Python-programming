# check student pass or fail
def check(m,n,p):
    a=(m+n+p)/3
    if a>=40:
        if a>80:
            print("Distenction")
        elif a>70:
            print("A")
        elif a>60:
            print("B")
        elif a>50:
            print("C")
        else:
            print("D")
    else:
        print("Fail")
m=int(input("Enter marks of sub1"))
n=int(input("Enter marks of sub2"))
p=int(input("Enter marks of sub3"))
check(m,n,p)
