/* YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 
  Given a table STUDY, update the marks of all the students to 50, whose marks lie in the range 25 - 50
   (excluding 25 , including 50 i.e. (25,50] ) . Then print the new table.

The description of the table STUDY is given below: 
   ID,AGE, MARKS(INT)
Name (VARCHAR 255)

Note: Create a copy of the original table.
*/
CREATE TABLE STUDY2 AS SELECT * FROM STUDY;

UPDATE STUDY2 SET Marks = 50 
WHERE Marks IN (SELECT Marks FROM STUDY WHERE Marks > 25 and Marks <= 50);
    
SELECT * FROM STUDY2;