/* Display all distinct last_name of the TVShow = Game of Thrones ordered by last_name ascending */
SELECT DISTINCT last_name
FROM   person P
      JOIN tvshowperson TSP
      	   ON P.id = TSP.person_id
      JOIN tvshow TS
           ON TS.id = TSP.tvshow_id
WHERE  TS.NAME = 'Game of Thrones'
ORDER  BY P.last_name ASC;

/* Display the number of Person where the age is greater than 30 */
SELECT Count(id)
FROM   person
WHERE  age > 30;

/* Display all Person records with all information from other tables */
SELECT P.id,
       first_name,
       last_name,
       age,
       color,
       NAME
FROM   person P
       JOIN eyescolor E
           ON P.id = E.person_id
       JOIN tvshowperson TSP
	   ON P.id = TSP.person_id
       JOIN tvshow TS
           ON TS.id = TSP.tvshow_id;

/* Sum of age of all Person */
SELECT Sum(age)
FROM   person; 
