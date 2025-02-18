#Author: Drake Nelson
#My Coffee and More Shop
#A program where the user enters the number of each item bought and receives a total cost

#Displays the title
print("***************************************")
print("My Coffee and More Shop")

#Gathers the input on how much of each item was bought
print("Number of coffees bought?")
coffeesBought = int(input())
print("Number of muffins bought?")
muffinsBought = int(input())
print("Number of teas bought?")
teasBought = int(input())
print("Number of donuts bought?")
donutsBought = int(input())

#Check if inputs are negitive
#If so it sets them to zero
if coffeesBought < 0:
    coffeesBought = 0
if muffinsBought < 0:
    muffinsBought = 0
if teasBought < 0:
    teasBought = 0
if donutsBought < 0:
    donutsBought = 0

#Displays seperator
print("***************************************")
print("")
print("***************************************")

#Displays start of receipt
print("My Coffee and More Shop Receipt")

#Defines the varibles for cost, tax, and totals
#Also calculates the total cost of each item, the subtotal, tax, and main total
coffeeCost = 5
muffinCost = 4
teaCost = 5
donutCost = 3
taxPercent = 6
totalCoffeeCost = coffeesBought * coffeeCost
totalMuffinCost = muffinsBought * muffinCost
totalTeaCost = teasBought * teaCost
totalDonutCost = donutsBought * donutCost
subTotal = totalCoffeeCost + totalMuffinCost + totalTeaCost + totalDonutCost
taxCost = subTotal * (taxPercent / 100)
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

#Displays how many teas were bought
#Displays the cost for each
#Displays the total cost
#Checks if there is multiple teas bought
#If multiple it uses the plural word for tea
if(teasBought > 1):
    print(str(teasBought) + " Teas at $" + str(teaCost) + " each: $ " + str(totalTeaCost) + ".00")
if(teasBought <= 1):
    print(str(teasBought) + " Tea at $" + str(teaCost) + " each: $ " + str(totalTeaCost) + ".00")

#Displays how many donuts were bought
#Displays the cost for each
#Displays the total cost
#Checks if there is multiple donuts bought
#If multiple it uses the plural word for donut
if(donutsBought > 1):
    print(str(donutsBought) + " Donuts at $" + str(donutCost) + " each: $ " + str(totalDonutCost) + ".00")
if(donutsBought <= 1):
    print(str(donutsBought) + " Donut at $" + str(donutCost) + " each: $ " + str(totalDonutCost) + ".00")

#Displays the tax percent and the cost
print(str(taxPercent) + "% tax: $ " + str(taxCost)) 

#Displays seperator
print("---------")

#Displays total and final seperator
print("Total: $ " + str(total))
print("***************************************")

#Displays final message
print("")
print("Thank you for visting my store.")
