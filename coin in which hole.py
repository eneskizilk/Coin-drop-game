import random

numberOfCoinsInChamber1 = 0
numberOfCoinsInChamber2 = 0           #These are the number of coins in the chambers.
numberOfCoinsInChamber3 = 0
numberOfCoinsInChamber4 = 0
numberOfCoinsInChamber5 = 0
numberOfCoinsInChamber6 = 0
numberOfCoinsInChamber7 = 0
numberOfCoinsInChamber8 = 0
numberOfCoinsInChamber9 = 0
numberOfCoinsInChamber10 = 0
numberOfCoinsInChamber11 = 0

numberReceivedFromTheUser=int(input("Please enter your coins number :"))

for i in range(1,numberReceivedFromTheUser+1):      #This code will return the following probability for each coin.



    possibility=random.randrange(1,512+1)               #I calculated the probability of
                                                        # coins falling into chambers with these sequence of codes.
                                                        #Since we are working with multiples of 2,
                                                        # I chose 512 as the last value for convenience.

    if(possibility<=1):
        numberOfCoinsInChamber1=numberOfCoinsInChamber1 + 1    #The number of coins that fell into the first chamber
                                                               # (1/2)^9. Each coin must fall to the left of the
                                                               # nail so that it enters the first chamber.
    elif(2<=possibility and possibility<=10):                  #Where 1/2 represents the left from the left or
        numberOfCoinsInChamber2=numberOfCoinsInChamber2+1      # right option, 9 represents the number of nails
                                                               # it will multiply.
    elif (11<= possibility and possibility <= 50):
        numberOfCoinsInChamber3=numberOfCoinsInChamber3+1

    elif (51<= possibility and possibility <= 134):
        numberOfCoinsInChamber4=numberOfCoinsInChamber4+1    #I found the probability of the coin hitting
                                                             # that nail by multiplying 1/2 by 1/2 or
    elif (135<= possibility and possibility <= 251):         # adding the results to find the probabilities of the nails
        numberOfCoinsInChamber5=numberOfCoinsInChamber5+1    # in between.

    elif (252<= possibility and possibility <= 378):
        numberOfCoinsInChamber6=numberOfCoinsInChamber6+1

    elif (379<= possibility and possibility <= 463):
        numberOfCoinsInChamber7=numberOfCoinsInChamber7+1

    elif (464<= possibility and possibility <= 500):
        numberOfCoinsInChamber8=numberOfCoinsInChamber8+1

    elif (501<= possibility and possibility <= 510):
        numberOfCoinsInChamber9=numberOfCoinsInChamber9+1

    elif (511<= possibility and possibility <= 511):
        numberOfCoinsInChamber10=numberOfCoinsInChamber10+1

    elif (512<= possibility):
        numberOfCoinsInChamber11=numberOfCoinsInChamber11+1

print("Number of coins in chamber 1 is :", numberOfCoinsInChamber1)
print("Number of coins in chamber 2 is :", numberOfCoinsInChamber2)
print("Number of coins in chamber 3 is :", numberOfCoinsInChamber3)
print("Number of coins in chamber 4 is :", numberOfCoinsInChamber4)
print("Number of coins in chamber 5 is :", numberOfCoinsInChamber5)   #These codes show the person
print("Number of coins in chamber 6 is :", numberOfCoinsInChamber6)   # how many coins are in which chamber.
print("Number of coins in chamber 7 is :", numberOfCoinsInChamber7)
print("Number of coins in chamber 8 is :", numberOfCoinsInChamber8)
print("Number of coins in chamber 9 is :", numberOfCoinsInChamber9)
print("Number of coins in chamber 10 is :", numberOfCoinsInChamber10)


maxTabColumnNumber=max(numberOfCoinsInChamber1,numberOfCoinsInChamber2,numberOfCoinsInChamber3,numberOfCoinsInChamber4,numberOfCoinsInChamber5,numberOfCoinsInChamber6,numberOfCoinsInChamber7,numberOfCoinsInChamber8,numberOfCoinsInChamber9,numberOfCoinsInChamber10)
#With this code, I determined how many numbers to write on the histogram. The number I have determined will write the amount of coins in which chamber is more, and the histogram will look better.


tabColumnNumber=1
forFirstBlank=True
while(tabColumnNumber<=maxTabColumnNumber):
    if forFirstBlank==True:     #I wrote this if to leave a space at the top of the histogram
        print("  ",end="")      # to make histogram good.
        forFirstBlank=False

    print("",tabColumnNumber,end=" ")     #This code writes the numbers above the histogram.
    tabColumnNumber=tabColumnNumber+1

print()       #This code allows us to move to the bottom line.

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")       #this code draws the hyphens in the histogram
    hyphen=hyphen+1

print()

print("1 ",numberOfCoinsInChamber1 * "o  ")     #This code shows the first circle and if the coin is dropped
                                                # in that circle, it draws "o" as much as the number of coins.
hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1
                                                  #The codes below show the chamber numbers and coins in the chamber
                                                  # like these codes. It leaves a hyphen in between.
print()                                           #You might wonder why you didn't write shortly using while.
                                                  #I tried, but I had trouble drawing "o" so I wrote one by one.
print("2 ",numberOfCoinsInChamber2 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("3 ",numberOfCoinsInChamber3 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1
print()

print("4 ",numberOfCoinsInChamber4 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("5 ",numberOfCoinsInChamber5 * "o  ")


hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("6 ",numberOfCoinsInChamber6 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("7 ",numberOfCoinsInChamber7 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("8 ",numberOfCoinsInChamber8 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("9 ", numberOfCoinsInChamber9 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1

print()

print("10 ", numberOfCoinsInChamber10 * "o  ")

hyphen=1
while(hyphen<=maxTabColumnNumber+1):
    print("-" ,end="  ")
    hyphen=hyphen+1