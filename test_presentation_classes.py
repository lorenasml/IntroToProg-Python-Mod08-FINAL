# ------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: A collection of tests for the presentation classes module
# ChangeLog: (Who, When, What)
# Lorena,12/03/2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for employee data
        with patch('builtins.input', side_effect=['Lucas', 'Hollis', '2024-12-03', '5']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Lucas')
            self.assertEqual(self.employee_data[0].last_name, 'Hollis')
            self.assertEqual(self.employee_data[0].review_date, '2024-12-03')
            self.assertEqual(self.employee_data[0].review_rating, 5)

        # Simulate invalid review date input (incorrect format)
        with patch('builtins.input', side_effect=['Lucas', 'Hollis', '03/12/2024', '5']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid review rating input (non-integer)
        with patch('builtins.input', side_effect=['Lucas', 'Hollis', '2024-12-03', '123']):
            IO.input_employee_data(self.employee_data)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()