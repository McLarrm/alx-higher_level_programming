-- Script: Create Table unique_id
-- Task: Create the table unique_id on the MySQL server
CREATE TABLE IF NOT EXISTS @database_name.unique_id (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
