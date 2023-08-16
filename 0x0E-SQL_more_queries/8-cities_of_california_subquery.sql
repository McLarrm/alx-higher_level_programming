-- Script: List Cities of California
-- Task: List all the cities of California from the database hbtn_0d_usa
SELECT * FROM @database_name.cities WHERE state_id = (SELECT id FROM @database_name.states WHERE name = 'California') ORDER BY id ASC;
