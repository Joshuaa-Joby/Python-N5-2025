# Program 3 - Investigate and modify
password = input("Please enter your password: ")
while len(password) > 8:
    print("Password accepted.")
if len(password) < 8:
    print("Error, you have to have more than 8 characters.")