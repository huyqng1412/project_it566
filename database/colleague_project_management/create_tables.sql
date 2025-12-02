/* ***********************************************************
Drop and Create tables for the project_management database.
************************************************************** */
/* Switch to project_management database */
USE `project_management`

/* Drop the table 'employee' if it already exists */
DROP TABLE IF EXISTS `employee`;

/* Create the 'employee' table */
CREATE TABLE IF NOT EXISTS `employee` (
    `employee_id` INT(20) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(25) NOT NULL,
    `last_name` VARCHAR(25) NOT NULL, 
    `birthday` DATE NOT NULL,
    `gender` CHAR(1) NOT NULL /*DEFAULT 'M'*/ CHECK (`gender` IN ('M', 'F'))
) AUTO_INCREMENT = 1;

/* Alter the 'id' column to the table's primary key 
ALTER TABLE employee
    ADD PRIMARY KEY (id);

ALTER TABLE employee
    MODIFY id int(20) NOT NULL AUTO_INCREMENT;
*/

/* Drop the table 'project' if it already exists */ 
DROP TABLE IF EXISTS `project`;

/* Create the 'project' table */
CREATE TABLE IF NOT EXISTS `project` (
    `project_id` INT(15) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `project_name` VARCHAR(30) NOT NULL,
    `total_hours` FLOAT NOT NULL,
    `total_fte` FLOAT NOT NULL,
    `status` VARCHAR(20) NOT NULL CHECK (`status` IN ('Done', 'In Progress'))
) AUTO_INCREMENT = 1000;

/* Drop the table 'project_allocations' if it already exists */ 
DROP TABLE IF EXISTS `project_allocations`;

/* Create the 'project_allocations' table */
CREATE TABLE IF NOT EXISTS `project_allocations` (
    `project_id` INT(15) NOT NULL,
    `employee_id` INT(20) NOT NULL,
    `assigned_fte` DECIMAL(3,2) NOT NULL
); 

/* Create indexes on project_id and employee_id columns */
ALTER TABLE `project_allocations`
    ADD KEY `fk_project_allocations_1`(`project_id`),
    ADD KEY `fk_project_allocations_2`(`employee_id`);

/* Add Cascade Delete Constraint on employee_id column */
ALTER TABLE `project_allocations`
    ADD CONSTRAINT `fk_project_allocations_2` 
    FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

/* Add Cascade Delete Constraint on project_id column */
ALTER TABLE `project_allocations`
    ADD CONSTRAINT `fk_project_allocations_1` 
    FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`)
    ON UPDATE CASCADE;





