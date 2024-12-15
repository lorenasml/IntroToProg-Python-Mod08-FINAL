from datetime import date

# Data -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

class Person:
    """
    A class to represent a person with a first name and a last name.

    Attributes:
        first_name (str): The person's first name.
        last_name (str): The person's last name.

    Methods:
        __str__: Returns a string representation of the person's full name.
    """
    def __init__(self, first_name: str = "", last_name: str = ""):
        """
        Initializes a new Person object with optional first and last names.

        Args:
            first_name (str): The first name of the person (default is an empty string).
            last_name (str): The last name of the person (default is an empty string).
        """
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first name of the person and first letter is uppercase.

        Returns:
            str: The capitalized first name of the person.
        """
        return self.__first_name.title()

    @first_name.setter
    def first_name(self, value: str):
        """
        Sets the first name of the person, ensuring it contains only alphabetic characters or is empty.

        Args:
            value (str): The first name to be set.

        Raises:
            ValueError: If the value contains non-alphabetical characters or is not empty.
        """
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("First name cannot contain numbers.")

    @property
    def last_name(self):
        """
        Gets the last name of the person, first letter uppercase.

        Returns:
            str: The capitalized last name of the person.
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value:str):
        """
        Sets the last name of the person, ensuring it contains only alphabetic characters or is empty.

        Args:
            value (str): The last name to be set.

        Raises:
            ValueError: If the value contains non-alphabetical characters or is not empty.
        """
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError ("Last name cannot contain numbers.")

    def __str__(self):
        """
        Returns the full name of the person in the format 'FirstName,LastName'.

        Returns:
            str: The full name of the person, with first and last names separated by a comma.
        """
        return f"{self.first_name},{self.last_name}"

class Employee(Person):
    """
    A class to represent an employee, inheriting from the Person class and adding review details.

    Attributes:
        first_name (str): The first name of the employee.
        last_name (str): The last name of the employee.
        review_date (str): The date of the employee's review in the format YYYY-MM-DD.
        review_rating (int): The rating given to the employee (between 1 and 5).

    Methods:
        __str__: Returns a string representation of the employee, including their full name, review date, and review rating.
    """
    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3):
        """
        Initializes a new Employee object with personal details, review date, and review rating.

        Args:
            first_name (str): The first name of the employee (default is an empty string).
            last_name (str): The last name of the employee (default is an empty string).
            review_date (str): The date of the employee's review (default is "1900-01-01").
            review_rating (int): The rating given to the employee (default is 3).

        """
        super().__init__(first_name = first_name, last_name = last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    def review_date(self):
        """
        Gets the review date of the employee.

        Returns:
            str: The review date of the employee in the format YYYY-MM-DD.
        """
        return self.__review_date

    @review_date.setter
    def review_date(self, value: str):
        """
        Sets the review date of the employee, ensuring the correct format (YYYY-MM-DD).

        Args:
            value (str): The review date to be set.

        Raises:
            ValueError: If the date is not in the correct format (YYYY-MM-DD).
        """
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    def review_rating(self):
        """
        Gets the review rating of the employee.

        Returns:
            int: The review rating of the employee.
        """
        return self.__review_rating

    @review_rating.setter
    def review_rating(self, value: str):
        """
        Sets the review rating of the employee, ensuring the value is between 1 and 5.

        Args:
            value (int): The review rating to be set.

        Raises:
            ValueError: If the rating is not an integer between 1 and 5.
        """
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        """
        Returns a string representation of the employee, including their full name, review date, and review rating.

        Returns:
            str: A formatted string containing the employee's full name, review date, and review rating.
        """
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
