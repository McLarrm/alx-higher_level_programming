-- Script: Create Table force_name
-- Task: Create the table force_name on the MySQL server
CREATE TABLE IF NOT EXISTS @database_name.force_name (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
