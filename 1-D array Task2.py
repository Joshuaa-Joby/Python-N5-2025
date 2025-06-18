weights = []
Total_weight = 0
weight = int(input("Enter the weight of food for this day: "))
while weight > 0 or weight < 300:
    if weight != weight > 0 or weight < 300:
        print("Invalid weight inputed")
    weights = int(input("Enter the weight of food for this day: "))
else:
    for i in range (4):
        weight = int(input("Enter the weight of food for this day: "))
        weights.append(weight)  

for x in range(len(weights)):
       Total_weight += (weight[x])    
print('The Total Weight is:' + str(round(Total_weight, 2))+ 'g') 