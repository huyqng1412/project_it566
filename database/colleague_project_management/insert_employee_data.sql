/* Insert data into the 'project_management' database. */

/* Switch to the project_management database. */
USE `project_management`


-- Insert employee data into the employee table.
INSERT INTO `employee` (`first_name`, `last_name`, `birthday`, `gender`)
VALUES
    ('Huy', 'Nguyen', '2000-12-14', 'M'),
    ('Long', 'Tran', '1999-02-19', 'M' ),
    ('Sinh', 'Tran', '2001-05-20', 'M'),
    ('Hoang', 'Nguyen', '2001-03-13', 'M'),
    ('Khang', 'Bui', '2000-12-19', 'M'),
    ('Hieu', 'Chau', '1996-02-15', 'M'),
    ('Phuong', 'Huynh', '2004-11-18', 'M'),
    ('Han', 'Tran', '2003-03-13', 'F'),
    ('Bobby', 'Dang', '2000-09-10', 'M')
    ;

