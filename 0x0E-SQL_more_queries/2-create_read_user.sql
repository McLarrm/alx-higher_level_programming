-- Script: Create Database hbtn_0d_2 and User user_0d_2
-- Task: Create the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- SQL Query: Create the user if it doesn't exist, and grant SELECT privilege with the specified password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
