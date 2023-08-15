-- Script: List Records with Names and Scores in second_table
-- Task: List all records of the table second_table in the database hbtn_0c_0, excluding rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
