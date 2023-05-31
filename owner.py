from person import Person

class Owner(Person):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address
