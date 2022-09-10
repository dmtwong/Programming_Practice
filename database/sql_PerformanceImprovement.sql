/* 
You are given a table having the marks of one student in every test (Tests are held every day) . 
You have to output the tests in which the student has improved his performance. For a student to improve 
his performance he has to score more than the previous test.
Table : TestId(Int) Marks(Int) 
NOTE : The output should contain one column by the name ‘TestId’ .
   YOUR QUERY GOES HERE
   Example: SELECT * FROM EMPLOYEE; 

# Select TestId from
# Select TestId Marks - lag(Marks) OVER (ORDER BY TestId) Changes,
# from Tests 
# where changes > 0
*/
SELECT Tests.TestId 
FROM Tests 
JOIN Tests AS Test2
    ON Test2.TestId = Tests.TestId - 1
    WHERE  Tests.Marks > Test2.Marks