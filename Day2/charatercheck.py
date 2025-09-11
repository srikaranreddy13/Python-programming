# take input as any chararcter and find it is alphabet or number or special character
def find(a):
    if a.isalpha():
        print("it is alphabet")
    elif a.isdigit():
        print("It is a number")
    else:
        print("It is a special character")
a=input("Enter a character")
find(a)
