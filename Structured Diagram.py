childBuffeter = 2.00
cakeRequired = "yes"
if cakeRequired == "yes":
    cake = 15.00
else:
    cake = 0.00
noAdults = int(input("Enter the number of adults: "))
noChildren = int(input("Enter the number of children: "))
for i in range(noChildren):
   dietaryRequirements = input("Enter dietary requirements: ")
   print(dietaryRequirements)
if (noAdults + noChildren) > 20:
    venue = 0.00
else:
    venue = 50.00
cost = (childBuffeter * noChildren) + cake * + venue
print(cost)