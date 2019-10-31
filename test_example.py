import unittest

from example_class import Person


class ExampleTests(unittest.TestCase):

    def test_person_has_name(self):
        self.assertEqual('Taylor', Person('Taylor', 'Hobbs').name)

    def test_person_has_last_name(self):
        self.assertEqual('Hobbs', Person('Taylor', 'Hobbs').last_name)

    def test_person_has_can_return_full_name(self):
        self.assertEqual('Taylor Hobbs', Person('Taylor', 'Hobbs').full_name)
        self.assertEqual('Maddy Hobbs', Person('Maddy', 'Hobbs').full_name)

    def test_person_can_do_simple_math(self):
        self.assertEqual('Taylor Hobbs', Person('Taylor', 'Hobbs').full_name)
        self.assertEqual('Maddy Hobbs', Person('Maddy', 'Hobbs').full_name)


if __name__ == '__main__':
    unittest.main()
