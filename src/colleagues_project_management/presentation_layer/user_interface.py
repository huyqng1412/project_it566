"""Implements the applicatin user interface."""

from colleagues_project_management.application_base import ApplicationBase
from colleagues_project_management.service_layer.app_services import AppServices
import inspect
import json
import sys 
from prettytable import PrettyTable


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
        print(f'\t6.Exit')

    # Choices for menu selections. #
    def process_menu_choice(self):
        menu_choice = input("\tSelection:")
        match menu_choice[0]:
            case '1':self.list_employees()
            case '6':sys.exit
            case _: print(f'Invalid menu choice item: {menu_choice[0]}')

    # List all the employees in a table format. #
    def list_employees(self):
        try: 
            results = self.app_services.get_all_employees()
            table = PrettyTable()
            table.field_names = ['ID', 'First Name', 'Middle Name', 'Last Name']
            for row in results:
               table.add_row([row[0], row[1], row[2], row[3]])
            print(table)

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')

    def start(self):
        """Start main user interface."""
        while True:
            self.display_menu()
            self.process_menu_choice()

            #self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: User interface started!')