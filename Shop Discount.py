quantity = float(input("Enter the Purchase Quantity "))
if quantity >= 1000:
    unitprice = quantity * 100
    discount = unitprice * 0.1
    payamount = unitprice - discount
    print("The Total Quantity Price ",unitprice)
    print("The Discount Amount ",discount)
    print("The Payable Amount is", payamount)
else:
    print("Not eligible Quantity For Discount")    