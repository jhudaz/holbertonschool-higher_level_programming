-- create a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
        id INT AUTO_INCREMENT,
        name VARCHAR(256),
        UNIQUE(id),
        PRIMARY KEY(id)
    )
