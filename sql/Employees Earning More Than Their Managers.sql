/* 
  The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
  Fun little question with a self-join necessary because all the information is contained in one table. 
*/

SELECT e1.Name AS Employee
FROM Employee e1 JOIN Employee e2 ON e1.ManagerId=e2.Id
WHERE e1.Salary > e2.Salary
