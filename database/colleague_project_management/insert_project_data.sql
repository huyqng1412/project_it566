/* Switch to the project_management database. */
USE `project_management`

-- Insert data into the project table.
INSERT INTO `project` (`project_name`, `total_hours`, `total_fte`, `status`)
VALUES
    ('Talenti Marketing Event', '320', '2', 'Done'),
    ('Stair-Climbing Robot', '480', '3', 'In Progress'),
    ('Nutrition AI Chatbot', '240', '1.5', 'In Progress'),
    ('Pub Sales System', '160', '1', 'Done'),
    ('Mechanic Logging System', '200', '1.25', 'In Progress')
    ;