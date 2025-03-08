#Author: Drake Nelson
#3/4/2025

#Declares variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

#Begin while loops
while keepGoing == 'y':
    while counter <= 7:
        #Expects input on how many bottles returned
        print("Enter number of bottles returned for day #" + str(counter) + ":")
        todayBottles = int(input())

        #Adds today bottles to total
        totalBottles += todayBottles

        #Increases counter
        counter += 1

    #Sets payout constant
    PAYOUT_PER_BOTTLE = .10

    #Sets counter and total payout to zero
    counter = 0
    totalPayout = 0

    #Calculates payout
    totalPayout = (totalBottles * PAYOUT_PER_BOTTLE)

    #Sets total bottles to zero
    totalBottles = 0

    #Displays how bottles collected and payout
    print("The total number of bottles collected is " + str(totalBottles))
    print("The total paid out is $ " + str(totalPayout))

    #Asks if the user wants to run the program again
    print("Do you want to run the program again? (Enter y for yes).")
    keepGoing = input()