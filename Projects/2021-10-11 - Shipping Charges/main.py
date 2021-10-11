import math

# Function receives input from user, converts to float, then returns value
def get_weight():
    # Loop until input is valid
    while True:
        # Validate input
        try:
            return float(input("\nWhat is the weight of the object in lbs? : "))
        except:
            print("Hmm... That's not a valid input. Try something like \"16\"")


# Function receives package weight and returns corresponding price.
def get_shipping_rate(weight):
    # Run weight through IF filter
    if weight <= 2.0:
        # Weight that defies gravity is treated as 2 or less lbs
        if weight < 0.0:
            print("The package defies gravity. The weight will be treated as 2 or less lbs.")
        return 1.10
    if weight > 2.0 and weight <= 6.0:
        return 2.20
    if weight > 6.0 and weight <= 10.0:
        return 3.70
    if weight > 10.0:
        return 3.80


# Function receives weight and rate, and returns the shipping price
def get_shipping_price(weight, rate):
    # Round up the value to account for floats
    return math.ceil(weight * rate)


# Print results
def print_results(shipping_weight, shipping_price, shipping_rate):
    print("\n==========================================")
    print("=                                        =")
    print("=            Shipping Invoice            =")
    print("=                                        =")
    print("==========================================\n")
    print("Weight of Object ................... ${:.2f}".format(shipping_weight))
    print("Shipping Rate ...................... ${:.2f}/lb".format(shipping_rate))
    print("\nTotal .............................. ${:.2f}\n".format(shipping_price))


# Begin primary functions of application
def main():
    # Get weight input
    shipping_weight = get_weight()

    # Calculate vars
    shipping_rate = get_shipping_rate(shipping_weight)
    shipping_price = get_shipping_price(shipping_weight, shipping_rate)

    # Print results
    print_results(shipping_weight, shipping_price, shipping_rate)


# Run main
main()