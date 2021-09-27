######################################
#  Code written by Alexander Anthis  #
######################################


#  Gets number of people attending and number of hot dogs and calculates num of hot dogs needed
def GetTotalHotDogs():
    print("") #command line formatting

    # Get the number of people attending cookout
    people = int(input("Enter the number of people attending the cookout: "))
    # Get number of hot dogs each person will have
    hot_dogs = int(input("Enter the number of hot dogs for each person: "))

    print("\n---\n") # command line formatting

    # Calculate needed amount of hot dogs
    return people * hot_dogs

# Calculates and shows the results
def ShowResults(total_hot_dogs):
    # Declare some constants
    HOT_DOGS_PER_PACKAGE = 10
    BUNS_PER_PACKAGE = 8

    # Calculate left over hot dogs
    hot_dogs_left_over = (HOT_DOGS_PER_PACKAGE - total_hot_dogs % HOT_DOGS_PER_PACKAGE) % HOT_DOGS_PER_PACKAGE

    # Calculate minimum number of hot dog packages needed
    min_hot_dog_packs_needed = (total_hot_dogs / HOT_DOGS_PER_PACKAGE) + (0 ^ (0 ^ hot_dogs_left_over))

    # Calculate number of left over buns
    buns_left_over = (BUNS_PER_PACKAGE - total_hot_dogs % BUNS_PER_PACKAGE) % BUNS_PER_PACKAGE

    # Calculate min number of bun packages needed
    min_bun_packs_needed = (total_hot_dogs / BUNS_PER_PACKAGE) + (0 ^ (0 ^ buns_left_over))

    # Display min packages of hot dogs needed
    print("Minimum packages of hot dogs needed: {}".format(min_hot_dog_packs_needed))

    # Display minimum packages of buns needed
    print("Minimum packages of hot dog buns needed: {}".format(min_bun_packs_needed))

    # Display num of hot dogs left over
    print("Hot dogs left over: {}".format(hot_dogs_left_over))

    # Display number of buns left over
    print("Hot dog buns left over: {}".format(buns_left_over))

# Main module
def main():
    # Get input for how many hot dogs are needed
    total_hot_dogs = GetTotalHotDogs()

    # Calculate and show results
    ShowResults(total_hot_dogs)

# Run the main() module
main()