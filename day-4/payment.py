class Payment:
    def pay(self,amount):
        print("Amount",self.amount)
class CashPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid in cash")
class CardPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid in card")
class UpiPayment(Payment):
    def pay(self,amount):
        print(f"{amount} paid in upi")
p=[CashPayment(),CardPayment(),UpiPayment()]
for x in p:
    x.pay(1000)

