for i in range(3):
    user_input = input("Do you want to know? [Y/n]: ")

    if user_input == "y" or user_input == "Y":
        career = "Computer Science"

        print("My major is:\n{}".format(career))
        print("I plan to be a software developer.")
        print("Programming is fun!")
        exit()
    else:
        print("Hmm... I don't like your answer.")
        if i == 2:
            print("Whatever. I'm done with you.")