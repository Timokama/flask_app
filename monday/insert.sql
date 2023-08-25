-- SQLite
INSERT OR REPLACE INTO first_table ('id','name') VALUES 
    (1,"Timothy Munyiri");
INSERT OR REPLACE INTO second_table ('id', "score", 'name_id') VALUES 
    (1, 20, 1);

DELETE FROM second_table WHERE id > 5;
SELECT * FROM first_table;
SELECT * FROM second_table;