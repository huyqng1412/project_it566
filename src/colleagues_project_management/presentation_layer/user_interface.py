"""Implements the applicatin user interface."""

from colleagues_project_management.application_base import ApplicationBase
from colleagues_project_management.service_layer.app_services import AppServices
import inspect
import json
import sys 
from prettytable import PrettyTable
from datetime import datetime


class UserInterface(ApplicationBase):
    """UserInterface Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = AppServices(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

    # Create a menu for the user interface with selections. #
    def display_menu(self):
        print(f'\n\n\t\tProject Management Application')
        print()
        print(f'\t1.List employees')
        print(f'\t2.List projects')
        print(f'\t3.List project assignments')
        print(f'\t4.List all employees and assigned projects')
        print(f'\t5.Add new employee')
        print(f'\t6.Add new project')
        print(f'\t7.Assign a project to an employee')
        print(f'\t8.Exit')

    # Choices for menu selections. #
    def process_menu_choice(self):
        menu_choice = input("\tSelection:")
        match menu_choice[0]:
            case '1':self.list_employees()
            case '2':self.list_projects()
            case '3':self.list_assignments()
            case '4':self.list_employees_assigned_projects()
            case '5':self.add_employee()
            case '6':self.add_project()
            case '7':self.add_allocation()
            case '8':sys.exit()
            case _: print(f'Invalid menu choice item: {menu_choice[0]}')

    # List all the employees in a table format. #
    def list_employees(self):
        try: 
            results = self.DB.get_all_employees()
            table = PrettyTable()
            table.field_names = ['Employee ID', 'First Name', 'Last Name', 'Birthday', 'Gender']
            for row in results:
               table.add_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    # List all the projects in a table format. #    
    def list_projects(self):
        try:
            results1 = self.DB.get_all_projects()
            table = PrettyTable()
            table.field_names = ['Project ID', 'Project Name', 'Total Hours', 'Total FTE', 'Status']
            for row in results1:
               table.add_row([row[0], row[1], row[2], row[3], row[4]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    # List all the projects and number of employees work on each in a table format. #
    def list_assignments(self):
        try:
            results2 = self.DB.get_all_assignments()
            table = PrettyTable()
            table.field_names = ['Project Name', 'Number of Employees']
            for row in results2:
                table.add_row([row[0], row[1]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    # List all the employees' name, projects, total FTE required for all the projects they work on, 
    # and the total FTE they were assigned for all the projects in a table format. #
    def list_employees_assigned_projects(self):
        try:
            results3 = self.DB.get_employees_assigned_projects()
            table = PrettyTable()
            table.field_names = ['First Name', 'Last Name', 'Assigned Projects', 'Total Project FTE', 'Total Employee FTE', "% FTE"]
            for row in results3:
                table.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
                table.add_row(["", "", "", "", "", ""])
                table.add_row(["", "", "", "", "", ""])
            print(table)
        except Exception as e: 
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    # Add a new employee to the project. #
    def add_employee(self)->None:
        """Add employee"""
        while True:
            print("\n\tAdd Employee...")
            try: 
                first_name = input('First Name: ').strip().title()
                last_name = input('Last Name: ').strip().title()
                birthday_input = input('Birthday (mm/dd/yyy): ').strip().title()
                birthday = datetime.strptime(birthday_input, '%m/%d/%Y')
                gender = input('Gender (M/F): ').strip().upper()
 
                if gender not in ["M", "F"]:
                    print("Please enter either ""M ""for Male or " "F ""for Female!")
                    continue

                new_employee = self.DB.create_employee(first_name, last_name, birthday, gender)

                if new_employee:
                    print(f'\nNew Employee added sucessfully with ID: {new_employee}')
                else:
                    print(f'\nFailed to add new employee.')

                break
            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                    f'{e}')

    # Add a new project to the database. #
    def add_project(self)->None:
        """Add project"""
        while True:
            print("\n\tAdd Project...")
            try:
                project_title = input('Project Title: ').strip().title()
                if not project_title:
                    print('Project Title cannot be empty.')
                    continue
                
                # Total Hours to be numbers only
                total_hours_input = input('Total Hours: ').strip()
                try:
                    total_hours = float(total_hours_input)
                except ValueError:
                    print("Error! Total Hours must be a number.")
                    continue 
                
                # Total FTE to be numbers only
                total_fte_input = input('Total FTE: ').strip()
                try:
                    total_fte = float(total_fte_input)
                except ValueError:
                    print("Error! Total FTE must be a number.")
                    continue 

                status = input('Status (Done/In Progress): ').strip().title()
                status_list = ["Done", "In Progress", "done", "in progress"]
                if status not in status_list:
                    print("Status not eligible!")
                    continue

                new_project = self.DB.create_project(project_title, total_hours, total_fte, status)
                if new_project:
                    print(f'\nA new project has been created, ID: {new_project}')
                else:
                    print('\nFailed to create a new project.')

                break
            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                    f'{e}')

    # Assign a project to an employee and record it to the database. #
    def add_allocation(self)->None:
        """Add allocation"""
        while True:
            print("\n\tAdd an employee assignment...")
            try:
                project_id_input = input("Project ID: ").strip()
                try: 
                    project_id = int(project_id_input)
                except ValueError:
                    print("Error! Project ID must be a number!")
                    continue
                
                employee_id_input = input("Employee ID: ").strip()
                try:
                    employee_id = int(employee_id_input)
                except ValueError:
                    print("Error! Employee ID must be a number!")
                    continue

                assigned_fte_input = input("FTE: ").strip()
                try:
                    assigned_fte = float(assigned_fte_input)
                except ValueError:
                    print("Error! FTE must be a number!")
                    continue

                new_allocation = self.DB.create_allocation(project_id, employee_id, assigned_fte)
                if new_allocation:
                    print(f'\nProject successfully assigned to employee.')
                else:
                    print(f'\nFailed to assign project to employee!')
                
                break
            
            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                    f'{e}')


    def start(self):
        """Start main user interface."""
        while True:
            self.display_menu()
            self.process_menu_choice()

            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: User interface started!')