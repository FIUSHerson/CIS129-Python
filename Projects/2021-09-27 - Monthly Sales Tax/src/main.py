#####################################################
#                                                   #
# Written by Alexander Anthis                       #
#                                                   #
# Takes price of item, displays total including tax #
#                                                   #
#####################################################


# Define tax rates
STATE_TAX_RATE = 0.04
COUNTY_TAX_RATE = 0.02

def AskForAmount():
    # Ask for input
    profit_amount = float(input("Please enter a price {DD.CC}: $"))
    print("")
    
    return profit_amount


def CalculateTaxAmounts(profit_amount):
    # Process math
    purchase_state_tax_amount = profit_amount * STATE_TAX_RATE
    purchase_county_tax_amount = profit_amount * COUNTY_TAX_RATE
    purchase_total = profit_amount + purchase_state_tax_amount + purchase_county_tax_amount

    return (profit_amount, purchase_state_tax_amount, purchase_county_tax_amount, purchase_total)


def PrintResults(purchase_data):
    profit_amount, purchase_state_tax_amount, purchase_county_tax_amount, purchase_total = purchase_data

    # Fancy print everything out
    print("\n==========================================")
    print("=                                        =")
    print("=              Tax  Summary              =")
    print("=                                        =")
    print("==========================================\n")
    print("Price of Item........................${:.2f}".format(profit_amount))
    print("State Tax............................${:.2f}".format(purchase_state_tax_amount))
    print("County Tax...........................${:.2f}".format(purchase_county_tax_amount))
    print("\nTotal................................${:.2f}\n".format(purchase_total))

profit_amount = AskForAmount()
purchase_data = CalculateTaxAmounts(profit_amount)
PrintResults(purchase_data)