# caluculate cuurent bill
def currentbill(pmr,lmr):
    tu=pmr-lmr
    cb=0
    if tu<=50:
        cb=tu*3.80
    elif tu>50 and tu<=100:
        cb=50*3.80+(tu-50)*4.20
    elif tu>100 and tu<=200:
        cb=50*3.80+(50)*4.20+(tu-100)*5.10
    elif tu>200 and tu<=300:
        cb=50*3.80+(50)*4.20+(100)*5.10+(tu-200)*6.30
    else:
        cb=50*3.80+(50)*4.20+(100)*5.10+(200)*6.30+(tu-300)*7.50
    return cb;
cno=eval(input("Enter the customer number"))
cname=input("Enter the customer name")
pmr=int(input("Enter the present month readings "))
lmr=int(input("Enter the last month readings "))
print("customer name :",cname)
print("customer number :",cno)
cb=currentbill(pmr,lmr)
print("Current bill is :",cb)

