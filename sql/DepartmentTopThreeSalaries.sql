# Top N per group SQL solution

# The Employee table holds all employees. Every employee has an Id, and there is also a column for the department Id.
# +----+-------+--------+--------------+
# | Id | Name  | Salary | DepartmentId |
# +----+-------+--------+--------------+
# | 1  | Joe   | 85000  | 1            |
# | 2  | Henry | 80000  | 2            |
# | 3  | Sam   | 60000  | 2            |
# | 4  | Max   | 90000  | 1            |
# | 5  | Janet | 69000  | 1            |
# | 6  | Randy | 85000  | 1            |
# | 7  | Will  | 70000  | 1            |
# +----+-------+--------+--------------+
#
# The Department table holds all departments of the company.
# +----+----------+
# | Id | Name     |
# +----+----------+
# | 1  | IT       |
# | 2  | Sales    |
# +----+----------+
# Write a SQL query to find employees who earn the top three salaries in each of the department. 

SELECT d.Name AS Department, e1.Name AS Employee, e1.Salary
FROM Employee e1 LEFT JOIN Employee e2 ON e1.DepartmentId = e2.DepartmentId AND e1.Salary < e2.Salary 
                      JOIN Department d ON e1.DepartmentId = d.Id
GROUP BY e1.Name
HAVING COUNT(DISTINCT e2.Salary) < 3
ORDER BY e1.Salary DESC, d.Name ASC
