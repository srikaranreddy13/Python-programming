def findsecondlargest():
    list=[10,6,9,2,7,8]
    for i in range(len(list)-1):
         if(list[i]>list[i+1]):
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp
    print(list)
findsecondlargest()
            
