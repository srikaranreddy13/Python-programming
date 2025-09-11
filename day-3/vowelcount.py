def vowelcount():
    s=input("Enter the string")
    v=0
    c=0
    for str in s:
     if(str=='a' or str=="e" or str=='i' or str=='o' or str=='u'):
        v+=1
     else:
        c+=1
    print(f"vowel count is {v} consonant count is {c}")
vowelcount()
