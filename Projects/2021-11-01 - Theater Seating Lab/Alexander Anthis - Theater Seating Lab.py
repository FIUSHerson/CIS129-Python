# Created by Alexander Anthis on 2021-11-01
# Created for Theater Seating Lab

# Makes sure user input is an integer
def validate_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("That is not a valid input. Please try again.")


# Checks if numbers go above max amount in each section
def check_input_numbers(tickets_A, tickets_B, tickets_c, MAX_A, MAX_B, MAX_C):
    if tickets_A <= MAX_A and tickets_B <= MAX_B and tickets_c <= MAX_C:
        return True
    else:
        return False


# Calculates income generated from each section along with the total
def calc_income(tickets_A, tickets_B, tickets_c):
    PRICE_FOR_TICKET_A = 20
    PRICE_FOR_TICKET_B = 15
    PRICE_FOR_TICKET_C = 10

    income_A = tickets_A * PRICE_FOR_TICKET_A
    income_B = tickets_B * PRICE_FOR_TICKET_B
    income_C = tickets_c * PRICE_FOR_TICKET_C
    total = income_A + income_B + income_C

    return income_A, income_B, income_C, total


# Fancy print everything out
def display_results(income_A, income_B, income_C, total):
    print("\n==========================================")
    print("||                                      ||")
    print("||            Income Summary            ||")
    print("||                                      ||")
    print("==========================================\n")
    print("Section A .......................... ${}".format(income_A))
    print("Section B .......................... ${}".format(income_B))
    print("Section C .......................... ${}".format(income_C))
    print("\nTotal .............................. ${}\n".format(total))


def main():
    # Init vars
    MAX_SEATS_A = 300
    MAX_SEATS_B = 500
    MAX_SEATS_C = 200

    # Loop for max ticket checking
    valid_numbers = False
    while not valid_numbers:
        # Get user input for ticket amounts
        tickets_sold_in_A = validate_user_input("How many tickets were sold in Section A? ")
        tickets_sold_in_B = validate_user_input("How many tickets were sold in Section B? ")
        tickets_sold_in_C = validate_user_input("How many tickets were sold in Section C? ")
        print()

        # Check if ticket amounts are more than max
        valid_numbers = check_input_numbers(tickets_sold_in_A, tickets_sold_in_B, tickets_sold_in_C, MAX_SEATS_A, MAX_SEATS_B, MAX_SEATS_C)

        # If tickets are above max, show numbers and max and get input again
        if valid_numbers == False:
            print("[ERROR] One or more of your tickets is above the maximum seats available.")
            print("Max seats in Section A is {}. Yours is {}.".format(MAX_SEATS_A, tickets_sold_in_A))
            print("Max seats in Section B is {}. Yours is {}.".format(MAX_SEATS_B, tickets_sold_in_B))
            print("Max seats in Section C is {}. Yours is {}.".format(MAX_SEATS_C, tickets_sold_in_C))

            print("\nPlease try again.")

        # If tickets are equal to or below max, calculate income and display results
        else:
            income_A, income_B, income_C, total = calc_income(tickets_sold_in_A, tickets_sold_in_B, tickets_sold_in_C)

            display_results(income_A, income_B, income_C, total)


main()