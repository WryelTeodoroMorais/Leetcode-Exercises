SELECT E.name as Employee
FROM Employee as E, Employee as E1
WHERE E.salary > E1.salary and E.managerId = E1.id