#Author: Drake Nelson
#My Coffee and Muffin Shop
#A program where the user enters the number of each item bought and receives a total cost

#Displays the title
print("***************************************")
print("My Coffee and Muffin Shop")

#Gathers the input on how much of each item was nought
print("Number of coffees bought?")
coffeesBought = int(input())
print("Number of muffins bought?")
muffinsBought = int(input())

#Displays seperator
print("***************************************")
print("")
print("***************************************")

#Displays start of receipt
print("My Coffee and Muffin Shop Receipt")

#Defines the varibles for cost, tax, and totals
#Also calculates the total cost of each item, the subtotal, tax, and main total
coffeeCost = 5
muffinCost = 4
taxPercent = 6
totalCoffeeCost = coffeesBought * coffeeCost
totalMuffinCost = muffinsBought * muffinCost
subTotal = totalCoffeeCost + totalMuffinCost
taxCost = round(subTotal * (taxPercent / 100), 2)
total = subTotal + taxCost

#Displays how many coffees were bought
#Displays the cost for each
#Displays the total cost
#Checks if there is multiple coffees bought
#If multiple it uses the plural word for coffee
if(coffeesBought > 1):
    print(str(coffeesBought) + " Coffees at $" + str(coffeeCost) + " each: $ " + str(totalCoffeeCost) + ".00")
if(coffeesBought <= 1):
    print(str(coffeesBought) + " Coffee at $" + str(coffeeCost) + " each: $ " + str(totalCoffeeCost) + ".00")

#Displays how many muffins were bought
#Displays the cost for each
#Displays the total cost
#Checks if there is multiple muffins bought
#If multiple it uses the plural word for muffin
if(muffinsBought > 1):
    print(str(muffinsBought) + " Muffins at $" + str(muffinCost) + " each: $ " + str(totalMuffinCost) + ".00")
if(muffinsBought <= 1):
    print(str(muffinsBought) + " Muffin at $" + str(muffinCost) + " each: $ " + str(totalMuffinCost) + ".00")

#Displays the tax percent and the cost
print(str(taxPercent) + "% tax: $ " + str(taxCost)) 

#Displays seperator
print("---------")

#Displays total and final seperator
print("Total: $ " + str(total))
print("***************************************")
