unit = float(input("Enter The Unit Value "))
if unit >= 101 and unit <=200:
    unit = unit * 5
    print("The Bill Amount ", unit)
elif unit >= 201:
     unit = unit * 10
     print("The Bill Amount ", unit)
else:     
    print("There is No Charges For Below 100 Units")