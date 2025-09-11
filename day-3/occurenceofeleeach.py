def updatedstr():
    s=input("Enter the string:")
    result=""
    counted=set()
    for ch in s:
        if ch not in counted:
            count=0
            for c in s:
                if(c==ch):
                    count+=1
            result+=ch + str(count)
            counted.add(ch)
    print(result)
updatedstr()

                