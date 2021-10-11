# Lab 5-4 The Bottle Return Program
# the main function
def main():
    endProgram = 'no'
    while endProgram == 'no':
        print   #prints a blank line
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        print()
    
        endProgram = input('Do you want to end the program? (yes/no): ')

# this function will get the number of bottles returned
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
    while counter <= 7:
        # Input validation prep
        valid_input = False

        # Begin input validation
        while valid_input == False:
            try:
                # Attempt input
                todayBottles = int(input('Enter number of bottles for today: '))

                # If program gets here, then the input is valid.
                valid_input = True
            except:
                # Error message
                print("Hmm... That's not a valid input. Let's try that again.")

        totalBottles = totalBottles + todayBottles
        counter = counter + 1
           
    return totalBottles

# this function will calculate the payout
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

# this function will display the information
def printInfo(totalBottles, totalPayout):
    print('The total number of bottles collected is', totalBottles)
    print('The total paid out is ${:.2f}'.format(totalPayout))

# calls main
main()