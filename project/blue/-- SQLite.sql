-- SQLite
CREATE TABLE table1 (
    id INTEGER PRIMARY KEY,
    name TEXT,
    talent String(255)
    );

INSERT INTO table1 (name, talent) VALUES (
    "Timothy Kamau", "Drawing");

INSERT INTO table1 (name, talent) VALUES (
    "Jane Kanyi", "Dancing");

INSERT INTO table1 (name, talent) VALUES (
    "Kelvin Ken", "Playing basketball");

INSERT INTO table1 (name, talent) VALUES (
    "Poul Makhenzi", "Preacher");

SELECT * FROM table1;
