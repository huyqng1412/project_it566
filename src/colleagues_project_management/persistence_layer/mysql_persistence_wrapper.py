"""Defines the MySQLPersistenceWrapper class."""

from colleagues_project_management.application_base import ApplicationBase
from mysql import connector
from mysql.connector.pooling import (MySQLConnectionPool)
import inspect
import json
from typing import List

class MySQLPersistenceWrapper(ApplicationBase):
	"""Implements the MySQLPersistenceWrapper class."""

	def __init__(self, config:dict)->None:
		"""Initializes object. """
		self._config_dict = config
		self.META = config["meta"]
		self.DATABASE = config["database"]
		super().__init__(subclass_name=self.__class__.__name__, 
				   logfile_prefix_name=self.META["log_prefix"])
		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}:It works!')

		# Database Configuration Constants
		self.DB_CONFIG = {}
		self.DB_CONFIG['database'] = \
			self.DATABASE["connection"]["config"]["database"]
		self.DB_CONFIG['user'] = self.DATABASE["connection"]["config"]["user"]
		self.DB_CONFIG['host'] = self.DATABASE["connection"]["config"]["host"]
		self.DB_CONFIG['port'] = self.DATABASE["connection"]["config"]["port"]

		self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: DB Connection Config Dict: {self.DB_CONFIG}')

		# Database Connection
		self._connection_pool = \
			self._initialize_database_connection_pool(self.DB_CONFIG)
		

		# SQL String Constants
		self.SELECT_ALL_EMPLOYEES = \
			f'SELECT employee_id, first_name, last_name, birthday, gender ' \
			f'FROM employee'

		self.SELECT_ALL_PROJECTS = \
			f'SELECT project_id, project_name, total_hours, total_fte, status ' \
			f'FROM project'
		
		self.SELECT_ASSIGNMENTS = \
			f'SELECT p.project_name, COUNT(e.employee_id)' \
			f'FROM project_allocations pa ' \
			f'INNER JOIN project p ON pa.project_id = p.project_id ' \
			f'INNER JOIN employee e ON pa.employee_id = e.employee_id ' \
			f'GROUP BY p.project_name ' \
			f'ORDER BY p.project_name' 
		
		self.SELECT_EMPLOYEES_ASSIGNED_PROJECTS = \
			f"SELECT e.first_name, e.last_name, GROUP_CONCAT('   • ', p.project_name SEPARATOR '\n') " \
			f"FROM project_allocations pa " \
			f"INNER JOIN employee e ON e.employee_id = pa.employee_id " \
			f"INNER JOIN project p ON p.project_id = pa.project_id " \
			f"GROUP BY e.employee_id " \
			f"ORDER BY e.employee_id"
		
		self.INSERT_EMPLOYEE = \
			f"INSERT INTO employee " \
			f"(first_name, last_name, birthday, gender) " \
			f"VALUES(%s, %s, %s, %s)"

		self.INSERT_PROJECT = \
			f"INSERT INTO project " \
			f"(project_name, total_hours, total_fte, status) " \
			f"VALUES(%s, %s, %s, %s)"
		
		self.INSERT_ALLOCATIONS = \
			f"INSERT INTO project_allocations " \
			f"(project_id, employee_id, assigned_fte) " \
			f"VALUES(%s, %s, %s)"
		

	# MySQLPersistenceWrapper Methods
	def select_all_employees(self)->List:
		"""Returns a list of all employee rows."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_EMPLOYEES)
					results = cursor.fetchall()

			return results
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	
	def select_all_projects(self)->List:
		"""Returns a list of all project rows."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ALL_PROJECTS)
					results = cursor.fetchall()

			return results
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	def select_assignments(self)->List:
		"""Returns a list of all project allocations rows."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_ASSIGNMENTS)
					results = cursor.fetchall()

			return results
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

	
	def select_employees_assigned_projects(self)->List:
		"""Returns a list of all employees and their assigned projects rows."""
		cursor = None
		results = None
		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(self.SELECT_EMPLOYEES_ASSIGNED_PROJECTS)
					results = cursor.fetchall()

			return results
		
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')



	def create_employee(self, first_name, last_name, birthday, gender): #->List:
		"""Create a new record in the employees table."""
		cursor = None
		
		try: 
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(
						self.INSERT_EMPLOYEE,
						(first_name, last_name, birthday, gender)
					)				
					connection.commit()
					#self._logger.log_debug(f'Updated {cursor.rowcount} row.')
					#self._logger.log_debug(f'Last Row ID: {cursor.lastrowid}.')
					new_id = cursor.lastrowid
			return new_id
		
		except Exception as e: 
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


	def create_project(self, project_title, total_hours, total_fte, status):
		"""Create a new record in the projects table."""
		cursor = None

		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(
						self.INSERT_PROJECT,
						(project_title, total_hours, total_fte, status)
					)
					connection.commit()
					new_id = cursor.lastrowid
			return new_id

		except Exception as e: 
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')

		
	def create_allocation(self, project_id, employee_id, assigned_fte):
		"""Create a new record in the project allocations table"""
		cursor = None

		try:
			connection = self._connection_pool.get_connection()
			with connection:
				cursor = connection.cursor()
				with cursor:
					cursor.execute(
						self.INSERT_ALLOCATIONS,
						(project_id, employee_id, assigned_fte)
					)
					connection.commit()
					new_allocation = cursor.lastrowid
			return new_allocation

		except Exception as e: 
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: {e}')


		##### Private Utility Methods #####

	def _initialize_database_connection_pool(self, config:dict)->MySQLConnectionPool:
		"""Initializes database connection pool."""
		try:
			self._logger.log_debug(f'Creating connection pool...')
			cnx_pool = \
				MySQLConnectionPool(pool_name = self.DATABASE["pool"]["name"],
					pool_size=self.DATABASE["pool"]["size"],
					pool_reset_session=self.DATABASE["pool"]["reset_session"],
					use_pure=self.DATABASE["pool"]["use_pure"],
					**config)
			self._logger.log_debug(f'{inspect.currentframe().f_code.co_name}: Connection pool successfully created!')
			return cnx_pool
		except connector.Error as err:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Problem creating connection pool: {err}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}: Check DB cnfg:\n{json.dumps(self.DATABASE)}')
		except Exception as e:
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Problem creating connection pool: {e}')
			self._logger.log_error(f'{inspect.currentframe().f_code.co_name}:Check DB conf:\n{json.dumps(self.DATABASE)}')
