english = int (input("Enter your English score: ")) 
maths = int(input("Enter your Maths score: "))  
computing = int(input("Enter your Computing score: ")) 
art = int(input("Enter your Art score: ")) 
total = english + maths + computing + art
Avg = total / 4
print("Your total score is: " + str(total), "%") 
print("Your average score is: " + str(Avg), "%")