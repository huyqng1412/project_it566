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

INSERT INTO `project` (`project_name`, `start_date`, `total_hours`, `total_fte`, `project_dscr`)
VALUES
    ('Talenti Marketing Event', '2025-10-03', '320', '2', 'Creates and distributes an online survey to gather and analyze customer feedback on various Talenti ice cream flavors for a marketing campaign.'),
    ('Stair-Climbing Robot', '2025-08-18', '480', '3', 'Build a robot that can recognize stairs as it approaches them and find a method to climb them. Each attempt to identify stairs will be recorded in a database to help train the robot.'),
    ('Nutrition AI Chatbot', '2025-01-01', '240', '1.5', 'Create a personalized nutrition AI chatbot to answer questions on food, drugs, medicines, and nutrition facts. Chat data will train the AI to meet individual user needs better.'),
    ('Pub Sales System', '2025-02-20', '160', '1', 'Develop a sales system for a Vietnamese pub restaurant to summarize daily sales, collect customer data, and generate sales insights.'),
    ('Mechanic Logging System', '2025-07-15', '200', '1.25', 'Develop a tracking and logging system for mechanical engineers to manage daily workflows and outstanding tasks. Collaboration with a mechanical engineer is required to understand device algorithms for system optimization.')
    ;