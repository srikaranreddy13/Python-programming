def apply_discount(price,discount_percent):
    return (price-((price*discount_percent)/100))
def add_gst(price,gst_percent):
    return (price+((price*gst_percent)/100))
def generate_invoice(cart,discount_percent=10,gst_percent=18):
    subtotal=0

    for i in cart.keys():
        subtotal=subtotal+cart[i]
    print(f"Subtotal:{subtotal}")
    a=apply_discount(subtotal,10)
    print(f"after 10% discount:{a}")
    b=add_gst(a,18)
    print(f"after 18% gst:{b}")
    print(f"thank you for shopping ")




