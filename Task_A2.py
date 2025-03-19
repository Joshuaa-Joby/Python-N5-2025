#Get user input
Name = int(input("Enter Name:"))
Age =  int(input("Enter Age:"))

#Validate between 0 and 100
while Age < 0 or Age > 18:
    print("Not an accepted age")
    percentage = int(input("Please enter a valid age:"))