-- Script: Create Database hbtn_0d_usa and Table states
-- Task: Create the database hbtn_0d_usa and the table states on the MySQL server
CREATE DATABASE IF NOT EXISTS @database_name;
-- SQL Query: Use the hbtn_0d_usa database
USE @database_name;
-- SQL Query: Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id)
);
