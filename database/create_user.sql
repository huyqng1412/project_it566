/* ****************************************
Drop and create the project_management_user
**************************************** */

-- Drop user if exists
DROP USER IF EXISTS 'project_management_user'@'%';

-- Create user if not exists
CREATE USER IF NOT EXISTS 'project_management_user'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'project_management_user'@'%';
ALTER USER 'project_management_user'@'%'
    REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 0
    MAX_CONNECTIONS_PER_HOUR 0
    MAX_UPDATES_PER_HOUR 0
    MAX_USER_CONNECTIONS 0;
GRANT ALL PRIVILEGES ON `project\_management\_user\_%`.*
    TO 'project_management_user'@'%';
GRANT ALL PRIVILEGES ON `project\_management`.*
    TO 'project_management_user'@'%' WITH GRANT OPTION; 