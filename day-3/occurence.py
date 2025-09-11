def occurence():
    s=input("Enter the string:")
    c=input("enter  a character to find its occurences:")
    count=0
    for i in s:
        if(i==c):
            count+=1
        
    print(f"count of the character:{c} is {count} ")
occurence()
