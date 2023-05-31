from dataclasses import dataclass
from typing import Optional
from owner import Owner
from license_plate import LicensePlate

@dataclass
class Car:
    make: str
    model: str
    year: int
    license_plate: LicensePlate
    owner: Optional[Owner] = None

    def register_owner(self):
        self.owner = self.owner
