class BankAccount:
    def __init__(self):
     self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print(f"money deposited {amount}")
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance-=amount
            print(f"money withdrawed {amount}")
        else:
            print("Insufficient funds")
    def get_balance(self):
        print("current balace is:",self.__balance)
b=BankAccount()
b.get_balance()
b.deposit(1000)
b.get_balance()
b.withdraw(500)
b.get_balance()



    
        