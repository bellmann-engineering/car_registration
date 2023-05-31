class RegistrationService:
    def __init__(self):
        self.cars = {}

    def register_car(self, car):
        license_plate_number = car.license_plate.number

        if license_plate_number in self.cars:
            raise ValueError(f"Auto mit dem Kennzeichen {license_plate_number} ist bereits registriert.")

        if not car.owner.is_adult():
            raise ValueError(f"Person {car.owner.name} ist nicht volljährig und kann kein Auto registrieren.")

        self.cars[license_plate_number] = car
        print(f"Auto mit dem Kennzeichen {license_plate_number} wurde registriert.")

    def get_car_by_license_plate(self, license_plate_number):
        if license_plate_number in self.cars:
            return self.cars[license_plate_number]
        return None

    def get_car_owner(self, car):
        return car.owner
