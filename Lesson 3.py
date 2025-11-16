class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passengers in {self.brand}")

Bob = Human("Bob")
Carl = Human("Carl")
car = Auto("Porshe")
car.add_passenger(Bob)
car.add_passenger(Carl)
car.print_passengers_names()





