/* ***********************************************************
Drop and Create tables for the project_management database.
************************************************************** */
/* Switch to project_management database */
USE project_management

/* Drop the table 'employee' if it already exists */
DROP TABLE IF EXISTS employee;

/* Create the 'employee' table */
CREATE TABLE IF NOT EXISTS employee (
    id int(20) NOT NULL,
    first_name varchar(25) NOT NULL,
    last_name varchar(25) NOT NULL, 
    birthday date NOT NULL,
    gender char(1) NOT NULL
);

/* Alter the 'id' column to the table's primary key */
ALTER TABLE employee
    ADD PRIMARY KEY (id);

ALTER TABLE employee
    MODIFY id int(20) NOT NULL AUTO_INCREMENT;

/* Drop the table 'project' if it already exists */ 
DROP TABLE IF EXISTS project;

/* Create the 'project' table */
CREATE TABLE IF NOT EXISTS project (
    
)


