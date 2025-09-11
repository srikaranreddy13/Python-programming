# convert number into word
def word(n):
    a=str(n)
    for i in a:
        if i=="1":
            print("one",end=" ")
        elif i=="2":
            print("Two",end=" ")
        elif i=="3":
            print("three",end=" ")
        elif i=="4":
            print("four",end=" ")
        elif i=="5":
            print("five",end=" ")
        elif i=="6":
            print("six",end=" ")
        elif i=="7":
            print("seven",end=" ")
        elif i=="8":
            print("eight",end=" ")
        else:
            print("nine",end=" ")

n=int(input("Enter a nunber"))
word(n)