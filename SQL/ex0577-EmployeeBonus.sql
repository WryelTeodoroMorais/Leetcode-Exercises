SELECT name, bonus
FROM Employee as E LEFT JOIN Bonus as B on E.empId = B.empId
WHERE bonus < 1000 or bonus is NULL