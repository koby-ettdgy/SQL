/* Get a column form a table*/ 
SELECT column name
FROM table name;

/* Get a few columns from a table */

SELECT column1, column2, column3
FROM table name;

/* Get all the columns in a table */

SELECT * 
FROM table name;

/* To get only uniqe vlaus from a column */

SELECT DISTINCT column
FROM table name;

/* to limit the number of row retrieved from a column*/

SELECT column
FROM table name
LIMIT 5;

/* Sorting Retrieved DATA */

/* Use Order By */

/* sort by on columnm */

SELECT column
FROM table name
ORDER BY  column; 

/* sort by multiple column*/

ELECT column1, column2, column3
FROM table name
ORDER BY  column1 , column3;

/* sort by direction */

SELECT column
FROM table name
ORDER BY  column [ASC|DESC];

/* ASC -down to up
   DESC - up to down
*/

