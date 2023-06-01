from person import Person

class TestPerson(unittest.TestCase):
    def test_is_adult(self):
        # Test case 1: Person is an adult
        adult_person = Person("John Doe", 25)
        self.assertTrue(adult_person.is_adult())

        # Test case 2: Person is not an adult
        minor_person = Person("Jane Smith", 16)
        self.assertFalse(minor_person.is_adult())

        # Test case 3: Person just turned 18
        just_turned_18 = Person("Alice Brown", 18)
        self.assertTrue(just_turned_18.is_adult())
