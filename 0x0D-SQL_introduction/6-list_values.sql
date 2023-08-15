-- Script: List All Rows of first_table
-- Task: List all rows of the table first_table from the database hbtn_0c_0
SET @database_name = IFNULL(@@ARGS[1], 'hbtn_0c_0');
SELECT *
FROM @database_name.first_table;
