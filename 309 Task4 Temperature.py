Temperatures = []

for index in range (5):
    Temperature = input("Enter the Temperature:")
while Temperature >-20 or Temperature <50:
    print("Error, Temperature must be between -20 and 50")
    Temperature = int(input("Please enter a valid Temperature:"))
    Temperatures.append(Temperature)
Average_Temperature = sum(Temperatures) / len(Temperatures)
print("The Average Temperature is:", Average_Temperature)
#still not completed