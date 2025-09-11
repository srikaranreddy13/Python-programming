def ecommerce():
    nums=[]
    print("1.Add product to the cart")
    print("2.Remove product from the cart")
    print("3.Search for a product in the cart")
    print("4.Diplay all the products in the cart")
    print("5.Total number of products in the cart")
    print("6.Sort the products in the cart")
    print("7.Clear the products in the cart")

    
    while(True):
        
        
        c=int(input("Enter the option from 1-7:"))
        if(c==1):
            x=int(input("Enter the element to add in the cart"))
            nums.append(x)
        elif(c==2):
            x=int(input("Enter the element to remove from the cart"))
            
            if x in nums:
                nums.remove(x)
            else:
                    print("Element not available")
        elif(c==3):
            x=int(input("Enter the element to remove from the cart"))
            if x in nums:
                    print("Element found")
                   
            else:
                    print("Element is not found")
        elif(c==4):
            print(f"Products are {nums}")
        elif(c==5):
            print(f"Total number of Products in the list are {len(nums)}")
        elif(c==6):
            nums.sort()
            print(f"Products in the sorted order are {nums}")
        elif(c==7):
            nums.clear()
            print(f"Products in the sorted order are {nums}")
        else:
            exit(0)


ecommerce()



