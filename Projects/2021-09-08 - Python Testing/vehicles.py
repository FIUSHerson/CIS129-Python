class Vehicles:
    def __init__(self, car_type, year) -> None:
        self.car_type = car_type
        self.year = year

x = Vehicles("car", 2020)
print("You have a {} from {}.".format(x.car_type, x.year))

class Snacks:
    def __init__(self, brand, color, is_good) -> None:
        self.brand = brand
        self.color = color
        self.is_good = is_good

cheeto = Snacks("cheeto", "orange", True)
print("{} {} {}".format(cheeto.brand, cheeto.color, cheeto.is_good))