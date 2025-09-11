def oddevencount():
    nums = list(map(int, input("Enter elements separated by space: ").split()))
    ec=0
    oc=0
    for i in range(len(nums)):
        if(nums[i]%2==0):
            ec+=1
        else:
            oc+=1
    print(f"number of even numbers in list {ec} and number of odd numbers in the list are {oc}")

oddevencount()

