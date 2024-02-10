-- Set up a mysql user and databases for the project

-- Create a dedicated mysql user
CREATE USER IF NOT EXISTS 'crimson'@'%' IDENTIFIED BY 'hayat_for_all';
GRANT SELECT ON performance_schema.* TO 'crimson'@'%';

-- Reset production database
DROP DATABASE IF EXISTS hayat_prod_db;
CREATE DATABASE hayat_prod_db;
GRANT ALL PRIVILEGES ON hayat_prod_db.* TO 'crimson'@'%';

-- Reset developement database
DROP DATABASE IF EXISTS hayat_dev_db;
CREATE DATABASE hayat_dev_db;
GRANT ALL PRIVILEGES ON hayat_dev_db.* TO 'crimson'@'%';

-- Reset testdatabase
DROP DATABASE IF EXISTS hayat_test_db;
CREATE DATABASE hayat_test_db;
GRANT ALL PRIVILEGES ON hayat_test_db.* TO 'crimson'@'%';

FLUSH PRIVILEGES;
