import data_classes as data

class IO:
    """
    A collection of presentation functions that manage user input and output
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        Displays a custom error message to the user and optionally includes technical details for debugging.

        Args:
            message (str): A custom error message that will be displayed to the user.
            error (Exception, optional): An optional exception object that contains technical error details.
                                        If provided, additional error information will be printed for debugging.

        Returns:
            None: This function does not return any value, but it prints the error messages to the console.
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu:str):
        """
        Displays a menu of choices to the user.

        Args:
            menu (str): A string representing the menu to be displayed. This could be a list of options
                         or a formatted string to show to the user.

        Returns:
            None: This function does not return any value, but it prints the menu to the console.
        """
        print()  # Adding extra space to make it look nicer.
        print(data.MENU)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """
        Prompts the user to input a menu choice and returns the user's selection.

        This function displays a prompt asking the user to enter a menu choice (typically a number),
        then returns the user's input as a string.

        Returns:
            str: The user's input choice, which is returned as a string.
        """
        choice = input("Enter your menu choice number: ")
        return choice

    @staticmethod
    def input_employee_data(employee_data: list):
        """
        Prompts the user for employee information and adds a new Employee object to the given list.

        This function collects the employee's first name, last name, review date, and review rating
        from the user. The review date is expected to be in the format YYYY-MM-DD, and the review rating
        must be an integer between 1 and 5.

        Args:
            employee_data (list): A list where the new Employee object will be appended.

        Returns:
            list: The updated list of employee data with the newly added Employee object.

        Raises:
            ValueError: If the review rating is not an integer between 1 and 5, or if the review date
                        is not in the correct format.
        """
        try:
            employee_object = data.Employee() # Instantiate a new employee object
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is the date of the review? ")
            employee_object.review_rating = int(input("What is the employee's rating? "))
            employee_data.append(employee_object)  # Add the employee object to the list

            print()
            print(f"You have rated {employee_object.first_name} {employee_object.last_name} "
                  f"with a rating of {employee_object.review_rating} on {employee_object.review_date}.")

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:  # catch-all
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data

    @staticmethod
    def output_employee_data(employee_data: list):
        """
        Outputs the employee data in a formatted manner with the review ratings and descriptions.

        Args:
            employee_data (list): A list of Employee objects whose data will be displayed.

        This function will print the first name, last name, review date, and rating description for each employee.
        The rating descriptions are mapped as follows:
            5 -> "Greatly Exceeds Expectations"
            4 -> "Exceeds Expectations"
            3 -> "Meets Expectations"
            2 -> "Meets Some Expectations"
            1 -> "Does Not Meet Expectations"
        """
        message: str = ""

        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = " {} {} has been rated as 5 (GE -- Greatly Exceeds Expectations)"
            elif employee.review_rating == 4:
                message = " {} {} has been rated as 4 (EE -- Exceeds Expectations)"
            elif employee.review_rating == 3:
                message = " {} {} has been rated as 3 (ME -- Meets Expectations)"
            elif employee.review_rating == 2:
                message = " {} {} has been rated as 2 (Meets Some Expectations)"
            elif employee.review_rating == 1:
                message = " {} {} has been rated as 1 (Does Not Meet Expectations)"

            print(message.format(employee.first_name, employee.last_name, employee.review_date, employee.review_rating))
        print("-" * 50)