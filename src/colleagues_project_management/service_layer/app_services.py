"""Implements AppServices Class."""

from colleagues_project_management.application_base import ApplicationBase
from colleagues_project_management.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
import inspect
import json

class AppServices(ApplicationBase):
    """AppServices Class Definition."""
    def __init__(self, config:dict)->None:
        """Initializes object. """
        self._config_dict = config
        self.META = config["meta"]
        super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
        self.DB = MySQLPersistenceWrapper(config)
        self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')


    def get_all_employees(self)->list:
        """Returns a list of employees from the persistence layer."""
        try:
            results = self.DB.select_all_employees()
            return results

        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_all_projects(self)->list:
        """Returns a list of projects from the persistence layer."""
        try:
            results = self.DB.select_all_projects()
            return results 
         
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_all_assignments(self)->list:
        """Returns a list of project allcoations from the persistence layer."""
        try:
            results = self.DB.select_assignments()
            return results 
         
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_employees_assigned_projects(self)->list:
        """Returns a list of all employees and assigned projects from the persistence layer."""
        try:
            results = self.DB.select_employees_assigned_projects()
            return results 
         
        except Exception as e:
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_all_employees_as_json(self)->str:
            """Returns a list of employees from the persistence layer in JSON."""
            try:
                results = self.DB.select_all_employees()
                return json.dumps(results)

            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_all_projects_as_json(self)->str:
            """Returns a list of employees from the persistence layer in JSON."""
            try:
                results = self.DB.select_all_projects()
                return json.dumps(results)

            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_all_assignments_as_json(self)->str:
            """Returns a list of project allocations from the persistence layer in JSON."""
            try:
                results = self.DB.select_assignments()
                return json.dumps(results)

            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def get_employees_assigned_projects_as_json(self)->str:
            """Returns a list of all employees and assigned projects from the persistence layer in JSON."""
            try:
                results = self.DB.select_employees_assigned_projects()
                return json.dumps(results)

            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')


    def create_employee(self, first_name, last_name, birthday, gender): #->list:
        """Create a new employee in the database"""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            new_employee = self.DB.create_employee(first_name, last_name, birthday, gender)
            return new_employee
        except Exception as e: 
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')


    def create_project(self, project_title, total_hours, total_fte, status):
        """Create a new project in the database"""
        self._logger.log_debug(f'In {inspect.currentframe().f_code.co_name}()...')
        try:
            new_project = self.DB.create_project(project_title, total_hours, total_fte, status)  
            return new_project
        except Exception as e: 
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')


    def create_allocation(self, project_id, employee_id, assigned_fte):
        """Create new assignments for employees in the database"""
        self._logger.log_debug((f'In {inspect.currentframe().f_code.co_name}()...'))
        try:
            new_allocation = self.DB.create_allocation(project_id, employee_id, assigned_fte)
            return json.dumps(new_allocation)
        except Exception as e: 
            self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:{e}')