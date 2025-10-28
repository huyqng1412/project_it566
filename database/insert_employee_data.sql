/* Insert data into the 'project_management' database. */

/* Switch to the project_management database. */
USE `project_management`


-- Insert employee data into the employee table.
INSERT INTO employee (first_name, last_name, birthday, gender)
VALUES
    ('Huy', 'Nguyen', '2000-12-14', 'M'),
    ('Long', 'Tran', '1999-02-19', 'M' );

INSERT INTO project (project_name, project_role)
VALUES
    ('1', 'SQL Database', 'Data Engineer'),
    ('2', 'Stair Robot', 'Electrical Enginner');