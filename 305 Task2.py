username = input("Please enter your username:")
password = input("Please enter your password:")
if username == "ian" and password == "letmein":
    print("Logon accepted")
else:
    print("Password incorrect")

#a) username=IAN, password=letmein = Password incorrect
#b) username=ian, password=letmein = Logon accepeted
#c) username=ian, password=LETMEIN = Password incorrect