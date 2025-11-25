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
        print(f'\t6.Exit')

    # Choices for menu selections. #
    def process_menu_choice(self):
        menu_choice = input("\tSelection:")
        match menu_choice[0]:
            case '1':self.list_employees()
            case '2':self.list_projects()
            case '3':self.list_assignments()
            case '4':self.list_employees_assigned_projects()
            case '5':self.add_employee()
            case '6':sys.exit()
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

    def list_employees_assigned_projects(self):
        try:
            results3 = self.DB.get_employees_assigned_projects()
            table = PrettyTable()
            table.field_names = ['First Name', 'Last Name', 'Assigned Projects']
            for row in results3:
                table.add_row([row[0], row[1], row[2]])
                table.add_row(["", "", ""])
                table.add_row(["", "", ""])
            print(table)
        except Exception as e: 
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    def add_employee(self)->None:
        """Add employee"""
        print("\n\tAdd Employee...")
        employee = 
        try: 
            employee.first_name = input('First Name: ')
            employee.last_name = input('Last Name: ')
            birthday_input = input('Birthday (mm/dd/yyy): ')
            employee.birthday = datetime.strptime(birthday_input, '%m/%d/%Y')
            employee.gender = input('Gender (M/F): ')
            employee = self.DB.create_employee(employee=employee)
            print(f'New employee id: {employee.id}')


        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: ' \
                                f'{e}')
    def start(self):
        """Start main user interface."""
        while True:
            self.display_menu()
            self.process_menu_choice()

            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: User interface started!')