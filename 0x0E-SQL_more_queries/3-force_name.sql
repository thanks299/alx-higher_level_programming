-- script that creates the table force_name on your MySQL server
-- if database hbtn_0d_2 already exists, your script should not fail
CREATE TABLE IF NOT EXISTS force_name (id INT,name VARCHAR(256) NOT NULL);
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;
