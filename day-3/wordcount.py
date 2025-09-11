def wordcount():
    s=input("Enter the string:")
    c=0
    for i in s:
        if(i==' '):
            c+=1
    print(f"number of words in the string are:{c+1}")
wordcount()