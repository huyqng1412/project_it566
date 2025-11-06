/* Switch to the project_management database. */
USE `project_management`

-- Insert data into the project table.
INSERT INTO `project` (`project_name`, `total_hours`, `total_fte`, `status`, `project_dscr`)
VALUES
    ('Talenti Marketing Event', '320', '2', 'Done', 'Creates and distributes an online survey to gather and analyze customer feedback on various Talenti ice cream flavors for a marketing campaign.'),
    ('Stair-Climbing Robot', '480', '3', 'In Progress', 'Build a robot that can recognize stairs as it approaches them and find a method to climb them. Each attempt to identify stairs will be recorded in a database to help train the robot.'),
    ('Nutrition AI Chatbot', '240', '1.5', 'In Progress', 'Create a personalized nutrition AI chatbot to answer questions on food, drugs, medicines, and nutrition facts. Chat data will train the AI to meet individual user needs better.'),
    ('Pub Sales System', '160', '1', 'Done', 'Develop a sales system for a Vietnamese pub restaurant to summarize daily sales, collect customer data, and generate sales insights.'),
    ('Mechanic Logging System', '200', '1.25', 'In Progress', 'Develop a tracking and logging system for mechanical engineers to manage daily workflows and outstanding tasks. Collaboration with a mechanical engineer is required to understand device algorithms for system optimization.')
    ;