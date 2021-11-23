# Written by Alexander Anthis
# Created on 2021-11-01
# Created for Dice Game Lab

import random

def main():
    print()

    # Initialize variables
    endProgram = "no"
    playerOne = "NO NAME"
    playerTwo = "NO NAME"

    # Call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # While loop to run program again
    while endProgram == "no":

        # Populate variables
        winnerName = "NO NAME"

        # Call to rollDice
        winnerName = rollDice(playerOne, playerTwo)

        # Call to displayInfo
        displayInfo(winnerName)

        endProgram = input("Do you want to end the program? [yes/no]: ")
    

# This function gets the players' names
def inputNames(playerOne, playerTwo):
    playerOne = input("Please enter the name for Player 1: ")
    playerTwo = input("Please enter the name for Player 2: ")

    return playerOne, playerTwo

# This function will get the random values
def rollDice(playerOne, playerTwo):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number > p2number:
        return playerOne
    elif p1number < p2number:
        return playerTwo
    else:
        return "TIE"

# This function displays the winner
def displayInfo(winnerName):
    print("The winner is {}".format(winnerName))

# Call main
main()