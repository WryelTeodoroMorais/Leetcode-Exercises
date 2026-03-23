DELETE P
FROM Person P, Person P1
WHERE P.email = P1.email and P.id > P1.id