# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# Lorena,12/01/2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("Lucas", "Hollis")
        self.assertEqual(person.first_name, "Lucas")
        self.assertEqual(person.last_name, "Hollis")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Hollis")
        with self.assertRaises(ValueError):
            person = Person("Lucas", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("Lucas", "Hollis")
        self.assertEqual(str(person), "Lucas,Hollis")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Lucas", "Hollis", "2024-12-02", 4)
        self.assertEqual(employee.first_name, "Lucas")
        self.assertEqual(employee.last_name, "Hollis")
        self.assertEqual(employee.review_date, "2024-12-02")
        self.assertEqual(employee.review_rating, 4)

    def test_employee_review_date_type(self):  # Test the date validation
        with self.assertRaises(ValueError):
            employee = Employee("Lucas", "Hollis", "invalid_date")

    def test_employee_review_rating_type(self):  # Test the rating validation
        with self.assertRaises(ValueError):
            employee = Employee("Lucas", "Hollis", "2024-12-02", 0)

    def test_employee_str(self):
        student = Employee("Lucas", "Hollis", "2024-12-02", 5)  # Tests the __str__() magic method
        self.assertEqual(str(student), "Lucas,Hollis,2024-12-02,5")

if __name__ == '__main__':
    unittest.main()