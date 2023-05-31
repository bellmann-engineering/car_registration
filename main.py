from license_plate import LicensePlate
from person import Person
from owner import Owner
from car import Car
from registration_service import RegistrationService

license_plate = LicensePlate("M-KB-123", "BY")

owner = Owner("Max Mustermann", 30, "Hauptstraße 123, Berlin")

car = Car("Audi", "A1", 2022, license_plate, owner)

registration_service = RegistrationService()

registration_service.register_car(car)

# Versuche das gleiche Auto erneut zu registrieren (sollte eine Exception werfen)
registration_service.register_car(car)

car_owner = registration_service.get_car_owner(car)
print(f"Der Besitzer des Autos ist {car_owner.name}.")
