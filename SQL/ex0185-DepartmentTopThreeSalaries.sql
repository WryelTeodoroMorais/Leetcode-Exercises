SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee as E JOIN Department as D on E.departmentId = D.id
WHERE 
(
    SELECT COUNT(DISTINCT Salary)
    FROM Employee as E2 
    WHERE E2.departmentId = E.departmentId and E2.salary > E.salary
) < 3
ORDER BY E.salary DESC;