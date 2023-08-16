-- Script: Create Database hbtn_0d_usa and Table cities
-- Task: Create the database hbtn_0d_usa and the table cities on the MySQL server
CREATE DATABASE IF NOT EXISTS @database_name;
-- SQL Query: Use the hbtn_0d_usa database
USE @database_name;
-- SQL Query: Create the table cities if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
