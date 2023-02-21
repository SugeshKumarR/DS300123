a = int(input("Enter The Value "))
first_value=0
second_value=1
while second_value<a:
    print(second_value,end=" ")
    first_value,second_value = second_value, first_value + second_value
    
