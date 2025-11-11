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


    def get_all_employees_as_json(self)->str:
            """Returns a list of employees from the persistence layer in JSON."""
            try:
                results = self.DB.select_all_employees()
                return json.dumps(results)

            except Exception as e:
                self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: It works!')
