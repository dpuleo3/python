-- Select
SELECT * FROM movies;

SELECT name, genre, year 
FROM movies;


-- As
--  the result, that the name of the column is now your alias.
SELECT name AS 'movie name'
FROM movies;

SELECT imdb_rating  AS 'IMDb'
FROM movies;


-- Distinct
-- DISTINCT is used to return unique values in the output. It filters out all duplicate values in the specified column(s).
SELECT DISTINCT genre 
FROM movies;

SELECT DISTINCT year 
FROM movies;


-- Where
-- Comparison operators used with the WHERE clause are:
-- = equal to
-- != not equal to
-- > greater than
-- < less than
-- >= greater than or equal to
-- <= less than or equal to
SELECT * 
FROM movies 
WHERE imdb_rating < 5;

SELECT * 
FROM movies 
WHERE year > 2014;


-- Like 
-- can be a useful operator when you want to compare similar values.

-- The movies table contains two films with similar titles, ‘Se7en’ and ‘Seven’.
SELECT * 
FROM movies
WHERE name LIKE 'Se_en';

-- A% matches all movies with names that begin with letter ‘A’
-- %a matches all movies that end with ‘a’
SELECT * 
FROM movies
WHERE name LIKE '%man%';

SELECT * 
FROM movies
WHERE name LIKE 'The %';


-- Is Null
-- find all the movies without an IMDb rating.
SELECT name
FROM movies
WHERE imdb_rating IS NULL;

-- To filter for all movies with an IMDb rating:
SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;


-- Between
-- The BETWEEN operator is used in a WHERE clause to filter the result 
-- set within a certain range. It accepts two values that are either numbers, text or dates.
SELECT *
FROM movies
WHERE name BETWEEN 'D' AND 'G';

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979;


-- And
-- AND operator displays a row if all the conditions are true.
SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979
  AND imdb_rating > 8;

SELECT *
FROM movies
WHERE year < 1985
  AND genre = 'horror';


-- Or
-- OR operator displays a row if any condition is true.
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';

SELECT *
FROM movies
WHERE genre = 'romance'
   OR genre = 'comedy';


-- Order By
--  ordered by their name alphabetically.
SELECT name, year
FROM movies
ORDER BY name;

-- query that retrieves the name, year, and imdb_rating columns of all the movies, ordered highest to lowest by their ratings.
SELECT name, year, imdb_rating
FROM movies
ORDER BY imdb_rating DESC;


-- Limit
--  top 3 highest rated movies.
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;


-- Case
-- Each WHEN tests a condition and the following THEN gives us the string if the condition is true.
-- The ELSE gives us the string if all the above conditions are false.
-- The CASE statement must end with END.
SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy'  THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;


-- Review
-- SELECT is the clause we use every time we want to query information from a database.
-- AS renames a column or table.
-- DISTINCT return unique values.
-- WHERE is a popular command that lets you filter the results of the query based on conditions that you specify.
-- LIKE and BETWEEN are special operators.
-- AND and OR combines multiple conditions.
-- ORDER BY sorts the result.
-- LIMIT specifies the maximum number of rows that the query will return.
-- CASE creates different outputs.