# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08
# # Description: main program script. User can select to add, display and save employee rating data
# ChangeLog: (Who, When, What)
    # Lorena,11/30/2024,Created Script
    # Lorena, 12/01/2024,Created Script
# ------------------------------------------------------------------------------------------------- #

import processing_classes as proc
import presentation_classes as pres
import data_classes as data

employees: list = []  # a table of employee data
menu_choice = ''

employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME, employee_data=employees)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":
        try:
            pres.IO.input_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":
        break  # out of the while loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
