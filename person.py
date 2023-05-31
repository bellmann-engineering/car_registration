from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18


