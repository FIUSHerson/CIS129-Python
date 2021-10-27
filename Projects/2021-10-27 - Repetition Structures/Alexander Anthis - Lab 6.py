# Code written by Alexander Anthis on 2021-10-27
# Lab 6 The Bottle Return Program

# This program calculates and returns the amount of bottles and the payout.


def get_bottles(total_bottles):
    # Get user input and add to total bottle count
    counter = 1
    while counter <= 7:                 # run 7 times
        valid_user_input = False        # setup for input validation
        while valid_user_input == False:
            try:                        # make sure input is an integer
                total_bottles += int(input("Enter the number of bottles for today: "))
                valid_user_input = True
            except:
                print("That is not a valid answer. Try again...")

        counter += 1
    
    return total_bottles


def calc_payout(total_bottles):
    # Multiply bottle count by price-per-bottle
    return total_bottles * 0.1


def print_info(total_bottles, total_payout):
    # Print results
    print("Total bottles: {}".format(total_bottles))
    print("Total payout: ${:.2f}".format(total_payout))


def main():
    # Define variables
    total_bottles = 0
    total_payout = 0
    end_program = False

    # Begin primary loop
    while not end_program:
        # Calculate number of bottles and payout, then print results
        total_bottles = get_bottles(total_bottles)
        total_payout = calc_payout(total_bottles)
        print_info(total_bottles, total_payout)

        # Ask if user wants to end program, default or error input set to "no"
        valid_user_input = False        # setup for input validation
        while valid_user_input == False:
            try:
                user_input = input("Would you like to end the program? [y/N]: ")
                if user_input == "y" or user_input == "Y":
                    valid_user_input = True
                    end_program = True
                else:
                    valid_user_input = True
            except:
                print("That is not a valid answer. Try again...")


main()