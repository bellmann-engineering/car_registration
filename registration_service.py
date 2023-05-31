from registration import Registration

class RegistrationService:
    def __init__(self):
        self.registrations = {}

    def register_car(self, car, owner):
        license_plate_number = car.license_plate.number

        if license_plate_number in self.registrations:
            raise ValueError(f"Auto mit dem Kennzeichen {license_plate_number} ist bereits registriert.")

        if not owner.is_adult():
            raise ValueError(f"Person {owner.name} ist nicht volljährig und kann kein Auto registrieren.")

        registration = Registration(owner, car)
        self.registrations[license_plate_number] = registration
        print(f"Auto mit dem Kennzeichen {license_plate_number} wurde registriert.")

    def get_car_owner(self, car):
        for registration in self.registrations.values():
            if registration.car == car:
                return registration.owner
        return None