# Created by Alexander Anthis on 2021-11-03
# for the Going Green Lab

# Init a list of months
LIST_OF_MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


# Validates user input as integer
def get_user_input_as_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Invalid input. Please try again.")

# Pretty print the results
def print_results(not_green_cost, gone_green_cost):
    print("                      SAVINGS")
    print("-----------------------------------------------------")
    print("SAVINGS      NOT GREEN       GONE GREEN      MONTH")
    print("-----------------------------------------------------")
    
    # Calculate results for each month, then print
    for i, month in enumerate(LIST_OF_MONTHS):
        current_not_green = not_green_cost[i]
        current_gone_green = gone_green_cost[i]
        green_savings = current_gone_green - current_not_green

        print("${}          ${}             ${}         {}".format(green_savings, current_not_green, current_gone_green, month))
    
    print()


def main():
    # "Continue Running" loop
    keep_going = "y"
    while keep_going == "y":

        # Get user input for each month
        not_green_cost = []
        for month in LIST_OF_MONTHS:
            not_green_cost.append(get_user_input_as_int("Please enter your NOT GREEN energy costs for {}: ".format(month)))
        print("\n-----------------------------------------------------\n")

        # Same as above, but different variable
        gone_green_cost = []
        for month in LIST_OF_MONTHS:
            gone_green_cost.append(get_user_input_as_int("Please enter your GONE GREEN energy costs for {}: ".format(month)))
        print("\n-----------------------------------------------------\n")
        
        # Print the results
        print_results(not_green_cost, gone_green_cost)

        # Ask the user if they want to run the program again
        keep_going = input("Would you like to run the program again? [y/N]: ")


main()