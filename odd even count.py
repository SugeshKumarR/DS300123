list1 = []
n = int(input("Enter The List Range "))
for i in range(0,n):
 x = int(input("Enter The List Values "))
 list1.append(x)
print(list1)
even = 0
odd = 0
for a in list1:
    if a % 2 == 0 :
        even = even + 1
    else:
        odd = odd + 1
print("The Total Number of Even number ", even)
print("The Total Number of Odd number ", odd)
