def delbypos(pos):
    nums=[10,20,30,40,50,60]
    if(pos<1 or pos>len(nums)):
        print("enter coorect pos")
    else: 

     for i in range(pos-1,len(nums)-1):
        nums[i]=nums[i+1]
     nums=nums[:-1]
    print(nums)
delbypos(3)



        
