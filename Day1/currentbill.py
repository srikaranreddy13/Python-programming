# calculate the current bill for present month and display with customer details
cno=eval(input("Enter the customer number"))
cname=input("Enter the customer name")
pmr=int(input("Enter the present month readings "))
lmr=int(input("Enter the last month readings "))
tu=pmr-lmr
cbill=tu*3.80
print("customer name :",cname)
print("customer number :",cno)
print("total units for present month :",tu)
print("current bill for this month :",round(cbill,2))