import json
from data_classes import Employee
from presentation_classes import IO

class FileProcessor:
    """
    A class to process employee data from files, including reading from and writing to JSON files.

    Methods:
        read_employee_data_from_file(file_name: str, employee_data: list): Reads employee data from a file and loads it into a list of Employee objects.
        write_employee_data_to_file(file_name: str, employee_data: list): Writes employee data from a list of Employee objects to a file.
    """
    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list):
        """
        Reads employee data from a JSON file and converts it into Employee objects.

        Args:
            file_name (str): The name of the file to read data from.
            employee_data (list): The list to which the employee objects will be added.

        Returns:
            list: The updated list of employee objects.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
            for employee in list_of_dictionary_data:  # Convert the list of dictionary rows into Employee objects
                employee_object = Employee
                employee_object.first_name=employee["FirstName"]
                employee_object.last_name= employee["LastName"]
                employee_object.review_date=employee["ReviewDate"]
                employee_object.review_rating=employee["ReviewRating"]
                employee_data.append(employee_object)

        except FileNotFoundError as e:
            IO.output_error_messages(f"The file {file_name} does not exist. Please check the file path.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """
        Writes employee data from a list of Employee objects to a JSON file.

        Args:
            file_name (str): The name of the file to write data to.
            employee_data (list): The list of Employee objects to write to the file.

        Raises:
            IOError: If there's an issue with writing to the file (e.g., permissions or path issue).
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of Employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating}
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=4)
        except IOError as e:
            IO.output_error_messages(f"Error: Could not write to file '{file_name}'. Please check file permissions and path.", e)
        except Exception as e:  # catch all
            IO.output_error_messages("There was a non-specific error!", e)

        print("Employee data successfully saved!")
