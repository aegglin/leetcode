SELECT FirstName, LastName, City, State
FROM Person as p LEFT join Address as a on p.PersonId = a.PersonId
