TAX_PERCENT = 0.06

# Function asks for user input, converts to float, and returns amount as float.
def get_price_amount():
    # Create an infinite loop to get input, and break out once valid input is received.
    while True:
        try:
            return float(input("What is the initial total of the order before tips and tax? {$DD.CC} : $"))
        except:
            print("Hmm... That's not valid input. Here is an example: \"$23.45\"")


# Function receives initial total and returns the tip percent in decimal form.
def get_tip_percent(price):
    # Run price through IF filter to assign a tip percent
    if price <= 0:
        print("Currint price is $0.00, so tip amount is 0%.")
        return 0.00
    if price > 0 and price < 6:
        return 0.10
    if price >= 6 and price <= 12:
        return 0.13
    if price > 12 and price <= 17:
        return 0.16
    if price > 17 and price <= 25:
        return 0.19
    if price > 25:
        return 0.22


# Function receives price and tip percent and returns a final price
def calc_final_total(price, tip):
    # Calculate tip and tax, then add to price
    tip_amount = price * tip
    tax_amount = price * TAX_PERCENT
    final_total = price + tip_amount + tax_amount
    return (tip_amount, tax_amount, final_total)

# Function prints results given to it
def print_results(initial_price, tip_amount, tip_percent, tax_amount, final_total):
    print("\n==========================================")
    print("=                                        =")
    print("=                 Receipt                =")
    print("=                                        =")
    print("==========================================\n")
    print("Subtotal ........................... ${:.2f}".format(initial_price))
    print("")
    print("Tip ................................ ${:.2f}".format(tip_amount))
    print("Tip Percent ........................ {:.0f}%".format(tip_percent * 100))
    print("")
    print("Tax ................................ ${:.2f}".format(tax_amount))
    print("Tax Percent ........................ {:.2f}%".format(TAX_PERCENT * 100))
    print("\nTotal .............................. ${:.2f}\n".format(final_total))


# Function initiates goal of program
def main():
    # Get input
    price_amount = get_price_amount()

    # Calculate other vars
    tip_percent = get_tip_percent(price_amount)
    tip_amount, tax_amount, final_total = calc_final_total(price_amount, tip_percent)

    # Print results
    print_results(price_amount, tip_amount, tip_percent, tax_amount, final_total)


# Run main
main()