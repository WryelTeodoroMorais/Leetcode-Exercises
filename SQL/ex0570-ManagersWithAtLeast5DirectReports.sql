SELECT E.name
FROM Employee as E
WHERE (SELECT COUNT (E1.id) FROM Employee as E1 WHERE E.id = E1.managerID) > 4