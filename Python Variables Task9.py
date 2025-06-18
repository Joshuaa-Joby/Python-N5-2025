names =  ['flour','sugar','eggs','butter','chocolate','vanilla']
ing = [100,100,2,50,50,10]
newingredients = []

scale = 6/4

for index in range(6):
    newingredients.append(ing[index]*scale)
    print(names[index] + ": " +str(newingredients[index]))