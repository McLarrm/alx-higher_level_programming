-- Script: Create Table id_not_null
-- Task: Create the table id_not_null on the MySQL server
CREATE TABLE IF NOT EXISTS @database_name.id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);
