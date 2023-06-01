import unittest
from person import Person
from parameterized import parameterized

class TestPerson(unittest.TestCase):

    @parameterized.expand([
        ("Max Muster", 25, True),  # Adult person
        ("Karl Niemand", 16, False),  # Minor person
        ("Alice Wunderland", 18, True),  # Just turned 18
    ])
    def test_is_adult(self, name, age, expected_result):
        person = Person(name, age)
        self.assertEqual(person.is_adult(), expected_result)
