SELECT FirstName, LastName, City, State
FROM Person as p LEFT JOIN Address AS a ON p.PersonId = a.PersonId
