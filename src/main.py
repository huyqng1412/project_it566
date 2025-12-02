"""Entry point for the Employee Training Application."""

import json
from argparse import ArgumentParser
from colleagues_project_management.presentation_layer.user_interface import UserInterface
from colleagues_project_management.persistence_layer.mysql_persistence_wrapper import MySQLPersistenceWrapper
from colleagues_project_management.service_layer.app_services import AppServices

def main():
	"""Entry point."""
	args = configure_and_parse_commandline_arguments()

	if args.configfile:
		config = None
		with open(args.configfile, 'r') as f:
			config = json.loads(f.read())

		#service_layer = AppServices(config)
		#employees_list = service_layer.get_all_employees_as_json()
		#print(employees_list)
	
	ui = UserInterface(config)
	ui.start()

	### Returns all the employees information as a list (but it looks horrible).###
	#db = MySQLPersistenceWrapper(config)
	#results = db.select_all_employees()
	#print(results)	

	### Returns all employees in rows that looks cleaner! ###
	app_services = AppServices(config)
	results = app_services.get_all_employees()
	results1 = app_services.get_all_projects()
	results2 = app_services.get_all_assignments()
	results3 = app_services.get_employees_assigned_projects()
	for row in results:
		print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')
		
		print(f'{app_services.get_all_employees_as_json()}')

	for row in results1:
		print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')

		print(f'{app_services.get_all_projects_as_json()}')
	
	for row in results2:
		print(f'{row[0]} {row[1]}')

		print(f'{app_services.get_all_assignments_as_json()}')

	for row in results3:
		print(f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}')

		print(f'{app_services.get_employees_assigned_projects_as_json()}')

def configure_and_parse_commandline_arguments():
	"""Configure and parse command-line arguments."""
	parser = ArgumentParser(
	prog='main.py',
	description='Start the application with a configuration file.',
	epilog='POC: Huy Nguyen | huyqng1412@gmail.com')

	parser.add_argument('-c','--configfile',
					help="Configuration file to load.",
					required=True)
	args = parser.parse_args()
	return args



if __name__ == "__main__":
	main()