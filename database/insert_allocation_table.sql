/* Insert data into the 'project_management' database. */

/* Switch to the project_management database. */
USE `project_management`

/* Insert data into the project_allocations table */
INSERT INTO `project_allocations` (`employee_id`, `project_id`, `assigned_fte`)
VALUES
    ('8', '1000', '0.5'),
    ('7', '1000', '0.5'),
    ('1', '1000', '0.5'),
    ('9', '1000', '0.5'),

    ('2', '1001', '1'),
    ('3', '1001', '0.5'),
    ('4', '1001', '0.5'),
    ('1', '1001', '1'),

    ('5', '1002', '0.5'),
    ('1', '1002', '0.25'),
    ('7', '1002', '0.25'),
    ('6', '1002', '0.25'),

    ('3', '1002', '0.25'),
    ('6', '1003', '0.5'),
    ('1', '1003', '0.15'), 
    ('8', '1003', '0.15'),
    ('9', '1003', '0.2'),

    ('4', '1004', '0.5'),
    ('2', '1004', '0.25'),
    ('3', '1004', '0.25'),
    ('1', '1004', '0.25')