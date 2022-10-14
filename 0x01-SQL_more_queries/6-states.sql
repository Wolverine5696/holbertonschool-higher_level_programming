-- Write a script that creates the table unique_id on your MySQL server.
--  unique_id description:
--  id INT with the default value 1 and must be unique
--  name VARCHAR(256)
--  The database name will be passed as an argument of the mysql command
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
	)
