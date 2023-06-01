from dataclasses import dataclass
from owner import Owner
from license_plate import LicensePlate

@dataclass
class Car:
    make: str
    model: str
    year: int
    license_plate: LicensePlate

