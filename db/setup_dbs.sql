-- Set up a mysql user and databases for the project

-- Create a dedicated mysql user
CREATE USER IF NOT EXISTS 'crimson'@'localhost' IDENTIFIED BY 'hayat_for_all';
GRANT SELECT ON performance_schema.* TO 'crimson'@'localhost';

-- Create production database
CREATE DATABASE IF NOT EXISTS hayat_prod_db;
GRANT ALL PRIVILEGES ON hayat_prod_db.* TO 'crimson'@'localhost';

-- Create developement database
CREATE DATABASE IF NOT EXISTS hayat_dev_db;
GRANT ALL PRIVILEGES ON hayat_dev_db.* TO 'crimson'@'localhost';

-- Create test database
CREATE DATABASE IF NOT EXISTS hayat_test_db;
GRANT ALL PRIVILEGES ON hayat_test_db.* TO 'crimson'@'localhost';

FLUSH PRIVILEGES;
