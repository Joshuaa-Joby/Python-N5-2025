unit = 0.15
meterstart = int(input("Enter the meter at the start of the month: "))
meterend = int (input("Enter the meter at the end of the month: "))
totalmeter = meterstart - meterend
totalcost = totalmeter * unit
totalcost  = totalcost + 12.00
print ("The total cost for the month is: £" + str(totalcost))