lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
widthOfSquarePacks = lengthOfSquarePacks
additionalRows = int(input("Please enter the number of additional rows included for free: "))
specialOffer = input("Is a special offer running? (y/n): ")
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    widthOfSquarePacks = widthOfSquarePacks + additionalRows
if specialOffer == "y":
    totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
print("The number of cans in the pack is: "+str(totalNumberOfCans))