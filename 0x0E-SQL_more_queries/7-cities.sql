-- create a database and a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
        id INT AUTO_INCREMENT,
        state_id INT,
        name VARCHAR(256),
        UNIQUE(id),
        PRIMARY KEY(id),
        FOREIGN KEY(state_id)
            REFERENCES hbtn_0d_usa.states(id)
    )
