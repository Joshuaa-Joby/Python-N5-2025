overdue = int(input("Enter the number of days books overdue: "))  
fine_per_book = 0.50 
total_fine = overdue * fine_per_book 
if total_fine > 5:
    total_fine += 2.00 
print("The total fine for overdue books is: £" + str(total_fine))  