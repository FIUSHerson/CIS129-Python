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

# Ask for input
purchase_amount = float(input("Please enter a price {DD.CC}: $"))
print("")

# Process math
purchase_state_tax_amount = purchase_amount * STATE_TAX_RATE
purchase_county_tax_amount = purchase_amount * COUNTY_TAX_RATE
purchase_total = purchase_amount + purchase_state_tax_amount + purchase_county_tax_amount

# Fancy print everything out
print("\n==========================================")
print("=                                        =")
print("=              Tax  Summary              =")
print("=                                        =")
print("==========================================\n")
print("Price of Item........................${:.2f}".format(purchase_amount))
print("State Tax............................${:.2f}".format(purchase_state_tax_amount))
print("County Tax...........................${:.2f}".format(purchase_county_tax_amount))
print("\nTotal................................${:.2f}".format(purchase_total))