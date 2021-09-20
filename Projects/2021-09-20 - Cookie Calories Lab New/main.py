#######################################
# Program written by Alexander Anthis #
#######################################

# Ask for input
miles_driven = float(input("How many miles did you drive?: "))
gallons_used = float(input("How many gallons did you use?: "))

# Process math
miles_per_gallon = miles_driven / gallons_used

# Spit out results
print("\nYour MPG is {:.2f} miles per gallon.".format(miles_per_gallon))