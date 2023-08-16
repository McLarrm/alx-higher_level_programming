-- Script: List All Cities with State Names
-- Task: List all cities along with their IDs and corresponding state names from the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS state_name FROM @database_name.cities JOIN @database_name.states ON cities.state_id = states.id ORDER BY cities.id ASC;
