#!/bin/bash

#create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs
echo 'Deleting old log files if they exist...'
rm -f logs/*

d=$(date)
echo $d

# Create Colleague Project Management Database
echo "Running Colleague Project Management Database Scripts..."
echo $d': Dropping database...' | tee -a logs/drop_database.log
mysql < colleague_project_management/drop_database.sql 2>&1 | tee -a logs/drop_database.log
echo $d': Dropping user...' | tee -a logs/drop_user.log
mysql < colleague_project_management/drop_user.sql 2>&1 | tee -a logs/drop_user.log
echo $d': Creating database...' | tee -a logs/create_database.log
mysql < colleague_project_management/create_database.sql 2>&1 | tee -a logs/create_database.log
echo $d': Creating user...' | tee -a logs/create_user.log
mysql < colleague_project_management/create_user.sql 2>&1 | tee -a logs/create_user.log
echo $d': Creating tables...' | tee -a logs/create_tables.log
mysql < colleague_project_management/create_tables.sql 2>&1 | tee -a logs/create_tables.log
echo $d': Inserting employee data...' | tee -a logs/insert_employee_data.log
mysql < colleague_project_management/insert_employee_data.sql 2>&1 | tee -a logs/insert_employee_data.log
echo $d': Inserting project data...' | tee -a logs/insert_project_data.log
mysql < colleague_project_management/insert_project_data.sql 2>&1 | tee -a logs/insert_project_data.log
echo $d': Inserting allocation data...' | tee -a logs/insert_allocation_data.log
mysql < colleague_project_management/insert_allocation_data.sql 2>&1 | tee -a logs/insert_allocation_data.log