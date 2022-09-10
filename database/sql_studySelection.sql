/* YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 
Given a table STUDY, query for all the attributes, which have marks greater than 80.

The description of the table STUDY is given below:
ID,AGE, MARKS(INT)
Name (VARCHAR 255)
NOTE : The output should contain 4 columns  ‘ID’ , ‘Name’ ,’Age’ and ‘Marks’ .
*/

SELECT *
FROM STUDY
WHERE marks > 80

/*
SELECT * FROM STUDY WHERE ID IN (SELECT ID FROM STUDY WHERE Marks > 80);
*/