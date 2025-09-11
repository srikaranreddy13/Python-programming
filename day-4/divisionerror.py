def division():
    num=int(input("Enter the numerator:"))
    den=int(input("Enter the denominator:"))
    try:
        print(f"Division result:{num/den}")
    except ZeroDivisionError:
        print(f"division by zero is not allowed")
    else:
        print(f"no error")
    finally:
        print(f"a={num} and b={den}")
division()
    