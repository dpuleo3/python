SELECT *
FROM nomnom;

--  distinct neighborhood
SELECT DISTINCT neighborhood
FROM nomnom;

-- distinct cuisine types
SELECT DISTINCT cuisine 
FROM nomnom;

-- Chinese takeout options
FROM nomnom
WHERE cuisine = 'Chinese';

-- Return all the restaurants with reviews of 4 and above
FROM movies
WHERE REVIEW > 4;

-- Return all the restaurants that are Italian and $$$.
FROM nomnom
WHERE cuisine = 'Italian'
   AND price = '$$$';

--  he knows it contains the word ‘meatball’ in it.
FROM nomnom
WHERE name LIKE '%meatball%';

-- Find all the close by spots in Midtown, Downtown or Chinatown.
FROM nomnom
WHERE neighborhood = 'Midtown'
  OR neighborhood = 'Downtown'
  OR neighborhood = 'Chinatown';

-- Find all the health grade pending restaurants
SELECT *
FROM nomnom
WHERE health IS NULL;

-- Top 10 Restaurants Ranking based on review
SELECT *
FROM nomnom
ORDER BY review DESC
LIMIT 10;

-- Change the rating system
SELECT name,
 CASE
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
 END AS 'Review'
FROM nomnom;
