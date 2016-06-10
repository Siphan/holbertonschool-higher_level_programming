/* Update Jon Snow's age */
UPDATE Person SET age=27 WHERE first_name='Jon';
/* Update Walter Junior White's age */
UPDATE Person SET age=18 WHERE first_name='Walter Junior';
/* Delete Walter White from table Person */
DELETE FROM Person WHERE id = 1;
/* Delete Walter White from table EyesColor */
DELETE FROM EyesColor WHERE person_id =1;
/* Display all Person with all attributes ordered by first_name */
SELECT * FROM Person ORDER BY first_name;
