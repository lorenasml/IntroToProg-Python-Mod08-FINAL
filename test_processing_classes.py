# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# Lorena,12/04/2024,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "Lucas", "LastName": "Hollis", "ReviewDate": "2024-12-04", "ReviewRating": 5},
            {"FirstName": "Mike", "LastName": "Hollis", "ReviewDate": "2024-12-04", "ReviewRating": 3},
            {"FirstName": "Lorena", "LastName": "Hollis", "ReviewDate": "2024-12-04", "ReviewRating": 4}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].last_name, "Hollis") # Check one attribute of the first employee
        self.assertEqual(self.employee_data[1].review_date, "2024-12-04") # Check one attribute of the second employee
        self.assertEqual(self.employee_data[2].first_name, "Lorena") # Check one attribute of the third employee
        self.assertEqual(self.employee_data[2].review_rating, 4) # Check one attribute of the third employee


    def test_write_employee_data_to_file(self):
        # Create some sample employee objects
        sample_employees = [
            data.Employee("Lucas", "Hollis", "2024-12-04", 5),
            data.Employee("Mike", "Hollis", "2024-12-04", 3),
            data.Employee("Lorena", "Hollis", "2024-12-04", 4)
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_employees)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data), len(sample_employees))
        self.assertEqual(file_data[0]["FirstName"], "Lucas")
        self.assertEqual(file_data[1]["ReviewDate"], "2024-12-04")

if __name__ == "__main__":
    unittest.main()