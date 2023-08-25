-- SQLite
SELECT first_table.id,first_table.name, second_table.score FROM first_table, second_table, third_table WHERE
    first_table.id = third_table.first_id AND
    third_table.second_id=second_table.id; 

SELECT * FROM first_table;

SELECT * FROM second_table;