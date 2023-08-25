-- SQLite
CREATE TABLE If NOT EXISTS first_table(
    id INT PRIMARY KEY,
    name VARCHAR(256)
);

CREATE TABLE If NOT EXISTS second_table(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    score INT
);

CREATE TABLE IF NOT EXISTS third_table(
    first_id INTEGER,
    second_id INTEGER
);

INSERT OR REPLACE INTO first_table (id, name) VALUES
    (1,"Timothy"),
    (2,"Jane"),
    (3,"Ken"),
    (4,"Daniel"),
    (5,"mark");

INSERT OR REPLACE INTO second_table (id,name, score) VALUES
    (1,"Timothy", 30),
    (2,"Jane", 20),
    (3,"Ken", 20),
    (4,"Daniel", 30),
    (5,"mark",20);

-- INSERT OR REPLACE INTO third_table (first_id, second_id) VALUES
--     (1,1),
--     (2,2),
--     (3,3),
--     (4,4),
--     (5,5);

-- DELETE  FROM third_table WHERE first_id IN(
--     SELECT DISTINCT first_id
-- );


SELECT * FROM first_table;

SELECT * FROM second_table;

SELECT * FROM third_table;