savings = []
Total_savings = 0
savings = int(input("Enter the savings for this month: "))
while savings  < 0 or savings > 1000:
    print("Invalid savings inputed")
    savings = int(input("Enter the savings for this month: "))
else:
    for i in range (12):
        saving = int(input("Enter the savings for this month: "))
        savings.append(savings)