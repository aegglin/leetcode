/*
  Prompt: Suppose that a website contains two tables, the Customers table and the Orders table. 
  Write a SQL query to find all customers who never order anything.
*/

SELECT Name AS Customers
FROM Customers
WHERE Id NOT IN (SELECT c.Id
FROM Customers c INNER JOIN Orders o on c.Id = o.CustomerId)

# Here the join is not strictly necessary, as just selecting CustomerId from Orders will suffice to see who has ordered. 
