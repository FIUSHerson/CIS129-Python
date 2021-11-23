# Program written by Alexander Anthis
# Date: 2021-11-17
# Written for CIS129

# Class definitions
class Pet:
    # Init the object with predefined vars
    def __init__(self, p_name, p_type, p_age) -> None:
        super().__init__()
        self.pet_name = p_name
        self.pet_type = p_type
        
        # Age requires input validation with 0 as default
        try:
            self.pet_age = int(p_age)
        except Exception as ex:
            print("An error occurred: [{}] \nSetting age to 0.".format(ex))
            self.pet_age = 0


    # Get and Set modules for each variable in accordance to the project.
    def set_name(self, name):
        self.pet_name = name
    
    def get_name(self):
        return self.pet_name


    def set_type(self, ptype):
        self.pet_type = ptype

    def get_type(self):
        return self.pet_type


    def set_age(self, age):
        self.pet_age = age

    def get_age(self):
        return self.pet_age


def main():
    # Get user input
    p_name = input("Enter your pet's name: ")
    p_type = input("Enter your pet's type: ")
    p_age = input("Enter your pet's age: ")

    # Turn user input into an object
    user_pet = Pet(p_name, p_type, p_age)

    # Print results
    print()
    print("Your pet name: {}".format(user_pet.get_name()))
    print("Your pet type: {}".format(user_pet.get_type()))
    print("Your pet age: {}".format(user_pet.get_age()))
    

main()