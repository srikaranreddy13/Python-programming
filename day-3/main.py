import ecommerce_utils
cart={}
n=int(input("Enter the number of items in your cart:"))
for i in range(n):
    x=input("Enter the name of the product:")
    y=int(input("Enter the price of the products"))
    cart[x]=y
ecommerce_utils.generate_invoice(cart)