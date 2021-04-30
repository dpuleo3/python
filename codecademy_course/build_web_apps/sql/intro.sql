-- Statements
CREATE TABLE table_name (
   column_1 data_type, 
   column_2 data_type, 
   column_3 data_type
);

-- CREATE TABLE is a clause. 
-- Clauses perform specific tasks in SQL. By convention, clauses are written in capital letters. 
-- Clauses can also be referred to as commands. 
-- table_name refers to the name of the table that the command is applied to.
-- (column_1 data_type, column_2 data_type, column_3 data_type) is a parameter.
--  A parameter is a list of columns, data types, or values that are passed to a clause as an argument. 
--  Here, the parameter is a list of column names and the associated data type.


-- Create
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);

-- 1. CREATE TABLE is a clause that tells SQL you want to create a new table.
-- 2. celebs is the name of the table.
-- 3. (id INTEGER, name TEXT, age INTEGER) is a list of parameters defining each column, or attribute in the table and its data type:

-- id is the first column in the table. It stores values of data type INTEGER
-- name is the second column in the table. It stores values of data type TEXT
-- age is the third column in the table. It stores values of data type INTEGER


-- Insert
-- inserts rows
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22); 

INSERT INTO celebs (id, name, age) 
VALUES (2, 'Beyonce Knowles', 33); 

INSERT INTO celebs (id, name, age) 
VALUES (3, 'Jeremy Lin', 26); 

INSERT INTO celebs (id, name, age) 
VALUES (4, 'Taylor Swift', 26);


-- Select
SELECT name FROM celebs; 
SELECT age FROM celebs; 


-- Alter
-- "twitter_handle" is the name of the new column being added
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT; 

SELECT * FROM celebs; 


-- Update
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4; 

SELECT * FROM celebs;


-- Delete
-- Delete all of the rows that have a NULL value in the twitter handle column. 
DELETE FROM celebs 
WHERE twitter_handle IS NULL;

SELECT * FROM celebs; 


-- Constraints
-- add information about how a column can be used are invoked after specifying the data type for a column.
CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'
);


-- Review
-- A statement is a string of characters that the database recognizes as a valid command.

-- CREATE TABLE creates a new table.
-- INSERT INTO adds a new row to a table.
-- SELECT queries data from a table.
-- ALTER TABLE changes an existing table.
-- UPDATE edits a row in a table.
-- DELETE FROM deletes rows from a table.