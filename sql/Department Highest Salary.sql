# The Employee table holds all employees. 
# Every employee has an Id, a salary, and there is also a column for the department Id.
# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 70000  | 1            |
# | 2  | Jim   | 90000  | 1            |
# | 3  | Henry | 80000  | 2            |
# | 4  | Sam   | 60000  | 2            |
# | 5  | Max   | 90000  | 1            |
# +----+-------+--------+--------------+

# The Department table holds all departments of the company.
# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who have the highest salary in each of the departments. 
# For the above tables, your SQL query should return the following rows (order of rows does not matter).

SELECT d.Name AS Department, e.Name AS Employee, e.Salary
FROM Employee e JOIN DEPARTMENT d ON e.DepartmentId = d.Id
WHERE (e.Salary, e.DepartmentId) IN 
    (SELECT MAX(Salary), DepartmentId
    FROM Employee
    GROUP BY DepartmentId)
