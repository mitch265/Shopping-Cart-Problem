## Shopping Cart Calculator Problem ##

numDrinks = input("How many drinks? ")
numDrinks = int(numDrinks)

singleDrinkCost = 2.25
sixPackCost = 10 # $1.67 per drink in 6-pack

numSingleDrinks = numDrinks % 6
numSixPacks = numDrinks // 6

totalCost = (singleDrinkCost * numSingleDrinks) + (sixPackCost * numSixPacks)

# apply 25% discount if cost (before sales tax) > $20
if totalCost > 20:
    totalCost *= 0.75 

# add sales tax
totalCost *= 1.06

print("Your total is ${:.2f}.".format(totalCost))
