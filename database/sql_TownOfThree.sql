/* YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 
   Given a table TOWNS, query for all the Town Names and Population, such that the ID is a multiple of 3.

The description of the table TOWNS is as given below:
    The description of the table Towns is given below:
    id, TownCode, Population (INT), TownName(VARCHAR)
NOTE : The output should contain 2 columns ‘TownName’ and ‘Population’


*/
SELECT TownName, Population
FROM TOWNS
WHERE mod(ID, 3) = 0

/*
SELECT TownName, Population FROM TOWNS WHERE ID % 3 = 0;
*/
