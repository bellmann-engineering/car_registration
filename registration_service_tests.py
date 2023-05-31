import unittest
from license_plate import LicensePlate
from person import Person
from owner import Owner
from car import Car
from registration_service import RegistrationService

class RegistrationServiceTests(unittest.TestCase):
    def setUp(self):
        self.registration_service = RegistrationService()

    def test_register_car(self):
        # Arrange
        license_plate = LicensePlate("M-KB-123", "BY")
        owner = Owner("Max Mustermann", 30, "Hauptstraße 123, Berlin")
        car = Car("Audi", "A1", 2022, license_plate)

        # Act
        self.registration_service.register_car(car, owner)

        # Assert
        self.assertIn(license_plate.number, self.registration_service.registrations.keys(),
                      f"Das Auto mit dem Kennzeichen {license_plate.number} sollte registriert sein.")
        self.assertEqual(self.registration_service.registrations[license_plate.number].owner, owner,
                         f"Der Besitzer des Autos mit dem Kennzeichen {license_plate.number} sollte {owner.name} sein.")

    def test_register_car_already_registered(self):
        # Arrange
        license_plate = LicensePlate("M-KB-123", "BY")
        owner = Owner("Max Mustermann", 30, "Hauptstraße 123, Berlin")
        car = Car("Audi", "A1", 2022, license_plate)
        self.registration_service.register_car(car, owner)

        # Act & Assert
        with self.assertRaises(ValueError):
            self.registration_service.register_car(car, owner)

    def test_register_car_owner_underage(self):
        # Arrange
        license_plate = LicensePlate("M-KB-123", "BY")
        underage_owner = Owner("Fritz Müller", 16, "Am Bach 5, Hamburg")
        car = Car("Audi", "A1", 2022, license_plate)

        # Act & Assert
        with self.assertRaises(ValueError):
            self.registration_service.register_car(car, underage_owner)

    def test_get_car_owner_registered(self):
        # Arrange
        license_plate = LicensePlate("M-KB-123", "BY")
        owner = Owner("Max Mustermann", 30, "Hauptstraße 123, Berlin")
        car = Car("Audi", "A1", 2022, license_plate)
        self.registration_service.register_car(car, owner)

        # Act
        retrieved_owner = self.registration_service.get_car_owner(car)

        # Assert
        self.assertEqual(retrieved_owner, owner,
                         f"Der Autobesitzer des Autos mit dem Kennzeichen {license_plate.number} sollte {owner.name} sein.")

    def test_get_car_owner_not_registered(self):
        # Arrange
        license_plate = LicensePlate("M-KB-123", "BY")
        car = Car("Audi", "A1", 2022, license_plate)

        # Act
        retrieved_owner = self.registration_service.get_car_owner(car)

        # Assert
        self.assertIsNone(retrieved_owner, "Der Autobesitzer sollte None sein, da das Auto nicht registriert ist.")

if __name__ == "__main__":
    unittest.main()
