SELECT A.id
FROM Weather as A
INNER JOIN Weather as B on DATEDIFF(day, B.recordDate, A.recordDate) = 1
WHERE A.temperature > B.temperature 