from dataclasses import dataclass
from owner import Owner
from car import Car

@dataclass
class Registration:
    owner: Owner
    car: Car