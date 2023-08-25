-- SQLite

CREATE TABLE IF NOT EXISTS second(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    score INT);

CREATE TABLE IF NOT EXISTS first (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS third (
    first_id INTEGER,
    second_id INTEGER
);
INSERT INTO third VALUES
    (1,1),
    (2,2),
    (3,3),
    (4,4);
INSERT INTO first VALUES
    (1,"John"),
    (2,"Kelvin"),
    (3,"Mark"),
    (4,"George");

INSERT INTO second VALUES 
    (1,"John", 10),
    (2,"Kelvin", 4),
    (3,"Mark", 15),
    (4,"George", 9);
    
SELECT * FROM second;
SELECT* FROM first;
SELECT* FROM third;

SELECT first.id, first.name, second.score FROM first, second, third
    WHERE
    first.id=third.first_id AND
    first_id =  second.id;
SELECT sum(score) AS Total_score FROM second;

