Temperature = []

Temperature = int(input("Enter temperature: "))
while Temperature > -20 or Temperature < 50:
    print("Invalid temperature")
    Temperature = int(input("Enter temperature: "))