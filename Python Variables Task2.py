total = []
item1 = int(input("Enter the first item price: "))
item2 = int(input("Enter the second item price: "))
item3 = int(input("Enter the third item price: "))
total.append(item1)
total.append(item2)
total.append(item3)
sum_total = sum(total)
print("The total price of the items is: £" + str(sum_total))