tempratures = []
Average_temperature = 0
temperature = int(input("Enter temprature: "))
while temperature > -20 or temperature < 50 :
    print("Invalid temprature")
    temperature = int(input("Enter temprature: "))
else:
    for i in range (6):
        temperature = int(input("Enter temprature: "))
        tempratures.append(temperature)  

for x in range(len(tempratures)):
       
       Average_temperature += (temperature[x]/6)    
print('The Average Temperature is:' + str(round(Average_temperature, 2))+ '°C') 